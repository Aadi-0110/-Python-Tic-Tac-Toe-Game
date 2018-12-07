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
    if board[int(val)-1] == '*':
        board[int(val)-1] = player
    else:
        print('xoxo Invalid Option xoxo')
        val = input("Enter the index you want to insert (1-9)\n ")
        make_move(val, player)


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


whoisplayer()
set_board()
i = 0
print("Player{0} You are '{0}'\t Player{1} You are '{1}'".format(player1, player2))
print_board()
while 1:

    if i % 2 == 0:
        print('Player"{}\'s" turn'.format(player1))
        val = input("Enter the index you want to insert (1-9)\n Press N to exit\n")
        make_move(val, player1)

    else:
        print('Player"{}\'s" turn'.format(player2))
        val = input("Enter the index you want to insert (1-9)\n Press N to exit\n")
        make_move(val, player2)

    print_board()
    i += 1
    if val == 'N' or i > 9:
        print("\n----- Thanks for playing -----\n")
        exit(0)






