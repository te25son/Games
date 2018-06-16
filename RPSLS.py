"""
ROCK-PAPER-SCISSORS-LIZARD-SPOCK
--------------------------------
A program that simulates a game of Rock-Paper-Scissors-Lizard-Spock
"""

import random
import time
from math import ceil


def name_to_number(name):
    """
    Takes string (name) as input (rock, spock, paper, lizard, scissors)
    and returns integer (0,1,2,3,4)
    """
    # convert the string name to all lowercase letters
    # so that the typed name matches the name in the function
    name = name.lower()
    if name == 'rock':
        return 0
    elif name == 'spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return 'Error: Invalid string (name)'


def number_to_name(number):
    """
    Takes integer (number) as input (0,1,2,3,4)
    and returns string (rock, spock, paper, lizard, scissors)
    """
    if number == 0:
        return 'Rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'Paper'
    elif number == 3:
        return 'Lizard'
    elif number == 4:
        return 'Scissors'
    else:
        return 'Error: Invalid integer (number)'


def rpsls(player_choice):
    print('')
    print('Player chooses %s' % player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    time.sleep(2)
    print('Computer chooses %s' % comp_choice)
    difference = (player_number - comp_number) % 5
    if difference == 0:
        print('Player and Computer tie!')
        score_list[0] = score_list[0] + 1
        print(score_list)
        return score_list
    elif (difference == 1) or (difference == 2):
        print('Player wins!')
        score_list[2] = score_list[2] + 1
        print(score_list)
        return score_list
    else:
        print('Computer wins!')
        score_list[1] = score_list[1] + 1
        print(score_list)
        return score_list


def best_out_of(number):
    """
    Takes the parameter number and returns integers to set up the game.
    """
    if number == 1:
        number_to_win = 1
        game_set_to = 2
        return number_to_win, game_set_to
    else:
        number_to_win = number / 2
        game_set_to = number / 2 + 1
        return ceil(number_to_win), ceil(game_set_to)


def play_again():
    reset_score()
    print('')
    print('Another round? (Y/N)')
    user_reply = input()
    if user_reply.lower() == 'y':
        main()
    else:
        print('Next time then.')
        return exit()


def reset_score():
    score_list[0] = 0
    score_list[1] = 0
    score_list[2] = 0
    return score_list[0] and score_list[1] and score_list[2]


score_list = [0, 0, 0]

rules = """
Rock-Paper-Scissors-Lizard-Spock is a funner, more complicated game of Rock-Paper-Scissors.
Unlike the original game, one option defeats two other options and loses to two options. 

The pattern is as follows:

ROCK - crushes SCISSORS & crushes LIZARD
PAPER - covers ROCK & disproves SPOCK
SCISSORS - cuts PAPER & decapitates LIZARD
LIZARD - eats PAPER & poisons SPOCK
SPOCK - smashes Scissors & vaporizes ROCK

**Remember: you're playing against a randomized opponent, so don't think about it too much.**
"""


def main():
    print('')
    print('''
    Welcome CONTENDER, to a vicious game of ROCK-PAPER-SCISSORS-LIZARD-SPOCK!
    Where the meek survive, the bold thrive, and everyone dies!
    
    Let's get this party started.
    ''')
    print('')
    print('Best games out of how many?')
    user_reply = int(input())
    best_list = best_out_of(user_reply)
    game_set_to = best_list[1]
    number_to_win = best_list[0]
    print('The game is set for best %s out of %s' % (number_to_win, user_reply))
    print('')
    print('Do you need to know the game rules? (Y/N)')
    know_rules = input()
    if know_rules.lower() == 'y':
        print(rules)
    else:
        print('Wonderful! Let\'s begin.')

    while (score_list[1] < game_set_to) and (score_list[2] < game_set_to):
        if (score_list[1] < number_to_win) and (score_list[2] < number_to_win):
            print('')
            print('Enter your decision.')
            user_decision = input()
            rpsls(user_decision)
        elif (score_list[1] == number_to_win) or (score_list[2] == number_to_win):
            if score_list[1] > score_list[2]:
                print('')
                print('Computer won %s out of %s. Computer wins!' % (number_to_win, user_reply))
                play_again()
            else:
                print('')
                print('Player won %s out of %s. Player wins!' % (number_to_win, user_reply))
                play_again()
        else:
            print('Tie game.')


if __name__ == '__main__':
    main()
