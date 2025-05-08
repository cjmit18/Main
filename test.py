import random
import Player_Settings
import Game_outputs
import os
def clear_screen() -> None:
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
    centered_game = "{0:^100}\n{1:^100s}"
    centered_options = "{0:^100s}\n{1:^100s}\n{2:^100s}" 
    print(centered_game.format(f"{'-'*10} Player 1 Choices: {'-'*10}",'-- Rock -- Paper -- Scissors'))
    print(centered_options.format(f"{'-'*10} Menu Options {'-'*10}",'-- Stats -- Back -- Help',f"{'-'*30}"))
    user = input().lower()
    if user not in ["rock", "paper", "scissors","stats","back","help"]:
        print("Invalid Option")
        return user_choice()
    return user

def multiplayer_choice() -> str:
    centered_game = "{0:^100}\n{1:^100s}"
    centered_options = "{0:^100s}\n{1:^100s}\n{2:^100s}" 
    print(centered_game.format(f"{'-'*10} Player 2 Choices: {'-'*10}","-- Rock -- Paper -- Scissors"))
    print(centered_options.format(f"{'-'*10} Menu Options {'-'*10}","-- Stats -- Back -- Help",f"{'-'*30}"))
    user = input().lower()
    if user not in ["rock", "paper", "scissors","stats","back","help"]:
        print("Invalid Option")
        return multiplayer_choice()
    return user

def main_menu() -> tuple:
    diff = None
    while True:
        mode: str = input("Main Menu: Computer, Multiplayer, Difficulty or Back: ").lower()
        if mode in ["computer","multiplayer", "difficulty" ,"back"]:
            if mode == "computer" and diff != None:
                return mode,diff
            elif mode in "computer" and diff == None:
                print("Please select a difficulty")
            elif mode == "multiplayer":
                return mode,diff
            elif mode == "back":
                return mode,diff
            elif mode == "difficulty":
                diff = difficulty()
                continue
        else:
            print("Please choose a valid mode and difficulty.")

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
    
def split_list(actions: list, mode: str, rounds: int,) -> tuple:
    game_actions = []
    setup_actions = []
    for i in actions:
        if i in ["computer","multiplayer","easy","medium","hard","back","stats","help",None]:
            setup_actions.append(i)
        else:
            game_actions.append(i)
    return setup_actions, game_actions

def sets(setup_actions,game_actions) -> str:
            action_output = Game_outputs.Output(setup_actions,game_actions)
            action_output.set_actions(setup_actions,game_actions)
            action_output.set_rounds(game_actions)
            return action_output

