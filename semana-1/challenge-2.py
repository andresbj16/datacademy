import random
from functools import reduce

user_round_winner = 0
machine_round_winner = 0


def judge(choice_user, choice_machine):
    global user_round_winner
    global machine_round_winner

    if(choice_user == 0 and choice_machine == 0 or choice_user == 1 and choice_machine == 1 or choice_user == 2 and choice_machine == 2):
        print('Tied round')
    elif(choice_user == 0 and choice_machine == 2 or choice_user == 1 and choice_machine == 0 or choice_user == 2 and choice_machine == 1):
        user_round_winner += 1
        print('You win')
    else:
        machine_round_winner += 1
        print('You lose')

    print('Scoreboard: You [' + str(user_round_winner) + '] VS ' + 'Machine [' + str(machine_round_winner) + ']')

    if(user_round_winner == 3):
        print('You are winner')

    if(machine_round_winner == 3):
        print('Machine is winner')

def text_choice(choice):
    rock_papper_scissors = {0: 'Rock', 1: 'Papper', 2: 'Scissors'}
    return rock_papper_scissors[choice]


def rock_papper_scissors(choice_user):
    if(choice_user >= 0 and choice_user <= 2):
        choice_machine = random.choice([0, 1, 2])
        print('\nYou: ' + text_choice(choice_user) + ' - Machine: ' + text_choice(choice_machine))
        judge(choice_user, choice_machine)
    else:
        print('The selection is not valid')


def run():
    print("\nLet's go to play Rock, Papper, Scissors")

    round_number = 1

    while(user_round_winner < 3 and machine_round_winner < 3):
        print('\nRound ' + str(round_number))

        choice = int(input('''
[0] Rock
[1] Papper
[2] Scissors

What do you selection? '''))
        
        rock_papper_scissors(choice)

        round_number +=1


if __name__ == '__main__':
    run()