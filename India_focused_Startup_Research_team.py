from agno.agent.agent import Agent
from agno.models.groq import Groq
from agno.team.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

startup_researcher = Agent(
    name="startup_researcher",
    role="Indian Startup Researcher",
    model=Groq(id="llama-3.1-8b-instant"),
    instructions=(
        "You research Indian startups, funding rounds, and founders. "
        "Prioritize up-to-date sources and India-specific news."
    ),
    tools=[DuckDuckGoTools(enable_search=True, enable_news=True)],
    markdown=True,
)

summary_writer = Agent(
    name="summary_writer",
    role="Insight Summarizer",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=(
        "You turn raw research into a 1-page summary with sections: Overview, Key Players, Funding, Opportunities."
    ),
    markdown=True,
)

startup_team = Team(
    model=Groq(id="llama-3.3-70b-versatile"),
    members=[startup_researcher, summary_writer],
    name="india_startup_team",
    instructions="""
    You are a startup insights team.
    First, use startup_researcher to collect data on the topic.
    Then, use summary_writer to synthesize it into a structured brief.
    """,
    show_members_responses=True,
    get_member_information_tool=True,
    add_member_tools_to_context=True,
)

startup_team.print_response(
    "Research notable Indian AI startups and summarize their focus areas.",
    stream=True,
)