def running_game() -> tuple:
    wins, losses, ties, rounds, = 0, 0, 0, 0
    game_wins,game_losses,game_ties,games = 0,0,0,0
    game_wins_two, game_loss_two = 0, 0
    player_two_loss = 0
    player_two_wins = 0
    mode, diff = None,None,
    action_export: list = []
    actions: list = []
    export_list: list = [game_wins,game_losses,game_ties,rounds,diff,mode,game_wins_two,game_loss_two,action_export]
    check: bool = True
    print("Welcome to Rock, Paper, Scissors")
    mode, diff = main_menu()
    actions.append(mode)
    actions.append(diff)
    if mode == "back":
        export_list[0],export_list[1],export_list[2],export_list[3] = game_wins,game_ties,game_losses,rounds
        export_list[4],export_list[5] = "None","None"
        export_list[6],export_list[7] = game_wins_two,game_loss_two
        export_list[8] = action_export
        return export_list
    while True:
        win,lose,tie = False,False,False
        user = user_choice()
        actions.append(user)
        if user == "stats" and rounds <= 2:
            print(f"wins: {wins}, Ties: {ties}, Losses: {losses} rounds: {rounds}")
            continue
        if user == "stats" and rounds >= 2:
            print(f"Game Wins: {game_wins}, Game Losses: {game_losses}, Tied Games: {game_ties} Total Games: {games}") 
            continue
        elif user == "back":
            export_list[0],export_list[1],export_list[2],export_list[3] = game_wins,game_ties,game_losses,rounds
            export_list[4],export_list[5] = diff,mode
            export_list[6],export_list[7] = game_wins_two,game_loss_two
            export_list[8] = action_export
            return export_list
        elif user == "help":
            print("Help: Type 'rock', 'paper', or 'scissors' to play, 'stats' to view your stats, 'back' to return to the main menu.")
            continue
        if mode == "computer":
            choice: str = computer_choice(diff,user)
            state: str = conditions(user,choice)
            actions.append(choice)
            actions.append(state)
            if state[0]:
                wins += 1
                player_two_loss += 1
            elif state[1]:
                losses += 1
                player_two_wins += 1
            elif state[2]:
                ties += 1
            rounds += 1
        elif mode == "multiplayer":
            while True:
                if check == True:
                    clear_screen()
                    choice = multiplayer_choice()
                elif check == False:
                    choice = multiplayer_choice()
                    check: bool = True
                actions.append(choice)
                if choice == "stats":
                    print(f"wins: {game_wins_two}, Ties: {ties}, Losses: {game_loss_two} rounds: {rounds}")
                    check = False
                    continue
                elif choice == "back":
                    export_list[0],export_list[1],export_list[2],export_list[3] = game_wins,game_ties,game_losses,rounds
                    export_list[4],export_list[5] = diff,mode
                    export_list[6],export_list[7] = game_wins_two,game_loss_two
                    export_list [8] = action_export
                    return export_list
                elif choice == "help":
                    print("Help: Type 'rock', 'paper', or 'scissors' to play, 'stats' to view your stats, 'back' to return to the main menu.")
                    check = False
                    continue
                state: str = conditions(user,choice)
                actions.append(state)
                if state[0]:
                    wins += 1
                    player_two_loss += 1
                elif state[1]:
                    losses += 1
                    player_two_wins += 1
                elif state[2]:
                    ties += 1
                rounds += 1
                break
        if rounds % 3 == 0 or 2 in [wins,losses,ties]:
            if wins >= 2:
                game_wins += 1
                game_loss_two += 1
            elif losses >= 2:
                game_losses += 1
                game_wins_two += 1
            else:
                game_ties += 1
            games += 1
            setup_actions, game_actions = split_list(actions,mode,rounds)
            new_round = sets(setup_actions,game_actions)
            action_export.append(new_round)
            actions: list = []
            wins,losses,ties = 0,0,0

def start_game() -> tuple:
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
    print(f"Games Played: {game_state.rounds//3} Rounds: {game_state.rounds}")
    print(f"Player 1 Stats: Wins: {game_state.wins}, Ties: {game_state.ties}, Losses: {game_state.losses}")
    print(f"Player 2 Stats: Wins: {game_state.player_two_wins}, Losses: {game_state.player_two_losses}")
    print("-"*50)
    return game_info, game_state

def commands(game_info, game_state) -> None:    
    while True:
        user = input("Do you want to play again? (yes/no/results/help): ").lower()
        if user in ["yes", "y", "start"]:
            game_info, game_state = start_game()
        elif user in ["no", "n", "exit"]:
            print("Exiting game...")
            exit()
        elif user == "help":
            print("Help: Type 'yes' or 'y' to start the game, 'no' or 'n' to exit, 'results' to view results.")
        elif user == "results":
            try:
                count = 1
                print(f"Games Played: {int(game_state.rounds/3)}")
                print("-"*50)
                for i in game_info:
                    print(f"Game {count}:")
                    print(f"Round 1: {i.round_1[:2]} {'win' if i.round_1[2][0] else 'lose' if i.round_1[2][1] else 'tie'}")
                    print(f"Round 2: {i.round_2[:2]} {'win' if i.round_2[2][0] else 'lose' if i.round_2[2][1] else 'tie'}")
                    print(f"Round 3: {i.round_3[:2]} {'win'if i.round_3[2][0] else 'lose' if i.round_3[2][1] else 'tie'}")
                    print("-"*50)
                    count += 1
            except IndexError:
                print("Round not played.")
        else:
            print("Invalid input. Please type 'yes' or 'y' to start the game, 'no' or 'n' to exit, or 'results' to view results.")

def main() -> None:
    user = input("Do you want to play Rock, Paper, Scissors? (Yes/No/Help): ").lower()
    if user in ["yes", "y", "start"]:
        game_info, game_state = start_game()
        commands(game_info, game_state).lower()
    elif user in ["no","n","exit"]:
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