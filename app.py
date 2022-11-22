import random


def display(b):
    print(f'0 | 1 | 2      {b[0]} | {b[1]} | {b[2]}')
    print(f'3 | 4 | 5      {b[3]} | {b[4]} | {b[5]}')
    print(f'6 | 7 | 8      {b[6]} | {b[7]} | {b[8]}')
    print()


def ending(c, b):
    if c >= 9:
        print('ending')
        exit(0)

    i = b[0]
    j = b[1]
    k = b[2]
    if i == j == k != ' ':
        print('ending')
        exit(0)

    i = b[3]
    j = b[4]
    k = b[5]
    if i == j == k != ' ':
        print('ending')
        exit(0)

    i = b[6]
    j = b[7]
    k = b[8]
    if i == j == k != ' ':
        print('ending')
        exit(0)

    i = b[0]
    j = b[3]
    k = b[6]
    if i == j == k != ' ':
        print('ending')
        exit(0)

    i = b[1]
    j = b[4]
    k = b[7]
    if i == j == k != ' ':
        print('ending')
        exit(0)

    i = b[2]
    j = b[5]
    k = b[8]
    if i == j == k != ' ':
        print('ending')
        exit(0)

    i = b[0]
    j = b[4]
    k = b[8]
    if i == j == k != ' ':
        print('ending')
        exit(0)

    i = b[2]
    j = b[4]
    k = b[6]
    if i == j == k != ' ':
        print('ending')
        exit(0)


# instruction
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display(board)

counter = 0
while 1:
    choosing = 1
    while choosing:
        choice = int(input('Input a number 0-8: '))
        if choice >= 0 and choice <= 8:
            if board[choice] == ' ':
                board[choice] = 'O'
                choosing = 0
                counter += 1

    display(board)
    ending(counter, board)

    choosing = 1
    while choosing:
        opponent = random.randrange(0, 8)
        if board[opponent] == ' ':
            board[opponent] = 'X'
            choosing = 0
            counter += 1

    display(board)
    ending(counter, board)
