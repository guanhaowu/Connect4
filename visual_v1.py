################################
##########  CREDITS ############
#   TEAM: Connect 4            #
#   Guan Hao Wu | 0976154      #
#   Gizem Sazak | 0965662      #
#   Bilal Azrioual | 0966189   #
################################
################################

import pygame
import sys

# Initialize program
pygame.init()

# Window Title
title = 'Connect 4'
iconTitle = ''
pygame.display.set_caption(title, iconTitle)

# DEFINES
COLUMN_COUNTER = 7
ROW_COUNTER = 6

SQUARE_size = 100
CIRCLE_size = 45
width = COLUMN_COUNTER * SQUARE_size
height = (ROW_COUNTER + 1) * SQUARE_size
screenSize = [width, height]
screen = pygame.display.set_mode(screenSize)


# kleuren
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


def update_screen():
    pygame.display.update()


#  layout Black BG & Blue rect
def bord():
    screen.fill(BLACK)
    screen.fill(BLUE, rect=[0, 100, width, height])
    y = 50
    i = 0
    while i < ROW_COUNTER:
        x = 50
        y += 100
        while x <= 650:
            pygame.draw.circle(screen, BLACK, (x, y), CIRCLE_size)
            x += 100
        i += 1


def coin_top_loc(kleur, mx):
    col = 0
    start = 0
    end = 100
    while col < COLUMN_COUNTER:
        if mx in range(start+(col*100), end+(col-1*100)):
            pygame.draw.circle(screen, kleur, ((col*end)+50, 50), CIRCLE_size)
        col += 1


def turn(player, mx):
    if player == 1:
        coin_top_loc(YELLOW, mx)
        return
    if player == 2:
        coin_top_loc(RED, mx)
        return


# row  = height; col = width;
def tile_color(num, row, col):
    if num == 0:
        pygame.draw.circle(screen, BLACK,  ((col*100)+50, (600-(row * 100))+50), CIRCLE_size)
    if num == 1:
        pygame.draw.circle(screen, YELLOW, ((col*100)+50, (600-(row * 100))+50), CIRCLE_size)
    if num == 2:
        pygame.draw.circle(screen, RED, ((col*100)+50, (600-(row * 100))+50), CIRCLE_size)
    return


# bovenste zwarte balk
def zwartbalk():
    screen.fill(BLACK, rect=[0, 0, 700, 100])


def get_mouse():
    # muis
    mx, my = pygame.mouse.get_pos()
    return mx, my


def exit_game():
    # Exits screen window is loop stopped
    pygame.display.quit()
    sys.exit()


# Player display MSG
def display_msg(player, text):
    if player == 1:
        kleur = YELLOW
    if player == 2:
        kleur = RED

    t = pygame.font.Font(None, 50) # fontType, FontSize
    text1 = t.render(text, True, kleur, [0, 0, 0]) # Text, Antiallias, text_color, bg_color
    display_text = screen.blit(text1, (250, 30))
    return display_text


# Event listening...
def get_event(gameover):
    # Listening to event
    for event in pygame.event.get():  # User executed something
        if event.type == pygame.QUIT and gameover == False:  # If clicked on Close
            gameover = True
            exit_game()
            return gameover
        elif event.type == pygame.QUIT and gameover == True:
            running = False
            exit_game()
            return running
        # if event.type == pygame.MOUSEBUTTONDOWN:
