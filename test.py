import random
#Randomly chooses rock, paper, or scissors for the computer to play against the user
#Returns the computer's choice as a string
def computer_choice() -> str:
    choice = random.randint(1,3)
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"
#Prompts the user to choose rock, paper, or scissors
#Returns the user's choice as a string
def user_choice() -> str: 
      return input("Rock, Paper, or Scissors? ").lower()
#Plays a game of rock, paper, scissors
#Prints the result of the game
#Returns a tuple containing the number of wins, losses, and ties for the user
def running_game() -> tuple:
    #Initializes the number of wins, losses, ties, and rounds to 0
    wins: int = 0
    losses: int = 0
    ties: int = 0
    round: int = 0
    #Initializes the variables that determine the result of the game to None
    win: bool = None
    lose: bool = None
    tie: bool = None
    #While loop that continues to play the game until the user types "exit"
    while True:
        user: str = user_choice()
        computer: str = computer_choice()
        win, lose, tie = None, None, None 
        #If statements that determine the result of the game
        if user == "stats":
            print(f"Wins: {wins} Losses: {losses} Ties: {ties}")
            continue
        if user == "exit":
            return (wins, losses, ties)
        if user == "rock" and computer == "scissors":
            win = True
            wins += 1
        elif user == "paper" and computer == "rock":
                win = True
                wins += 1
        elif user == "scissors" and computer == "paper":
                win = True
                wins += 1
        elif user == computer:
            ties += 1
        elif user not in ["rock", "paper","scissors"]:
            print("Choose a valid option")
            continue
        else:
            lose = True
            losses += 1
        round += 1
        print(f"You chose {user} and the computer chose {computer} and you {'won' if win else 'lost' if lose else 'tied'}!")
        print(f"Round: {round}")
        #Prints the result of the game
#Main function that runs the game
#Prompts the user to start the game or exit
def main():
    while True:
        user: str = input("Menu Options: Start Game? (y/n) or Exit? ").lower()
        if user == "yes" or user == "y":
            game = running_game()
            wins, losses, ties = game
            print(f'Wins: {wins} Losses: {losses} Ties: {ties}')
            break
        elif user == "exit":
            break
        else:
            print("Invalid Option")
            continue
if __name__ == '__main__':
    main()