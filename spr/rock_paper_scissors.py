import random

from response.response import get_response
from reusability import Response
from util.util import DEFAULT_UNEXPECTED

legal_choices_de = ["schere", "stein", "papier", "schere"]


def rock_paper_scissors(user_selection: str) -> str:
    response = Response(
        syntaxes=[
            "Ich nehme {0}.",
            "{0}.",
            "Ich wähle {0}.",
            "Ich habe mich für {0} entschieden.",
            "Okay. {0} ist meine Wahl."
        ],
        unexpected_syntaxes=DEFAULT_UNEXPECTED
    )

    user_selection = user_selection.lower()
    if user_selection in legal_choices_de:
        index = legal_choices_de.index(user_selection)
        selection = legal_choices_de[index + 1]
        response.data[0] = selection
    else:
        response.is_unexpected = True
    get_response(response)


if __name__ == '__main__':
    rock_paper_scissors(random.choice(legal_choices_de))
