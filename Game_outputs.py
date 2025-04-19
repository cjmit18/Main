import Player_Settings
class Output:
    def __init__(self, actions: list = None, rounds: int = 0):
        self.actions = actions if actions is not None else []
    def set_actions(self, actions: list) -> None:
        self.actions = actions
    def get_actions(self) -> list:
        return self.actions
