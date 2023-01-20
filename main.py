import json
import random
import pygame
import sys
from pygame.locals import *

MESSAGE_CLEAR_EVENT = USEREVENT + 1

images = []
hangman_status = 0

letters_ui = []
letter_use = []
letter_discover = []
word = ""
shown_word = ""

game_message = ""
last_message_time = 0


state = "MainMenu"


class Button:
    def __init__(self, sprite, size, rect, command):
        self.rect = pygame.Rect(rect, size)
        self.image = pygame.image.load(sprite)
        self.image_size = pygame.transform.scale(self.image, size)
        self.command = command

    def render(self, screen):
        screen.blit(self.image_size, self.rect)

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.command()


def show_command_message(message, t):
    global game_message
    game_message = message
    pygame.time.set_timer(MESSAGE_CLEAR_EVENT, t * 1000)


def write_word():
    global shown_word
    shown_word = ""
    for i in word:
        if i in letter_discover:
            shown_word += i
        else:
            shown_word += "_ "


def number_to_letter(n):
    return chr(n + 64).lower()


def show_letters():
    i = 0
    x_offset = 0
    y_offset = 0
    for l in letters_ui:
        i += 1
        if i - 1 == len(letters_ui)/2:
            y_offset += 50
            x_offset = 0
        l_big = pygame.transform.scale(l, (40, 40))
        if number_to_letter(i) not in letter_use:
            display_surface.blit(l_big, (25 + x_offset, 500 + y_offset))
        x_offset += 50


def new_game():
    global word, letter_discover, letter_use, letters_ui, shown_word, hangman_status
    hangman_status = 0
    letters_ui = []
    letter_use = []
    letter_discover = []
    word = ""
    shown_word = ""
    for i in range(26):
        letter_ui = pygame.image.load(f"keys/pkl_lite_keys_0_one_letter_{i+1}.png")
        letters_ui.append(letter_ui)
    for i in range(7):
        image = pygame.image.load(f"images/hangman{i}.png")
        images.append(image)
    with open("words.json") as jsonFile:
        data = json.load(jsonFile)
        word = random.choice(data["easy"])
    write_word()


pygame.init()

grey = (155, 155, 155)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


X = 1080
Y = 720

display_surface = pygame.display.set_mode((X, Y))

pygame.display.set_caption('Pendu')

font = pygame.font.Font('freesansbold.ttf', 32)
game_message_font = pygame.font.Font('freesansbold.ttf', 20)

# UI for WORD #
word_UI = font.render(shown_word, True, black)
word_Rect = word_UI.get_rect()
word_Rect.center = ((X // 2) - ((len(word) * 1.5) * 9) - 250, 400)
# ___________ #

# UI for GameMessage #
game_Message_tittle = font.render("Advert:", True, white)
game_message_UI = game_message_font.render(game_message, True, red)
game_message_rect = (750, 58)
# __________________ #

# UI for MainMenu #
game_name_UI = pygame.font.Font('freesansbold.ttf', 50).render("Pendu", True, white)
score_board_UI = pygame.font.Font('freesansbold.ttf', 60).render("Scoreboard", True, black)
# __________________ #


def change_state(s):
    global state
    state = s
    if state == "Play":
        new_game()


main_menu_button = Button(f"buttons/Exit Button.png", (200, 75), (790, 600), lambda: change_state("MainMenu"))
play_button = Button(f"buttons/Play Button.png", (200, 75), (790, 200), lambda: change_state("Play"))
quit_button = Button(f"buttons/Quit Button.png", (200, 75), (790, 600), lambda: exit())

while True:
    # UI Update#

    if state == "MainMenu":
        display_surface.fill(grey)
        pygame.draw.rect(display_surface, (96, 96, 96), [700, 0, X, Y])
        pygame.draw.rect(display_surface, black, [700, 0, 5, Y])
        display_surface.blit(game_name_UI, (810, 20))
        display_surface.blit(score_board_UI, (155, 20))
        play_button.render(display_surface)
        quit_button.render(display_surface)

    if state == "Play":
        display_surface.fill(white)
        pygame.draw.rect(display_surface, (96, 96, 96), [700, 0, X, Y])
        pygame.draw.rect(display_surface, black, [700, 0, 5, Y])
        pygame.draw.rect(display_surface, white, [720, 50, 350, 35])

        display_surface.blit(images[hangman_status], ((X // 2) - 260, 100))

        game_message_UI = game_message_font.render(game_message, True, red)

        display_surface.blit(game_Message_tittle, (730, 10))
        display_surface.blit(game_message_UI, game_message_rect)

        word_UI = font.render(shown_word, True, black)
        display_surface.blit(word_UI, word_Rect)

        main_menu_button.render(display_surface)
        show_letters()

    if state == "Ending":
        pass
    # ___________ #

    for event in pygame.event.get():

        if event.type == MESSAGE_CLEAR_EVENT:
            game_message = ""

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if state == "Play":
                main_menu_button.get_event(event)
            elif state == "MainMenu":
                play_button.get_event(event)
                quit_button.get_event(event)

        if event.type == KEYDOWN:
            try:
                if chr(event.key) in word:
                    if chr(event.key) in letter_discover:
                        show_command_message("character already discover !!!", 2)
                    else:
                        letter_discover.append(chr(event.key))
                        write_word()

                elif hangman_status <= 4 and chr(event.key) not in letter_use:
                    hangman_status += 1

                elif hangman_status == 5 and chr(event.key) not in letter_use:
                    hangman_status += 1
                    show_command_message("Loose !!!", 2)
                else:
                    print("please stop")
                letter_use += chr(event.key)
            except:
                print("Imput Error")

    won = True

    for letter in word:
        if letter not in letter_discover:
            won = False

    pygame.display.update()
