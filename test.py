import random
def computer_choice(diff,user) -> str:
    if diff == "easy":
        if user == "rock":
            return random.choice(["scissors","rock"])
        elif user == "paper":
            return random.choice(["paper","rock"])
        elif user == "scissors":
            return random.choice(["scissors","paper"])
    elif diff == "medium":
        return random.choice(["rock","paper","scissors"])
    elif diff == "hard":
        if user == "rock":
            return random.choice(["rock","paper"])
        elif user == "paper":
            return random.choice(["paper","scissors"])
        else:
            return random.choice(["scissors", "rock"])
        
def user_choice() -> str: 
    return input("Choose rock, paper, or scissors: ").lower()
def multiplayer_choice() -> str:
    return input("Player 2 choose rock, paper, or scissors: ").lower()
def mode_choice() -> str:
    return input("Select game mode: Computer, Multiplayer or Exit: ").lower()
def difficulty() -> str:
     return input("Select Difficulty: Easy, Medium, Hard ")

def running_game() -> tuple:
    wins, losses, ties, rounds = 0, 0, 0, 0
    choice, user, diff = None, None, None
    win, lose, tie = None, None, None 
    while True:
        mode: str = mode_choice()
        if mode == "computer":
            diff: str = difficulty()
            if diff not in ["easy","medium","hard"]:
                print("Invalid Choice")
                continue
        if mode == "exit":
            return wins, losses, ties, rounds
        elif mode not in ["computer","multiplayer","exit"]:
            print("Invalid Option")
            continue
        break
    while True:
        win, lose, tie = False, False, False
        if mode == "computer":
            user: str = user_choice()
            if user == "exit":
                return wins,losses,ties,rounds
            choice: str = computer_choice(diff,user)
        elif mode == "multiplayer":
            user: str = user_choice()
            if user == "exit":
                return wins,losses,ties,rounds
            choice: str = multiplayer_choice()
            if choice == "exit":
                return wins,losses,ties,rounds
        if user == "stats" or choice == "stats":
             print(f"wins: {wins}, Ties: {ties}, Losses: {losses} rounds: {rounds}")
             continue
        if user == "rock" and choice == "scissors":
            win: bool = True
            wins += 1
        elif user == "paper" and choice == "rock":
                win: bool = True
                wins += 1
        elif user == "scissors" and choice == "paper":
                win: bool = True
                wins += 1
        elif user not in ["rock", "paper","scissors"] or choice not in ["rock", "paper", "scissors"]:
            print("Choose a valid option")
            continue
        elif user == choice:
            tie: bool = True
            ties += 1
        else:
            lose: bool = True
            losses += 1
        if win:
            print("You won")
        elif lose:
            print("You lost")
        elif tie:
            print("Its a tie")
        rounds += 1
        print(f"Round: {rounds}")
def main():
    while True:
        user: str = input("Menu Options: Start Game? (y/n) or Exit? ").lower()
        if user == "yes" or user == "y":
            game: tuple = running_game()
            wins, losses, ties, rounds = game[0], game[1], game[2], game[3]
            print(f'Wins: {wins} Losses: {losses} Ties: {ties} Rounds: {rounds}')
            break
        elif user == "exit":
            break
        else:
            print("Invalid Option")
            continue
if __name__ == '__main__':
    main()