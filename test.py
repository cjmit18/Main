import random
import Player_Settings
import Game_outputs
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else "clear")
def computer_choice(diff,user,) -> str:
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
    user = input("Choose rock, paper, or scissors: ").lower()
    if user not in ["rock", "paper", "scissors","stats","exit"]:
        print("Invalid Option")
        return user_choice()
    return user

def multiplayer_choice() -> str:
    user = input("Player 2 Choose rock, paper, or scissors: ").lower()
    if user not in ["rock", "paper", "scissors","stats","exit"]:
        print("Invalid Option")
        return multiplayer_choice()
    return user

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
        print("Invalid Difficulty")
        continue
     
def conditions(user,choice) -> tuple:
    win,lose,tie, = False,False,False,
    while True:
        if user == "rock" and choice == "scissors" or user == "paper" and choice == "rock" or user == "scissors" and choice == "paper":
            win = True
            print(f" You chose {user} and player 2 chose {choice} and won!")
        elif user == choice:
            tie = True
            print(f"You both chose {user} and Tied!")
        else:
            lose = True
            print(f"You chose {user} and lost! your opponent chose {choice}")
        return win,lose,tie
    
def running_game() -> tuple:
    wins, losses, ties, rounds = 0, 0, 0, 0
    mode, diff = None, None
    player_two_wins, player_two_losses = 0, 0
    actions: list = []
    export_list: list = [wins,losses,ties,rounds,diff,mode,player_two_wins,player_two_losses,actions]
    mode = mode_choice()
    actions.append(mode)
    if mode == "exit":
        export_list[0],export_list[1],export_list[2],export_list[3] = wins,losses,ties,rounds
        export_list[4],export_list[5] = "None","None"
        export_list[6],export_list[7] = player_two_wins,player_two_losses
        export_list[8] = actions
        print("Exiting Game")
        return export_list
    elif mode == "computer":
        diff = difficulty()
        actions.append(diff)
    while True:
        win,lose,tie = False,False,False
        user = user_choice()
        actions.append(user)
        if user == "stats":
            print(f"wins: {wins}, Ties: {ties}, Losses: {losses} rounds: {rounds}")
            continue 
        elif user == "exit":
            export_list[0],export_list[1],export_list[2],export_list[3] = wins,losses,ties,rounds
            export_list[4],export_list[5] = diff,mode
            export_list[6],export_list[7] = player_two_wins,player_two_losses
            export_list[8] = actions
            print("Exiting Game")
            return export_list
        if mode == "computer":
            choice: str = computer_choice(diff,user)
            state: str = conditions(user,choice)
            actions.append(choice)
            actions.append(state)
            if state[0]:
                wins += 1
                player_two_losses += 1
            elif state[1]:
                losses += 1
                player_two_wins += 1
            elif state[2]:
                ties += 1
            rounds += 1
        elif mode == "multiplayer":
            clear_screen()
            choice = multiplayer_choice()
            actions.append(choice)
            if choice == "stats":
                print(f"wins: {player_two_wins}, Ties: {ties}, Losses: {player_two_losses} rounds: {rounds}")
                continue
            elif choice == "exit":
                export_list[0],export_list[1],export_list[2],export_list[3] = wins,losses,ties,rounds
                export_list[4],export_list[5] = diff,mode
                export_list[6],export_list[7] = player_two_wins,player_two_losses
                export_list [8] = actions
                print("Exiting Game")
                return export_list
            state: str = conditions(user,choice)
            actions.append(state)
            if state[0]:
                wins += 1
                player_two_losses += 1
            elif state[1]:
                losses += 1
                player_two_wins += 1
            elif state[2]:
                ties += 1
            rounds += 1
        if rounds == 3:
          #Here
          set_actions = Game_outputs.Output().set_actions(actions)
def main():
    while True:
        user: str = input("Menu Options: Start Game? (y/n) or Exit? ").lower()
        if user == "yes" or user == "y":
            game_state = Player_Settings.game_state()
            output = Game_outputs.Output()
            game: tuple = running_game()
            game_state.set_scores(game[0],game[1],game[2],game[3])
            output.set_actions(game[8])
            print(f"Game Actions: {output.get_actions()}")
            if game[5] == "computer":
                game_state.set_mode(game[5])
                game_state.set_diff(game[4])
                print(f"Game Mode: {game_state.get_mode().capitalize()}")
                print(f"Game Difficulty: {game_state.get_diff().capitalize()}")
            elif game[5] == "multiplayer":
                game_state.set_mode(game[5])
                game_state.set_diff("None")
                game_state.set_player_two_scores(game[6],game[7])
                print(f"Game Mode: {game_state.get_mode().capitalize()}")
            print(f"Player 1 Stats: Wins: {game_state.wins}, Ties: {game_state.ties}, Losses: {game_state.losses} rounds: {game_state.rounds}")
            print(f"Player 2 Wins: {game_state.player_two_wins}, Player 2 Losses: {game_state.player_two_losses} rounds: {game_state.rounds}")
            break
        elif user == "exit":
            print("Exiting Game")
            break
        else:
            print("Invalid Option")
            continue
if __name__ == '__main__':
    main()