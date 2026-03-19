from crewai import Task
from agents import web_agent, writer_agent, coder_agent, flight_agent

info_task = Task(
    description="""
Use the knowledge below to answer:

{web_context}

Question: {topic}
""",
    expected_output="Clear explanation",
    agent=web_agent
)

write_task = Task(
    description="""
Summarize clearly using:

{writer_context}

Topic: {topic}
""",
    expected_output="Simple explanation",
    agent=writer_agent,
    context=[info_task]
)

code_task = Task(
    description="""
Use knowledge:

{knowledge}

Write Python code for:
{topic}
""",
    expected_output="Only code block",
    agent=coder_agent
)

flight_task = Task(
    description="""
Use knowledge:

{knowledge}

Give top 3 flights:
{topic}
""",
    expected_output="[Flight | Time | Date]",
    agent=flight_agent
)
