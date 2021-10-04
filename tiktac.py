
import pygame
import sys
import numpy as num

pygame.init()  # initializing the pygame.

# Displaying a board
# WIDTH and HEIGHT are constant.
# Constant start here.
WIDTH = 600
HEIGHT = WIDTH
BOARDCOLOR = (79, 121, 66)
BOARD_ROW = 3
BOARD_COL = 3
LINE_WIDTH = 15
SQ_SIZE = WIDTH//BOARD_COL
WHITE = (239, 231, 200)
CIRCLCERADIUS = SQ_SIZE//3
CIRCLEWIDTH = 15
COLOR = (0, 139, 139)
CROSSWIDTH = 25
SPACE = SQ_SIZE//4
LINE_COLOR = (2, 48, 32)
# Constant end here.

# We are going to make(135, 206, 235) the GUI first.
scr = pygame.display.set_mode((WIDTH, HEIGHT))  # scr stands for screen
scr.fill(BOARDCOLOR)
pygame.display.set_caption('TikTacToe demo')

board = num.zeros((BOARD_ROW, BOARD_COL))


def draw_lines():
    # Horizontial Lines
    pygame.draw.line(scr, LINE_COLOR, (0, SQ_SIZE),
                     (HEIGHT, SQ_SIZE), LINE_WIDTH)
    pygame.draw.line(scr, LINE_COLOR, (0, 2*SQ_SIZE),
                     (HEIGHT, 2*SQ_SIZE), LINE_WIDTH)
    # Vertical Lines
    pygame.draw.line(scr, LINE_COLOR, (SQ_SIZE, 0),
                     (SQ_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(scr, LINE_COLOR, (2*SQ_SIZE, 0),
                     (2*SQ_SIZE, HEIGHT), LINE_WIDTH)

# Drawing the O and X.


def drawfig():
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            if board[row][col] == 1:
                pygame.draw.circle(scr, WHITE, (int(
                    col * SQ_SIZE+SQ_SIZE//2), int(row*SQ_SIZE+SQ_SIZE//2)), CIRCLCERADIUS, CIRCLEWIDTH)

            elif board[row][col] == 2:
                pygame.draw.line(
                    scr, WHITE, (col*SQ_SIZE+SPACE, row*SQ_SIZE+SQ_SIZE-SPACE), (col*SQ_SIZE+SQ_SIZE-SPACE, row*SQ_SIZE+SPACE), CROSSWIDTH)
                pygame.draw.line(
                    scr, WHITE, (col*SQ_SIZE+SPACE, row*SQ_SIZE+SPACE), (col*SQ_SIZE+SQ_SIZE-SPACE, row*SQ_SIZE+SQ_SIZE-SPACE), CROSSWIDTH)

# It will mark the square when user clicks.


def mark_sq(row, col, user):
    board[row][col] = user

# It will check the square is available or not.


def available_sq(row, col):
    return board[row][col] == 0

# It will check the board is full or not.


def isboardfull():
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            # It will check the board row and columns are available or not.
            if board[row][col] == 0:
                return False
    return True

# It will check the win of and draw the line over wining player mark.


def checkwin(user):
    for col in range(BOARD_COL):
        if board[0][col] == user and board[1][col] == user and board[2][col] == user:
            drawverticlewin(col, user)
            return True

    for row in range(BOARD_ROW):
        if board[row][0] == user and board[row][1] == user and board[row][2] == user:
            drawhorizontialwin(row, user)
            return True

    if board[2][0] == user and board[1][1] == user and board[0][2] == user:
        drawasecdiagonal(user)
        return True

    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        drawdescdiagonal(user)
        return True

    return False

# It create verticle line over the wining player mark.


def drawverticlewin(col, user):
    posX = col*SQ_SIZE+SQ_SIZE//2

    if user == 1:
        color = COLOR
    if user == 2:
        color = COLOR

    pygame.draw.line(scr, color, (posX, 15), (posX, HEIGHT-15), 15)

# It will create Horizontial line over the wining player.


def drawhorizontialwin(row, user):
    posY = row*SQ_SIZE+SQ_SIZE//2

    if user == 1:
        color = COLOR
    elif user == 2:
        color = COLOR

    pygame.draw.line(scr, color, (15, posY), (WIDTH-15, posY), 15)

# It will create ascending diagonal line over the wining player.


def drawasecdiagonal(user):
    if user == 1:
        color = COLOR
    elif user == 2:
        color = COLOR

    pygame.draw.line(scr, color, (15, HEIGHT-15), (WIDTH-15, 15), 15)

# It will create Descending diagonal line over the wining player.


def drawdescdiagonal(user):
    if user == 1:
        color = COLOR
    elif user == 2:
        color = COLOR

    pygame.draw.line(scr, color, (15, 15), (WIDTH-15, HEIGHT-15), 15)

# It will restart the game.


def restart():
    # It will fill the board background with BOARDCOLOR Constant.
    scr.fill(BOARDCOLOR)
    draw_lines()  # We are calling a draw_lines function to draw new lines.
    user = 1
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            board[row][col] = 0


draw_lines()
# Creating a Variable.
user = 1
gameover = False

# main loop.
# It will run If it is True not false.
while True:
    # We are crating a event where we make the TikTacToe window to display.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # This will make the exit button in window.
            sys.exit()  # this will tell the code to exit the window.

        # We are going to instruct the code to chect the mouse click in the board window.
        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
            mouseX = event.pos[0]  # X-coordinates
            mouseY = event.pos[1]  # Y-coordinates

            clickrow = int(mouseY // SQ_SIZE)
            clickcol = int(mouseX // SQ_SIZE)

            # This will check that square is available or not when user click the square.
            if available_sq(clickrow, clickcol):
                if user == 1:
                    mark_sq(clickrow, clickcol, 1)
                    if checkwin(user):
                        gameover = True
                    user = 2
                elif user == 2:
                    mark_sq(clickrow, clickcol, 2)
                    if checkwin(user):
                        gameover = True
                    user = 1
                drawfig()

        # This function will restart the game when user click 'r' button.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    #  This function will display the update the window constantly.
    pygame.display.update()
