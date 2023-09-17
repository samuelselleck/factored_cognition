import itertools
from typing import Optional
from fvalues import F

from debate_types import Message, Debate, Name


def initialize_debate(question: Message) -> Debate:
    return [
        ("Question", question),
        ("Proponent", "Yes."),
        ("Opponent", "No. Why?"),
    ]


def render_debate(debate: Debate, self_name: Optional[Name] = None) -> str:
    debate_text = ""
    for speaker, text in debate:
        if speaker == self_name:
            speaker = "You"
        debate_text += F(f'{speaker}: "{text}"\n')
    return debate_text.strip()


def render_list_permutations(elements: list[str]):
    perms = []
    for elems in itertools.permutations(elements):
        elem_str_list = "\n".join(
            (f'{n + 1}:"{name}"' for n, name in enumerate(elems))
        )
        perms.append(elem_str_list)
    return perms
