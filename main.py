import random

from config import GAME_CHOICES, RULES, scoreboard

from decorator import play_time


def get_user_choice():
    """
    get and validate player input, recursively
    """
    user_input = input('Enter your choice please (r, p, s): ')
    if user_input not in GAME_CHOICES:
        print('Oops!!, wrong choice, try again please...')
        return get_user_choice()
    return user_input


def get_system_choice():
    """
    choice random from GAME_CHOICES
    """
    return random.choice(GAME_CHOICES)


def find_winner(user, system):
    """
    receive user and system choice, sort them and compare with game rules if
    they are not the same.
    :param user:
    :param system:
    :return: winner
    """
    match = {user, system}

    if len(match) == 1:
        return None

    return RULES[tuple(sorted(match))]


def update_scoreboard(result):
    """
    update scoreboard after each hand of the game and show live result
    until now + last hand result
    """
    if result['user'] == 3:
        scoreboard['user'] += 1
        msg = 'You win'
    else:
        scoreboard['system'] += 1
        msg = 'You lose'

    print('#' * 30)
    print('##', f'user: {scoreboard["user"]}'.ljust(24), '##')
    print('##', f'system: {scoreboard["system"]}'.ljust(24), '##')
    print('##', f'last game: {msg}'.ljust(24), '##')
    print('#' * 30)


def play_one_hand():
    """
    main play ground handler
    """
    result = {'user': 0, 'system': 0}

    while result['user'] < 3 and result['system'] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)

        if winner == user_choice:
            msg = 'You win'
            result['user'] += 1
        elif winner == system_choice:
            msg = 'You lose'
            result['system'] += 1
        else:
            msg = 'draw'
        print(f'user: {user_choice}\t system: {system_choice}\t result: {msg}')

    update_scoreboard(result)
    play_again = input('Do you want to play again? (y/n) ')
    if play_again == 'y':
        play_one_hand()


@play_time
def play():
    play_one_hand()


if __name__ == '__main__':
    play()
