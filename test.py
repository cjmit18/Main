import random
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else "clear")
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
    while True:
        mode: str = input("Select game mode: Computer, Multiplayer or Exit: ").lower()
        if mode in ["computer","multiplayer","exit"]:
            return mode
        print("Please choose a valid mode.")
def difficulty() -> str:
     while True:
        diff: str = input("Select Difficulty: Easy, Medium, Hard ").lower()
        if diff in ["easy","medium","hard"]:
            return diff
        print("Invalid difficulty")

def running_game() -> tuple:
    wins, losses, ties, rounds = 0, 0, 0, 0
    mode = mode_choice()
    if mode == "computer":
        diff = difficulty()

    while True:
        win,lose,tie = False,False,False
        if mode == "exit":
            return wins,losses,ties,rounds
        
        user = user_choice()
        if user == "stats":
            print(f"wins: {wins}, Ties: {ties}, Losses: {losses} rounds: {rounds}")
            continue 
        if user == "exit":
            return wins,losses,ties,rounds
        
        if mode == "computer":
            choice: str = computer_choice(diff,user)
        elif mode == "multiplayer":
            clear_screen()
            choice = multiplayer_choice()
        if choice == "stats":
            print(f"wins: {wins}, Ties: {ties}, Losses: {losses} rounds: {rounds}")
            continue
        if user not in ["rock", "paper","scissors"] or choice not in ["rock", "paper", "scissors"]:
            print("Choose a valid option")
            continue

        if user == "rock" and choice == "scissors" or user == "paper" and choice == "rock" or user == "scissors" and choice == "paper":
            wins += 1
            print(f" You chose {user} and player 2 chose {choice} and won!")
        elif user == choice:
            ties += 1
            print(f"You both chose {user} and Tied!")
        else:
            losses += 1
            print(f"You chose {user} and lost! your opponent chose {choice}")
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