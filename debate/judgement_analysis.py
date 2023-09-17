
# notes/questions/thoughts:

# - Really hard to not let information symmetry
#   in the queries affect the outcome (ordering, names etc.).
#   Tried to avoid to some extend by choosing neutral names
#   or doing douple queries (with switched order) - other methods?

# - Initially I tried to get the judgement be a number (0-10).
#   this did not work at all (almost always completed with 5).
#   is there a way to get semi-uniform  numerical classifications
#   out of an LLM in a reasonable way?

# - This made me understand why ICE is useful!

# - GPT-3 is very unreasonable a lot of the time in debates.

from ice.recipe import recipe

from recipe import debate as debate_question
from prompt import debate_judgement_prompts, oneshot_prompt, questions_prompt


async def judgement_analysis():
    prompt = questions_prompt(10)
    questions = (await recipe.agent()
                 .complete(prompt=prompt, stop="---")).split("\n")
    all_judgements = {}
    for question in questions:
        debate_res = await debate_judgement(question)
        non_debate_res = await oneshot_judgement(question)
        all_judgements[question] = {
            "oneshot": non_debate_res,
            "debate:": debate_res
        }
    return all_judgements


async def oneshot_judgement(question: str) -> str:
    prompt = oneshot_prompt(question)
    answer = await recipe.agent().complete(prompt=prompt, stop='"')
    return answer


async def debate_judgement(question: str) -> str:
    agent_names = ["Proponent", "Opponent"]
    debate = await debate_question(question, agent_names)
    prompts = debate_judgement_prompts(debate, agent_names)
    results = []
    for p in prompts:
        answer = await recipe.agent().complete(prompt=p, stop='"')
        results.append(answer)

    if all((a == results[0] for a in results)):
        return results[0]
    else:
        return "Mixed"

if __name__ == "__main__":
    recipe.main(judgement_analysis)
