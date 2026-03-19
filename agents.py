from crewai import Agent, LLM
from crewai_tools import SerperDevTool
from image_agent import ImageAgent

# -------- LLM --------
llm = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0.3,
    max_tokens=300,
    top_p=0.9,
)

# -------- SERPER TOOL --------
search_tool = SerperDevTool()

# -------- WEB AGENT --------
web_agent = Agent(
    role="Research Analyst",
    goal="Find accurate information about {topic} using search tool.",
    backstory="Expert internet researcher.",
    tools=[search_tool],
    max_iter=2,
    llm=llm,
    verbose=True
)

# -------- WRITER --------
writer_agent = Agent(
    role="Content Writer",
    goal="Write simple explanation for {topic}.",
    backstory="Simplifies complex info.",
    llm=llm,
    verbose=True
)

# -------- CODER --------
coder_agent = Agent(
    role="Python Developer",
    goal="Write clean Python code for {topic}. Return ONLY code.",
    backstory="Expert programmer.",
    llm=llm,
    verbose=True
)

# -------- FLIGHT --------
flight_agent = Agent(
    role="Travel Planner",
    goal="Provide top 3 flights for {topic}.",
    backstory="Flight booking expert.",
    llm=llm,
    verbose=True
)

# -------- IMAGE (CUSTOM CLASS) --------
image_agent = ImageAgent(llm)
