import random
import Player_Settings
import Game_outputs
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
    user = input("Choose rock, paper, or scissors: ").lower()
    if user not in ["rock", "paper", "scissors","stats","back"]:
        print("Invalid Option")
        return user_choice()
    return user

def multiplayer_choice() -> str:
    user = input("Player 2 Choose rock, paper, or scissors: ").lower()
    if user not in ["rock", "paper", "scissors","stats","back"]:
        print("Invalid Option")
        return multiplayer_choice()
    return user

def mode_choice() -> str:
    while True:
        mode: str = input("Select game mode: Computer, Multiplayer or Back: ").lower()
        if mode in ["computer","multiplayer","back"]:
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
    
def split_list(actions: list, mode: str, rounds: int) -> tuple:
    if mode == "computer":
        if rounds == 3:
            setup_actions = actions[0:2]
            game_actions = actions[2:]
        elif rounds > 3:
            setup_actions = None
            game_actions = actions[0:]
    elif mode == "multiplayer":
        if rounds == 3:
            setup_actions = actions[0:1]
            game_actions = actions[1:]
        elif rounds > 3:
            setup_actions = None
            game_actions = actions[0:]
    return setup_actions, game_actions

def sets(setup_actions,game_actions) -> str:
            action_output = Game_outputs.Output(setup_actions,game_actions)
            action_output.set_actions(setup_actions,game_actions)
            action_output.set_rounds(game_actions)
            return action_output

def running_game() -> tuple:
    print("Welcome to Rock, Paper, Scissors")
    wins, losses, ties, rounds = 0, 0, 0, 0
    mode, diff = None, None
    player_two_wins, player_two_losses = 0, 0
    action_export: list = []
    actions: list = []
    export_list: list = [wins,losses,ties,rounds,diff,mode,player_two_wins,player_two_losses,action_export]
    mode = mode_choice()
    actions.append(mode)
    if mode == "back":
        export_list[0],export_list[1],export_list[2],export_list[3] = wins,losses,ties,rounds
        export_list[4],export_list[5] = "None","None"
        export_list[6],export_list[7] = player_two_wins,player_two_losses
        export_list[8] = action_export
        print(f"{'-'*25} Main Menu {'-'*25}")
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
        elif user == "back":
            export_list[0],export_list[1],export_list[2],export_list[3] = wins,losses,ties,rounds
            export_list[4],export_list[5] = diff,mode
            export_list[6],export_list[7] = player_two_wins,player_two_losses
            export_list[8] = action_export
            print(f"{'-'*25} Main Menu {'-'*25}")
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
            elif choice == "back":
                export_list[0],export_list[1],export_list[2],export_list[3] = wins,losses,ties,rounds
                export_list[4],export_list[5] = diff,mode
                export_list[6],export_list[7] = player_two_wins,player_two_losses
                export_list [8] = action_export
                print(f"{'-'*25} Main Menu {'-'*25}")
                return export_list
            state: str = conditions(user,choice)
            w,l,t = state
            actions.append(w)
            actions.append(l)
            actions.append(t)
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
        if rounds % 3 == 0:
            setup_actions, game_actions = split_list(actions,mode,rounds)
            actions: list = []
            new_round = sets(setup_actions,game_actions)
            action_export.append(new_round)

def start() -> tuple:
    game_state = Player_Settings.game_state()
    game: tuple = running_game()
    game_state.set_scores(game[0],game[1],game[2],game[3])
    game_state.set_player_two_scores(game[6],game[7])
    game_info: list = game[8]
    if game[5] == "computer":
        game_state.set_mode(game[5])
        game_state.set_diff(game[4])
        print(f"Game Mode: {game_state.get_mode().capitalize()}")
        print(f"Game Difficulty: {game_state.get_diff().capitalize()}")
    elif game[5] == "multiplayer":
        game_state.set_mode(game[5]) 
        game_state.set_diff("None")
        print(f"Game Mode: {game_state.get_mode().capitalize()}")
    print(f"Rounds: {game_state.rounds}, Games Played: {int(game_state.rounds/3)}")
    print(f"Player 1 Stats: Wins: {game_state.wins}, Ties: {game_state.ties}, Losses: {game_state.losses}")
    print(f"Player 2 Stats: Wins: {game_state.player_two_wins}, Losses: {game_state.player_two_losses}")
    print("-"*50)
    return game_info, game_state

def commands(game_info, game_state):
    while True:
        user = input("Do you want to play again? (yes/no/results/help): ").lower()
        if user in ["yes", "y", "start"]:
            game_info, game_state = start()
        elif user in ["no", "n", "exit"]:
            print("Exiting game...")
            exit()
        elif user == "help":
            print("Help: Type 'yes' or 'y' to start the game, 'no' or 'n' to exit, 'results' to view results.")
        elif user == "results":
            count = 1
            clear_screen()
            print(f"Games Played: {int(game_state.rounds/3)}")
            print("-"*50)
            for i in game_info:
                print(f"Game {count}:")
                print(f"Round 1: {i.round_1[:2]} {"win" if i.round_1[2][0] else "lose" if i.round_1[2][1] else "tie"}")
                print(f"Round 2: {i.round_2[:2]} {"win" if i.round_2[2][0] else "lose" if i.round_2[2][1] else "tie"}")
                print(f"Round 3: {i.round_3[:2]} {"win" if i.round_3[2][0] else "lose" if i.round_3[2][1] else "tie"}")
                print("-"*50)
                count += 1
        else:
            print("Invalid input. Please type 'yes' or 'y' to start the game, 'no' or 'n' to exit, or 'results' to view results.")
def main() -> None:
    user = input("Do you want to play Rock, Paper, Scissors? (yes/no/results/help): ").lower()
    if user == "yes" or user == "y" or user == "start":
        game_info, game_state = start()
        commands(game_info, game_state).lower()
    elif user == "no" or user == "n" or user == "exit":
        print(f"Exiting game...")
        exit()
    elif user == "results":
        clear_screen()
        print("No games played yet.")
    elif user == "help":
        clear_screen()
        print("Help: Type 'yes' or 'y' to start the game, 'no' or 'n' to exit, 'results' to view results.")
    else:
        clear_screen()
        print("Invalid input. Please type 'yes' or 'y' to start the game, 'no' or 'n' to exit, or 'results' to view results.")
    main()

if __name__ == '__main__':
    main()