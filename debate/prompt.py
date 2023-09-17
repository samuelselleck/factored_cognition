import itertools
from fvalues import F

from debate_types import Debate, Name
from utils import render_debate, render_list_permutations


def render_debate_prompt(agent_name: str, debate: Debate, turns_left: int) -> str:
    prompt = F(
        f"""
You are {agent_name}. There are {turns_left} turns left in the debate. You are trying to win the debate using reason and evidence. Don't repeat yourself. No more than 1-2 sentences per turn.

{render_debate(debate, agent_name)}
You: "
"""
    ).strip()
    return prompt


def debate_judgement_prompts(debate: Debate, agents: list[Name]) -> int:
    prompts = []
    for names in render_list_permutations(agents):
        prompt = F(
            f"""
Debate:
{render_debate(debate)}

Who won this debate? (answer with one of the following):

{names}

Answer: "
""").strip()
        prompts.append(prompt)
    return prompts


def oneshot_prompt(question: str) -> str:
    prompt = F(f"""
Who would be more likely to win a debate about: 
"{question}"

1. "Proponent"
2. "Opponent"

Answer: "
    """).strip()
    return prompt


def questions_prompt(num: int = 4) -> list[str]:
    prompt = F(f"""
This is a list of 4 questions:
---
Should we legalize all drugs?
Should we allow civilians to build nuclear bombs?
Should we subsidise birthday parties?
Should we create powerful AIs?
---

Provide another list with the same formatting
(no numbering) with {num} controversial
and still societally undecided questions to debate:
---
""").strip()
    return prompt
