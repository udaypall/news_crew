
import os
from datetime import date

from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool


# 1. Load environment variables
load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is missing in .env")

if not os.getenv("SERPER_API_KEY"):
    raise ValueError("SERPER_API_KEY is missing in .env")


# 2. Configure OpenAI model
model_name = os.getenv("MODEL", "openai/gpt-4o-mini")
llm = LLM(model=model_name)


# 3. Initialize Serper search tool
search_tool = SerperDevTool()

today = date.today().strftime("%B %d, %Y")


# 4. Create Researcher Agent
researcher = Agent(
    role="Technology News Researcher",

    goal=(
        "Find today's top 3 important and reliable "
        "technology news stories."
    ),

    backstory=(
        "You are an experienced technology journalist "
        "specializing in AI, cybersecurity, technology "
        "companies and innovation. You verify publication "
        "dates and prioritize credible sources."
    ),

    tools=[search_tool],
    llm=llm,
    verbose=True
)


# 5. Create Writer Agent
writer = Agent(
    role="Technology Newsletter Writer",

    goal=(
        "Convert research findings into a concise "
        "technology newsletter containing five numbered points."
    ),

    backstory=(
        "You are a professional technology newsletter editor. "
        "You write clear, engaging and informative news summaries. "
        "You only use information provided by the Researcher. "
        "You never perform independent web searches."
    ),

    llm=llm,
    verbose=True
)


# 6. Research Task
find = Task(
    description=(
        f"Research today's top 3 technology news stories "
        f"for {today}. "

        "Use web search to identify genuinely recent stories. "
        "Cover important developments in AI, technology "
        "companies, cybersecurity and innovation. "

        "Verify publication dates and avoid duplicate stories."
    ),

    expected_output=(
        "A structured research report containing exactly "
        "3 technology news stories. For each story include: "
        "headline, company or organization, publication date, "
        "a factual summary in 2-3 sentences, source name "
        "and original source URL. "
        "Use clear numbered sections."
    ),

    agent=researcher
)


# 7. Newsletter Writing Task
write = Task(
    description=(
        "Using ONLY the research provided by the Researcher, "
        "write a technology newsletter. "

        "Do not search the web or introduce unsupported stories. "

        "Start with the heading: Tech in 5 lines. "
        "Do NOT number the heading. "

        "Below the heading, provide exactly five numbered points. "
        "Each point must appear on a separate line. "

        "Points 1, 2 and 3: Three technology news stories. "
        "Point 4: An additional important insight based on "
        "the research. "
        "Point 5: Why it matters - a concluding sentence. "

        "Keep every point concise and on a single line."
    ),

    expected_output=(
        "A newsletter in exactly this format:\n\n"
        "Tech in 5 lines\n\n"
        "1. First technology news story.\n"
        "2. Second technology news story.\n"
        "3. Third technology news story.\n"
        "4. An important additional technology insight.\n"
        "5. Why it matters: One concluding sentence.\n\n"

        "The heading must NOT have a number. "
        "Only the five points below the heading must be numbered. "
        "Each point must be on one separate line. "
        "Do not add any other text."
    ),

    agent=writer,
    context=[find]
)


# 8. Create Crew
crew = Crew(
    agents=[researcher, writer],

    tasks=[find, write],

    process=Process.sequential,

    verbose=True
)


# 9. Execute Crew
if __name__ == "__main__":

    print("\nStarting Technology News Crew...\n")

    result = crew.kickoff()

    print("\n" + "=" * 50)
    print("          FINAL TECHNOLOGY NEWSLETTER")
    print("=" * 50 + "\n")

    print(result)

    print("\n" + "=" * 50)
