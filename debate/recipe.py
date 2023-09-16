from ice.recipe import recipe
from ice.agents.base import Agent

from prompt import render_debate_prompt
from debate_types import Debate, Name
from utils import initialize_debate


async def turn(
    debate: Debate,
    agent: Agent,
    agent_name: Name,
    turns_left: int
):
    prompt = render_debate_prompt(agent_name, debate, turns_left)
    answer = await agent.complete(prompt=prompt, stop="\n")
    return (agent_name, answer.strip('" '))


async def debate(
    question: str = "Should we legalize all drugs?",
    agent_names: list[Name] = ["Alice", "Bob"],
):
    agents = [recipe.agent(), recipe.agent()]
    debate = initialize_debate(question)
    turns_left = 8
    while turns_left > 0:
        for agent, agent_name in zip(agents, agent_names):
            response = await turn(debate, agent, agent_name, turns_left)
            debate.append(response)
            turns_left -= 1
    return debate


if __name__ == "__main__":
    recipe.main(debate)
