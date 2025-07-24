# 🧠 YouTube Blog Generator with CrewAI

This project automates the process of researching YouTube videos and generating blog posts using [CrewAI](https://github.com/joaomdmoura/crewAI), custom AI agents, and a YouTube content search tool.

It performs two main tasks:
1. **Research**: Finds a video on a given topic from a specific YouTube channel and extracts relevant information.
2. **Writing**: Summarizes the information and generates a structured blog post.

---
```text
## 📁 Project Structure
├── agents.py # Defines the AI agents for research and writing
├── tools.py # Sets up the YouTube search tool
├── tasks.py # Describes the tasks assigned to each agent
├── crew.py # Orchestrates and runs the agents and tasks
├── .env # Stores environment variables (API keys)
├── new-blog-post.md # Final blog output file
└── README.md # Project documentation
```
---

## 🔧 How It Works

### 1. `tools.py`: YouTube Search Tool

This file sets up a search tool using the `YoutubeChannelSearchTool` from `crewai_tools`. It targets a specific channel (`@JeffSu`) to find relevant videos.

```python
from crewai_tools import YoutubeChannelSearchTool

yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@channelname')
```
### 2. `agents.py`: AI Agents
Two CrewAI agents are defined:

#### Blog Researcher

- Role: Finds and analyzes relevant video content.

- Goal: Understand complex tech topics like AI, ML, and Generative AI.

- Tool: yt_tool

- Features: Verbose output, memory enabled, delegation allowed.

#### Blog Writer

- Role: Writes an engaging blog post from research.

- Goal: Convert technical content into a clear, readable blog.

- Tool: yt_tool

- Features: Verbose output, memory enabled, no delegation.

These agents are built using crewai.Agent.

### 3. `tasks.py`: Task Definations
Two main tasks are assigned to the agents:

Research Task

Description: Locate a video on {topic} and extract detailed content.

Expected Output: A three-paragraph article with a suitable title.

Assigned Agent: blog_researcher

Tool: yt_tool

Writing Task

Description: Use the research to generate a blog post.

Expected Output: Blog content in Markdown format.

Assigned Agent: blog_writer

Tool: yt_tool

Async: Set to False for sequential execution.

Output File: new-blog-post.md

### 4. `crew.py` : Running the Workflow
This file uses the Crew class to tie agents and tasks together. It defines how the process should run (sequentially) and starts execution with a specific topic.
```python
from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, writing_task

crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

result = crew.kickoff(inputs={'topic': 'AI Agents, Clearly Explained'})
print(result)
```
This will generate the blog content and save it in `new-blog-post.md`.

## ✅ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
```
### 2. Install dependencies

Make sure you have Python 3.8 or higher.
```bash
pip install -r requirements.txt
```
### 3. Set up environment variables
Create a `.env` file in the root directory and add your OpenAI API key:
```ini
OPENAI_API_KEY=your_openai_api_key
```
### 4. Run the application
``` bash
python crew.py
```
This will:
- Search a YouTube channel for the given topic

- Extract relevant content

- Generate a blog post in new-blog-post.md

## 📝 Example Output
The final output will be a well-written blog post including:

- A relevant title

- Three concise, informative paragraphs

- Markdown formatting

- Content derived from an actual YouTube video


