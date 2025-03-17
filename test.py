import random
def computer_choice() -> str:
    choice = random.randint(1,3)
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"

def user_choice() -> str: 
    return input("Choose rock, paper, or scissors: ").lower()
def multiplayer_choice() -> str:
    return input("Player 2 choose rock, paper, or scissors: ").lower()
def mode_choice() -> str:
    return input("Select game mode: Computer, Multiplayer, Stats, or Exit: ").lower()


def running_game() -> tuple:
    wins, losses, ties = 0, 0, 0
    win, lose, tie = False, False, False
    round = 0
    choice, user = None, None
    win, lose, tie = None, None, None 
    mode = mode_choice()
    while True:
        if user == "stats" or mode == "stats":
            print(f"Wins: {wins} Losses: {losses} Ties: {ties}")
            continue
        elif mode == "exit" or user == "exit":
            return (wins, losses, ties, round)
        elif mode == "multiplayer":
            user = user_choice()
            if user == "exit":
                return (wins, losses, ties, round)
            choice = multiplayer_choice()
            if choice == "exit":
                return (wins, losses, ties, round)
        elif mode == "computer":
            user = user_choice() 
            if user == "exit":
                return (wins, losses, ties, round)
            choice = computer_choice()
            if choice == "exit":
                return (wins, losses, ties, round)
        if user == "rock" and choice == "scissors":
            win = True
            wins += 1
        elif user == "paper" and choice == "rock":
                win = True
                wins += 1
        elif user == "scissors" and choice == "paper":
                win = True
                wins += 1
        elif user == choice:
            ties += 1
        elif user not in ["rock", "paper","scissors"] or choice not in ["rock", "paper", "scissors"]:
            print("Choose a valid option")
        else:
            lose = True
            losses += 1
        round += 1
        if mode == "multiplayer":
            print(f"Player 1 chose {user} and Player 2 chose {choice} and {"player 1" if win else "player 2" if lose else None} {'won' if win else 'lost' if lose else 'tied'}!")
        else:
            print(f"You chose {user} and the computer chose {choice} and you {'won' if win else None}!")
        print(f"Round: {round}")
def main():
    while True:
        user: str = input("Menu Options: Start Game? (y/n) or Exit? ").lower()
        if user == "yes" or user == "y":
            game = running_game()
            wins, losses, ties = game[0], game[1], game[2]
            print(f'Wins: {wins} Losses: {losses} Ties: {ties}')
            break
        elif user == "exit":
            break
        else:
            print("Invalid Option")
            continue
if __name__ == '__main__':
    main()