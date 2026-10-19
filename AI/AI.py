"""The Last Signal: a tiny, choice driven sci-fi adventure.

Run with: python AI/AI.py
"""

import random
import time


def pause():
    input("\nPress Enter to continue...")


def choose(prompt, options):
    """Show numbered options and return the chosen option (starting at 0)."""
    print(f"\n{prompt}")
    for number, option in enumerate(options, start=1):
        print(f"  {number}. {option}")

    while True:
        answer = input("\nYour choice: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return int(answer) - 1
        print(f"Type a number from 1 to {len(options)}.")


def play():
    print("=" * 48)
    print("             THE LAST SIGNAL")
    print("=" * 48)
    print("A tiny sci-fi adventure. Your decisions shape the ending.")
    pause()

    name = input("What's your callsign, pilot? ").strip() or "Rookie"
    courage = 0
    curiosity = 0

    print(f"\nThe year is 2249. Pilot {name}, your ship picks up a signal from a moon")
    print("that disappeared from every star chart a hundred years ago.")
    pause()

    action = choose(
        "The signal repeats three words: 'WE ARE AWAKE.' What do you do?",
        ["Answer the signal", "Scan the moon from a safe distance", "Land immediately"],
    )
    if action == 0:
        curiosity += 2
        print("You send a greeting. Something sends back your own voice... from tomorrow.")
    elif action == 1:
        curiosity += 1
        print("Your scanner finds a warm light under the frozen surface.")
    else:
        courage += 2
        print("You punch through the icy clouds and land beside a glowing doorway.")
    pause()

    print("\nInside a buried station, a small robot rolls toward you carrying a cracked star map.")
    action = choose(
        "The robot asks for help. Its memory is fading.",
        ["Repair it with your ship's spare battery", "Ask what happened first", "Take the map and keep moving"],
    )
    if action == 0:
        courage += 1
        print("The robot lights up. 'Thank you. The people are still here.'")
    elif action == 1:
        curiosity += 2
        print("'We built a doorway between stars,' it says. 'Then something answered.'")
    else:
        print("The robot lets you go, but its dimming eye follows you down the hall.")
    pause()

    print("\nAt the end of the hall, the doorway hums. Beyond it: a sky full of unfamiliar stars.")
    roll = random.randint(1, 6) + courage + curiosity
    action = choose(
        "The signal is coming from the other side. Your ship is waiting behind you.",
        ["Step through the doorway", "Shut it down", "Send a probe through first"],
    )

    print("\n" + "-" * 48)
    if action == 0 and roll >= 6:
        print(f"ENDING: FIRST CONTACT, {name.upper()}!\n")
        print("A thousand distant lights answer as you step into the stars.")
        print("You are the first human to cross the gap—and you are not alone.")
    elif action == 0:
        print("ENDING: LOST IN THE STARS\n")
        print("The doorway closes behind you. Your ship records one final transmission:")
        print("a laugh, a new constellation, and the words 'we made it.'")
    elif action == 1:
        print("ENDING: THE QUIET HERO\n")
        print("The signal stops. The moon goes dark. You fly home with a mystery")
        print("and the uneasy feeling that something out there noticed you.")
    elif roll >= 8:
        print("ENDING: THE SIGNAL KEEPER\n")
        print("The probe finds a living world beyond the doorway—and something there answers.")
        print(f"You stay behind to guide the first reply, {name}, while the probe charts a safe path home.")
    else:
        print("ENDING: A NEW BEGINNING\n")
        print("The probe returns with a tiny glowing seed. It unfolds into a map")
        print("of a thousand worlds—and one is marked with your home planet.")
    print("-" * 48)
    print("\nThanks for playing The Last Signal!")


if __name__ == "__main__":
    try:
        play()
    except (EOFError, KeyboardInterrupt):
        print("\n\nSignal lost. Thanks for playing!")
