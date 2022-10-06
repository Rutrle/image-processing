"""Simple exercise about building a number-guessing game"""
import random


def guessing_game(low_num: int = 0, high_num: int = 10) -> bool:
    """Play one round of number guessing game.

    Parameters
    ----------
    low_num : int, optional
        lower number between which the number will be guessed, by default 0
    high_num : int, optional
        higher number between which the the number will be guessed, by default 10

    Returns
    -------
    bool
        True if player win
    """
    my_number = random.randint(low_num, high_num)

    while True:
        user_input = int(input(
            f"I'm thinking about a number between {low_num} and {high_num}, try to guess about which: "))
        if user_input == my_number:
            print(f"Correct, the number I was thinking about was {my_number}")
            return True
        elif low_num>user_input or high_num<low_num:
            print('Your guess is outside of boundaries!')
        elif user_input > my_number:
            print(f"Guess again! try to aim little lower!")
        else:
            print(f"Guess again! try to aim little higher!")


def multiple_games():
    """Play multiple number guessing games.
    """
    print("Welcome to guessing games!")
    wins = 0
    while True:
        if wins > 0:
            print(f'so far you have won {wins}')
        continue_var = input(
            "Press enter to play next game, 'q' to quit and 'a' for advanced settings")

        if continue_var == 'q':
            return
        elif continue_var == 'a':
            low_num = int(input("Please enter a lower boundary between which the number will be guessed: "))
            high_num = int(input("Please enter a higher boundary between which the number will be guessed: "))
            result = guessing_game(low_num,high_num)

        else:
            result = guessing_game()

        if result:
            wins += 1


if __name__ == '__main__':
    multiple_games()
