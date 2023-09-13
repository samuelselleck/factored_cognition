

# notes/questions/thoughts:

# - Behaviour seems to be more and more extreme for each iteration,
#   What kinds of phrases or prompts makes it more likely to converge?
#
# - Other types of stop conditions that could be interesting:
#   - Prompt model for quality rating at each step
#     and choose best quality answer out of N
#   - Longer chain of quality ratings in regard to different metrics.

from fvalues import F

from ice.recipe import recipe


DEFAULT_CONTEXT = "We're running a hackathon on 9/9/2022 to decompose complex reasoning tasks into subtasks that are easier to automate & evaluate with language models. Our team is currently breaking down reasoning about the quality of evidence in randomized controlled trials into smaller tasks e.g. placebo, intervention adherence rate, blinding procedure, etc."

DEFAULT_QUESTION = "What is happening on 9/9/2022?"


def make_initial_prompt(context: str, question: str) -> str:
    return F(
        f"""
Background text: "{context}"

Answer the following question about the background text above:

Question: "{question}"
Answer: "
"""
    ).strip()


def make_refine_prompt(context: str, question: str, last_answer: str) -> str:
    return F(
        f"""
Background text: "{context}"
Question: "{question}"
Answer: "{last_answer}"
Improved Answer: "
"""
    ).strip()


async def answer(
    context: str = DEFAULT_CONTEXT, question: str = DEFAULT_QUESTION
) -> str:
    prompt = make_initial_prompt(context, question)
    answer = await recipe.agent().complete(prompt=prompt, stop='"')
    for i in range(5):
        prompt = make_refine_prompt(context, question, answer)
        answer = await recipe.agent().complete(prompt=prompt, stop='"')
    return answer


recipe.main(answer)
