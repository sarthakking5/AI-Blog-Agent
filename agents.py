import os
from dotenv import load_dotenv
from crewai import Agent
from tools import yt_tool
from langchain_groq import ChatGroq
load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_MODEL_NAME']='gpt-4-0125-preview'

#roq_api_key=os.getenv("GROQ_API_KEY")



# Create a senior blog content researcher

blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='Get the relevant video content for the topic {topic} from YT Channel',
    verbose=True,
    memory=True,
    backstory=(
        'Expert in understanding videos in AI, Data Science, Machine Learning and Gen AI'
    ),
    tools=[yt_tool],
    allow_delegation=True
)

## Create a Senior blog writer Agent with YT Tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YouTube Channel',
    verbose=True,
    memory=True,
    backstory=("""
        With a flair for simplifying complex topics, you craft
        engaging narratives that captivate and educate, bringing new
        discoveries to light in and accessible manner.
        """),
    tools=[yt_tool],
    allow_delegation=False
)   