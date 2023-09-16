from typing import Optional
from fvalues import F

from debate_types import Message, Debate, Name


def initialize_debate(question: Message) -> Debate:
    return [
        ("Question", question),
        ("Proponent", "I'm in favor."),
        ("Opponent", "I'm against."),
    ]


def render_debate(debate: Debate, self_name: Optional[Name] = None) -> str:
    debate_text = ""
    for speaker, text in debate:
        if speaker == self_name:
            speaker = "You"
        debate_text += F(f'{speaker}: "{text}"\n')
    return debate_text.strip()
