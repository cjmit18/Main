import Player_Settings
class Output:
    def __init__(self, setup_actions: list, game_actions: list) -> None:
        self.setup_actions = setup_actions
        self.game_actions = game_actions
        self.round_1 = []
        self.round_2 = []
        self.round_3 = []
    def set_actions(self, setup_actions: list, game_actions: list) -> None:
        self.setup_actions = setup_actions
        self.game_actions = game_actions
    def set_rounds(self, game_actions) -> int:
        self.round_1 = game_actions[0:3]
        self.round_2 = game_actions[3:6]
        self.round_3 = game_actions[6:9]
        return self.round_1, self.round_2, self.round_3
    def get_rounds(self) -> tuple:
        return self.round_1, self.round_2, self.round_3
    def get_all_actions(self) -> list:
        return self.setup_actions, self.game_actions
    def get_actions_setup(self) -> list:
        return self.setup_actions
    def get_actions_game(self) -> list:
        return self.game_actions
    
