import dataclasses


@dataclasses.dataclass
class Slot:
    name: str
    content: str


@dataclasses.dataclass
class IntentHandler:
    slots: list[Slot]


@dataclasses.dataclass
class UserResponse:
    syntaxes: list[str]
    unexpected_syntaxes: list[str]
    data: list[object]
    ask: str

    is_unexpected = False

    def __init__(self, syntaxes: list[str], unexpected_syntaxes: list[str]):
        self.syntaxes = syntaxes
        self.unexpected_syntaxes = unexpected_syntaxes
        self.data = [0] * 100
