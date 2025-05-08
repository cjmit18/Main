class game_state:
    def __init__(self,wins: int = 0, losses: int = 0, ties: int = 0, 
                 rounds: int = 0, diff: str = None, mode: str = None, player_two_wins: int = 0, player_two_losses: int = 0) -> None:
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.rounds = rounds
        self.mode = mode
        self.diff = diff
        self.player_two_wins = player_two_wins
        self.player_two_losses = player_two_losses
    def set_scores(self, wins: int, ties: int, losses: int, rounds: int) -> None:
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.rounds = rounds
    def set_player_two_scores(self, player_two_wins: int, player_two_losses: int) -> None:
        self.player_two_wins = player_two_wins
        self.player_two_losses = player_two_losses
    def set_mode(self, mode: str) -> None:
        self.mode = mode
    def set_diff(self, diff: str) -> None:
        self.diff = diff
    def get_scores(self) -> tuple:
        return self.wins, self.losses, self.ties, self.rounds
    def get_mode(self) -> str:
        return self.mode
    def get_diff(self) -> str:
        return self.diff
    def get_player_two_wins(self) -> int:
        return self.player_two_wins
    def get_player_two_losses(self) -> int:
        return self.player_two_losses
    def get_player_two_scores(self) -> tuple:
        return self.player_two_wins, self.player_two_losses