
import pygame
import sys
import numpy as num

pygame.init()  # initializing the pygame.

# Displaying a board
# WIDTH and HEIGHT are constant.
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


def mark_sq(row, col, user):
    board[row][col] = user


def available_sq(row, col):
    return board[row][col] == 0


def isboardfull():
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            if board[row][col] == 0:
                return False
    return True


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


def drawverticlewin(col, user):
    posX = col*SQ_SIZE+SQ_SIZE//2

    if user == 1:
        color = COLOR
    if user == 2:
        color = COLOR

    pygame.draw.line(scr, color, (posX, 15), (posX, HEIGHT-15), 15)


def drawhorizontialwin(row, user):
    posY = row*SQ_SIZE+SQ_SIZE//2

    if user == 1:
        color = COLOR
    elif user == 2:
        color = COLOR

    pygame.draw.line(scr, color, (15, posY), (WIDTH-15, posY), 15)


def drawasecdiagonal(user):
    if user == 1:
        color = COLOR
    elif user == 2:
        color = COLOR

    pygame.draw.line(scr, color, (15, HEIGHT-15), (WIDTH-15, 15), 15)


def drawdescdiagonal(user):
    if user == 1:
        color = COLOR
    elif user == 2:
        color = COLOR

    pygame.draw.line(scr, color, (15, 15), (WIDTH-15, HEIGHT-15), 15)


def restart():
    scr.fill(BOARDCOLOR)
    draw_lines()
    user = 1
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            board[row][col] = 0


draw_lines()

user = 1
gameover = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
            mouseX = event.pos[0]  # X-coordinates
            mouseY = event.pos[1]  # Y-coordinates

            clickrow = int(mouseY // SQ_SIZE)
            clickcol = int(mouseX // SQ_SIZE)

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    pygame.display.update()
