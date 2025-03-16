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
      return input("Rock, Paper, or Scissors? ").lower()
def running_game() -> tuple:
    wins: int = 0
    losses: int = 0
    ties: int = 0
    win: bool = None
    lose: bool = None
    tie: bool = None
    while True:
        user: str = user_choice()
        computer: str = computer_choice()
        win, lose, tie = False, False, False 
        if user == "stats":
            print(f"Wins: {wins} Losses: {losses} Ties: {ties}")
            continue
        if user == "exit":
            return (wins, losses, ties)
        if user == "rock" and computer == "scissors":
            print("You win")
            win = True
            wins += 1
        elif user == "paper" and computer == "rock":
                win = True
                wins += 1
        elif user == "scissor"  or user == "scissors" and computer == "paper":
                win = True
                wins += 1
        elif user == computer:
            print("Its a tie")
            ties += 1
        elif user not in ["rock", "paper", "scissor","scissors","stats","exit"]:
            print("Choose a valid option")
            continue
        else:
            print("You lose")
            lose = True
            losses += 1
        print(f"You chose {user} and the computer chose {computer} and you {'won' if win else 'lost' if lose else 'tied'}!")
def main():
    while True:
        user: str = input("Menu Options: start game?(y/n) or exit? ").lower()
        if user == "yes" or user == "y":
            game = running_game()
            wins, losses, ties = game
            print(f'Wins: {wins} Losses: {losses} Ties: {ties}')
            break
        elif user == "exit":
            break
        else:
            print("Invalid Option")
if __name__ == '__main__':
    main()