from random import randint

board = []
player1 = ''
player2 = ''
play1 = []
play2 = []


def whoisplayer():
    global player1,player2
    i = randint(0, 2)
    if i == 0:
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'


def set_board():
    global board
    board = ['*']*9


def make_move(val, player):
    if board[int(val)] == '*':
        board[int(val)] = player
    else:
        print('xoxo Invalid Option xoxo')


def print_board():
    global board
    print(' {0} | {1} | {2}\n-----------\n {3} | {4} | {5} \n-----------\n {6} | {7} | {8}'.format(board[0],
                                                                                                   board[1],
                                                                                                   board[2],
                                                                                                   board[3],
                                                                                                   board[4],
                                                                                                   board[5],
                                                                                                   board[6],
                                                                                                   board[7],
                                                                                                   board[8],
                                                                                                   ))

i = 0
while 1:
    whoisplayer()
    set_board()
    print("PlayerX You are '{0}'\t PlayerO You are '{1}'".format(player1,player2))

    if i % 2 == 0:
        print('Player"{}" turn'.format(player1))
        val = input("Enter the index you want to insert\n Press N to exit\n")

    else:
        print('Player"{}" turn'.format(player2))
        val = input("Enter the index you want to insert\n Press N to exit\n")

    if val == 'N':
        exit(0)






