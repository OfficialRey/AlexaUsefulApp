import random

DEFAULT_UNEXPECTED = [
    "Das habe ich leider nicht verstanden.",
    "Hmmm. Leider konnte ich das nicht verstehen.",
    "Entschuldige, aber ich bin mir nicht ganz sicher, ob ich das richtig verstanden habe.",
    "Kannst du das bitte wiederholen?",
    "Wow, du musst auch schon die Zähne auseinander nehmen.",
    "Wenn man so nuschelt wie du, wird man nicht verstanden.",
    "Kannst du dich auch deutlich ausdrücken?",
    "Man redet nicht mit vollem Mund.",
    "Vielleicht möchtest du es mit einer existierenden Sprache versuchen?",
    "Ich habe bereits eine Menge Blödsinn gehört, aber das übertrifft alles."
]


def get_response(response, handler_input):
    # Create response
    if response.is_unexpected:
        response_value = random.choice(response.unexpected_syntaxes)
        response_value = response_value.format(*response.data).lower()
    else:
        response_value = random.choice(response.syntaxes)
        response_value = response_value.format(*response.data).lower()

    return_value = handler_input.response_builder.speak(response_value)
    if response.ask is not None and response.ask != "":
        return_value = return_value.ask(response.ask)

    return (
        return_value.response
    )  # Used during playback


def get_slots(handler_input) -> dict:
    return handler_input.request_envelope.request.intent.slots
