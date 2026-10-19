"""Play Rock, Paper, Scissors: python rock_paper_scissors.py"""

import random

CHOICES = ("rock", "paper", "scissors")
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
ALIASES = {"r": "rock", "p": "paper", "s": "scissors",
           "1": "rock", "2": "paper", "3": "scissors"}


def winner(player, computer):
    """Return the round result from the player's perspective."""
    if player == computer:
        return "tie"
    return "win" if BEATS[player] == computer else "loss"


def play():
    print("=== Rock, Paper, Scissors ===")
    print("Play against the computer. Type q to quit anytime.")
    wins = losses = ties = 0

    while True:
        answer = input("\nChoose rock (r/1), paper (p/2), or scissors (s/3): ").strip().lower()
        if answer in ("q", "quit", "exit"):
            break
        player = ALIASES.get(answer, answer)
        if player not in CHOICES:
            print("Please choose rock, paper, scissors, or q.")
            continue

        computer = random.choice(CHOICES)
        print(f"You chose {player}. Computer chose {computer}.")
        result = winner(player, computer)
        if result == "tie":
            ties += 1
            print("It's a tie!")
        elif result == "win":
            wins += 1
            print("You win this round!")
        else:
            losses += 1
            print("Computer wins this round!")
        print(f"Score: You {wins} | Computer {losses} | Ties {ties}")

        while True:
            again = input("Play again? (y/n): ").strip().lower()
            if again in ("y", "yes", "n", "no", "q", "quit", "exit"):
                break
            print("Please type y or n.")
        if again not in ("y", "yes"):
            break

    print(f"\nFinal score: You {wins} | Computer {losses} | Ties {ties}")
    print("Thanks for playing!")


if __name__ == "__main__":
    try:
        play()
    except (KeyboardInterrupt, EOFError):
        print("\nThanks for playing!")
