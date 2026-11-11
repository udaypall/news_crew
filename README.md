# Two-Agent CrewAI Tech Newsletter

## Project Overview

This project demonstrates a two-agent AI crew built using **CrewAI**, **Python**, **SerperDevTool**, and **OpenAI**.

The crew automatically researches the latest technology news and generates a concise newsletter containing five numbered points.

The project uses sequential execution, where the Researcher passes its findings to the Writer.

## Agents

### 1. Technology News Researcher
- Searches the web using SerperDevTool.
- Identifies today's top three technology news stories.
- Focuses on AI, cybersecurity, technology companies, and innovation.
- Provides headlines, summaries, publication dates, and source URLs.

### 2. Technology Newsletter Writer
- Receives research findings from the Researcher.
- Does not have any search tools.
- Converts research into a concise newsletter.
- Produces exactly five numbered points under an unnumbered heading.

## Workflow

1. Researcher searches the web for the latest technology news.
2. Researcher identifies and summarizes three important stories.
3. Research output is passed to the Writer using `context=[find]`.
4. Writer prepares the final newsletter.
5. CrewAI executes both tasks sequentially using `Process.sequential`.

## Technologies Used

- Python
- CrewAI
- CrewAI Tools
- SerperDevTool
- OpenAI API
- python-dotenv

## Project Structure

```text
news_crew/
│
├── venv/
├── .env
├── .gitignore
├── news_crew.py
├── requirements.txt
└── README.md
```

## Installation

### Step 1: Create and activate virtual environment

```cmd
python -m venv venv
venv\Scripts\activate
```

### Step 2: Install dependencies

```cmd
pip install -r requirements.txt
```

### Step 3: Configure API keys

Create a `.env` file in the project directory.

```env
OPENAI_API_KEY=your_openai_api_key
MODEL=openai/gpt-4o-mini
SERPER_API_KEY=your_serper_api_key
```

API key registration:

- OpenAI: https://platform.openai.com/api-keys
- Serper: https://serper.dev/

**Important:** Never upload your `.env` file or API keys to GitHub.

## Running the Application

Execute the following command in CMD:

```cmd
python news_crew.py
```

The Researcher will search for current technology news, followed by the Writer generating the newsletter.

## Expected Output

```text
Tech in 5 lines

1. First technology news story.
2. Second technology news story.
3. Third technology news story.
4. An important additional technology insight.
5. Why it matters: One concluding sentence.
```

## Key CrewAI Concepts Demonstrated

- Creating multiple AI agents.
- Assigning individual roles, goals, and backstories.
- Integrating external search tools.
- Creating sequential tasks.
- Passing task output using `context=[find]`.
- Configuring agents with an OpenAI LLM.
- Managing API keys through environment variables.

## GitHub Repository

[https://github.com/udaypall/news_crew.git](https://github.com/udaypall/news_crew.git)

