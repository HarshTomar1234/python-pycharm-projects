import sys
import random
from enum import Enum


def rps(name="Player 1"):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSOR = 3

        player_choice = input(
            f"\n{name}, please enter... \n1 for Rock,\n2 for Paper,\n3 for Scissor\n\n")

        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1,2, or 3.")
            return play_rps()

        player = int(player_choice)

        computer_choice = random.choice("123")
        computer = int(computer_choice)

        print(
            f"\n{name}, you chose  {str(RPS(player)).replace('RPS.', '').title()}.")
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
        )

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, you Won!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, you Won!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, you Won!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                computer_wins += 1
                return f"Sorry {name} , you Lose! 😞"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: { game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nComputer wins: {computer_wins}")

        print(f"\nPlay again, {name}?")

        while True:
            Prompting_user = input(" \nY for Yes or \nQ to Quit  \n\n")
            if Prompting_user not in ["y", "q"]:
                continue
            else:
                break

        if Prompting_user.lower() == "y":
            play_rps()
        else:
            print("🎉🎉🎉🎉 Good Bye! 🎉🎉🎉🎉")
            print("Thankyou for Playing the game.")
            sys.exit(f"\nBye {name}! 👋")

    return play_rps


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
