from swarm import Agent

def summarize_report(context_variables):
    earnings_report = context_variables["report_text"]
    return f"Summary: {earnings_report[:100]}..."

summary_agent = Agent(
    name="Summary Agent",
    instructions="Summarize the key points of the earnings report.",
    functions=[summarize_report]
)
