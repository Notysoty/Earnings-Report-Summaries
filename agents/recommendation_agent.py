from swarm import Agent

def generate_recommendation(context_variables):
    sentiment = context_variables.get("sentiment", "neutral")
    recommendation = "Buy" if sentiment == "positive" else "Hold"
    return f"My recommendation is: {recommendation}"

recommendation_agent = Agent(
    name="Recommendation Agent",
    instructions="Provide investment recommendations based on the sentiment.",
    functions=[generate_recommendation]
)
