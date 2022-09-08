# Rebecca Banks - Final project for Python Essentials 1 course from Cisco Networking Academy

from lib2to3.pytree import convert
from pyexpat.errors import XML_ERROR_INCOMPLETE_PE
import random
from itertools import combinations


original_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    for x in range(len(board)):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   "+str(board[x][0])+"   |   " +str(board[x][1])+"   |   "+str(board[x][2])+"   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    free_fields = []
    for x in range(len(board)):
        for y in range(len(board)):
            if(board[x][y] != 'o') and (board[x][y] != 'x'):
                free_fields.append([x, y])
    return free_fields


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    user_input = input("What is your move?: ")
    found = False
    for x in range(len(board)):
        for y in range(len(board)):
            if(int(user_input) == (original_board[x][y])):
                if((board[x][y] != 'o') and (board[x][y] != 'x')):
                    board[x][y] = 'o'
                else:
                    print("Try a new number; that one has been taken")
                    enter_move(board)


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    x_lst = []
    o_lst = []

    for x in range(len(board)):
        for y in range(len(board)):
            if(board[x][y] == 'o'):
                o_lst.append(original_board[x][y])
            elif(board[x][y] == 'x'):
                x_lst.append(original_board[x][y])

    winning_scores = [(1, 4, 7), (3, 5, 7), (2, 5, 8), (3, 6, 9),
                      (1, 5, 9), (1, 2, 3), (4, 5, 6), (7, 8, 9)]

    #using combinations to create all possible combinations of the elements in the x and o lists
    x_lst = list(combinations(x_lst, 3))
    o_lst = list(combinations(o_lst, 3))

    if (sign == 'x'):
        for elem in winning_scores:
            for xelem in x_lst:
                if((xelem[0] in elem) and (xelem[1] in elem) and (xelem[2] in elem)):
                    print("X has won the game!")
                    exit()

    elif (sign == 'o'):
        for elems in winning_scores:
            for oelem in o_lst:
                if((oelem[0] in elems) and (oelem[1] in elems) and (oelem[2] in elems)):
                    print("O has won the game!")
                    exit()


def draw_move(board):
    # The function draws the computer's move and updates the board.
    
    rand_num = random.choice(make_list_of_free_fields(board))
    x = rand_num[0]
    y = rand_num[1]
    board[x][y] = 'x'
    display_board(board)
    print("Computer has made move ...")


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
display_board(board)
for x in range(4):
    victory_for(board, 'x')
    victory_for(board, 'o')
    enter_move(board)
    draw_move(board)
