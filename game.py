human_turn = 'paper'
computer_turn = 'scissors'

if human_turn == 'rock' and computer_turn == 'scissors':
    print('human wins!')
elif human_turn == 'paper' and computer_turn == 'rock':
    print('human wins!')
elif human_turn == 'scissors' and computer_turn == 'rock':
    print('human wins!')
elif human_turn == computer_turn:
    print('Draw!')
else:
    print('human wins!')
