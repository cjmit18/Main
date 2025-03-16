import random
import tkinter as tk
roots = tk.TK()
def computer_choice() -> str:
    choice = random.randint(1,3)
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"
def user_choice() -> str:
      return input("Rock, Paper, or Scissors? ").lower()
def main():
    wins: int = 0
    losses: int = 0
    ties: int = 0
    while True:
        user: str = user_choice()
        computer: str = computer_choice()
        if user == "stats":
            print(f"Wins: {wins} Losses: {losses} Ties: {ties}")
            continue
        if user == "exit":
            return (wins, losses, ties)
        if user == "rock" and computer == "scissors":
            print("You win")
            wins += 1
        elif user == "paper" and computer == "rock":
                print("You win")
                wins += 1
        elif user == "scissor"  or user == "scissors" and computer == "paper":
                print("You win")
                wins += 1
        elif user == computer:
            print("Its a tie")
            ties += 1
        elif user not in ["rock", "paper", "scissor","scissors","stats"]:
            print("Choose a valid option")
            continue
        else:
            print("You lose")
            losses += 1
if __name__ == '__main__':
    while True:
        user = input("start game? ")
        if user == "yes" or user == "y":
           game = main()
           break
        else:
            print("Invalid Option")
    wins, losses, ties = game
print(f'Wins: {wins} Losses: {losses} Ties: {ties}')