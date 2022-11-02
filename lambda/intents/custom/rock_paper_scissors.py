import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

from 


class RockPaperScissorsIntent(AbstractRequestHandler):

    def can_handle(self, handler_input, exception):
        return
        return ask_utils.is_request_type("RockPaperScissorsIntent")(handler_input)

    def handle(self, handler_input, exception):
        legal_choices_de = ["schere", "stein", "papier", "schere"]
        response = UserResponse(
            syntaxes=[
                "Ich nehme {0}.",
                "{0}.",
                "Ich wähle {0}.",
                "Ich habe mich für {0} entschieden.",
                "Okay. {0} ist meine Wahl."
            ],
            unexpected_syntaxes=util.DEFAULT_UNEXPECTED
        )
        handler_input
        user_selection = user_selection.lower()
        if user_selection in legal_choices_de:
            index = legal_choices_de.index(user_selection)
            selection = legal_choices_de[index + 1]
            response.data[0] = selection
        else:
            response.is_unexpected = True
        send_response(response)
