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

easy_check = True
normal_check = False
hard_check = False

easy_sprite = f"buttons/CheckBox10.png"
normal_sprite = f"buttons/CheckBox06.png"
hard_sprite = f"buttons/CheckBox06.png"

difficulty = "Easy"

score = 0

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
    global word, letter_discover, letter_use, letters_ui, shown_word, hangman_status, score
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
        word = random.choice(data[difficulty])
    write_word()


def change_state(s):
    global state, score
    button_sound = pygame.mixer.Sound("Sounds/button_sound.mp3")
    if state != "Win":
        score = 0
    state = s
    button_sound.play()
    new_game()


def change_difficulty(dif):
    global hard_check, normal_check, easy_check, hard_sprite, normal_sprite, easy_sprite, difficulty
    uncheck_sprite = f"buttons/CheckBox06.png"
    check_sprite = f"buttons/CheckBox10.png"
    if dif == "Hard":
        difficulty = dif
        hard_check = True
        normal_check = False
        easy_check = False
    if dif == "Normal":
        difficulty = dif
        hard_check = False
        normal_check = True
        easy_check = False
    if dif == "Easy":
        difficulty = dif
        hard_check = False
        normal_check = False
        easy_check = True
    if hard_check:
        hard_sprite = check_sprite
    else:
        hard_sprite = uncheck_sprite
    if normal_check:
        normal_sprite = check_sprite
    else:
        normal_sprite = uncheck_sprite
    if easy_check:
        easy_sprite = check_sprite
    else:
        easy_sprite = uncheck_sprite


pygame.init()
pygame.mixer.init()


# SOUNDS
win_sound = pygame.mixer.Sound("Sounds/win.mp3")
good = pygame.mixer.Sound("Sounds/good.mp3")
type_keyboard = pygame.mixer.Sound("Sounds/type.mp3")
error = pygame.mixer.Sound("Sounds/error.mp3")
loose = pygame.mixer.Sound("Sounds/loose.mp3")

# COLORS
grey = (50, 50, 50)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


X = 1080
Y = 720

text_font = 'Sugar Snow.ttf'

display_surface = pygame.display.set_mode((X, Y))

pygame.display.set_caption('Pendu')

font = pygame.font.Font(text_font, 32)
game_message_font = pygame.font.Font(text_font, 15)

# UI for WORD #
word_UI = font.render(shown_word, True, black)
word_Rect = word_UI.get_rect()
word_Rect.center = ((X // 2) - ((len(word) * 1.5) * 9) - 250, 400)
# ___________ #

# UI for GameMessage #
game_Message_tittle = pygame.font.Font(text_font, 25).render("Advert", True, white)
game_message_UI = game_message_font.render(game_message, True, red)
game_message_rect = (762, 190)
# __________________ #

# UI for MainMenu #
score_board_UI = pygame.transform.scale(pygame.image.load("buttons/Msg20.png"), (650, 705))
score_ICON = pygame.transform.scale(pygame.image.load("buttons/Icon54.png"), (80, 80))
score_UI = pygame.image.load("buttons/Button05.png")
info_UI = pygame.image.load("buttons/Msg15.png")
main_menu = pygame.image.load("buttons/Msg08.png")
main_menu_sized = pygame.transform.scale(main_menu, (380, 700))
game_name_UI = pygame.font.Font(text_font, 45).render("Pendu", True, white)
score_board_Tittle = pygame.font.Font(text_font, 60).render("Scoreboard", True, white)
retry_button_text = pygame.font.Font(text_font, 40).render("Retry", True, white)
continue_button_text = pygame.font.Font(text_font, 40).render("Continue", True, white)
play_button_text = pygame.font.Font(text_font, 40).render("Play", True, white)
quit_button_text = pygame.font.Font(text_font, 35).render("Quit", True, white)
exit_button_text = pygame.font.Font(text_font, 35).render("Exit", True, white)
hard_button_text = pygame.font.Font(text_font, 30).render("Hard", True, white)
normal_button_text = pygame.font.Font(text_font, 30).render("Normal", True, white)
easy_button_text = pygame.font.Font(text_font, 30).render("Easy", True, white)
# __________________ #

hard_check_UI = Button(hard_sprite, (80, 80), (750, 310), lambda: change_difficulty("Hard"))
normal_check_UI = Button(normal_sprite, (80, 80), (750, 390), lambda: change_difficulty("Normal"))
easy_check_UI = Button(easy_sprite, (80, 80), (750, 470), lambda: change_difficulty("Easy"))
main_menu_button = Button(f"buttons/Button24.png", (250, 100), (750, 550), lambda: change_state("MainMenu"))
continue_button = Button(f"buttons/Button23.png", (280, 120), (736, 450), lambda: change_state("Play"))
play_button = Button(f"buttons/Button23.png", (300, 130), (720, 180), lambda: change_state("Play"))
retry_button = Button(f"buttons/Button23.png", (280, 120), (736, 450), lambda: change_state("Play"))
quit_button = Button(f"buttons/Button25.png", (250, 100), (750, 550), lambda: exit())


def render_state(game_state):
    if game_state == "MainMenu":
        display_surface.fill(grey)
        display_surface.blit(main_menu_sized, (680, 10))
        display_surface.blit(game_name_UI, (810, 40))
        display_surface.blit(score_board_UI, (20, 15))
        display_surface.blit(score_board_Tittle, (180, 60))
        play_button.render(display_surface)
        display_surface.blit(play_button_text, (825, 228))
        quit_button.render(display_surface)
        display_surface.blit(quit_button_text, (840, 585))
        hard_check_UI = Button(hard_sprite, (80, 80), (750, 310), lambda: change_difficulty("Hard"))
        normal_check_UI = Button(normal_sprite, (80, 80), (750, 390), lambda: change_difficulty("Normal"))
        easy_check_UI = Button(easy_sprite, (80, 80), (750, 470), lambda: change_difficulty("Easy"))
        display_surface.blit(hard_button_text, (850, 335))
        display_surface.blit(normal_button_text, (850, 415))
        display_surface.blit(easy_button_text, (850, 495))
        hard_check_UI.render(display_surface)
        normal_check_UI.render(display_surface)
        easy_check_UI.render(display_surface)

    elif game_state == "Play" or state == "Loose" or state == "Win":
        display_surface.fill(white)
        display_surface.blit(main_menu_sized, (680, 10))
        display_surface.blit(score_UI, (740, 260))
        display_surface.blit(score_text, (820, 293))
        display_surface.blit(score_ICON, (745, 267))
        display_surface.blit(info_UI, (720, 100))
        main_menu_button.render(display_surface)
        display_surface.blit(exit_button_text, (840, 585))
        display_surface.blit(images[hangman_status], ((X // 2) - 260, 100))

        game_message_UI = game_message_font.render(game_message, True, red)
        display_surface.blit(game_Message_tittle, (827, 122))
        display_surface.blit(game_message_UI, game_message_rect)

        word_UI = font.render(shown_word if state == "Play" else word, True, black)
        display_surface.blit(word_UI, word_Rect)

        show_letters()

        if game_state == "Loose":
            retry_button.render(display_surface)
            display_surface.blit(retry_button_text, (816, 492))

        if game_state == "Win":
            continue_button.render(display_surface)
            display_surface.blit(continue_button_text, (790, 492))


while True:
    score_text = pygame.font.Font(text_font, 30).render(str(score), True, white)
    for event in pygame.event.get():

        if event.type == MESSAGE_CLEAR_EVENT:
            game_message = ""

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if state == "Play" or state == "Loose" or state == "Win":
                main_menu_button.get_event(event)
            else:
                hard_check_UI.get_event(event)
                normal_check_UI.get_event(event)
                easy_check_UI.get_event(event)
                play_button.get_event(event)
                quit_button.get_event(event)
            if state == "Loose":
                retry_button.get_event(event)
            if state == "Win":
                continue_button.get_event(event)

        if event.type == KEYDOWN:
            try:
                if state not in ["Loose", "Win", "MainMenu"] and event.key in range(96, 123):
                    if chr(event.key) in word:
                        if chr(event.key) in letter_discover:
                            type_keyboard.play()
                            show_command_message("character already discover !!!", 2)
                        else:
                            good.play()
                            score += 100
                            letter_discover.append(chr(event.key))
                            write_word()

                    elif hangman_status <= 4 and chr(event.key) not in letter_use:
                        score -= 50
                        error.play()
                        hangman_status += 1

                    elif hangman_status == 5 and chr(event.key) not in letter_use:
                        loose.play()
                        hangman_status += 1
                        show_command_message("Loose !!!", 5)
                        state = "Loose"
                    else:
                        show_command_message("character already used !!!", 2)
                        type_keyboard.play()
                    letter_use += chr(event.key)
                if event.key == 13 and state in ["Loose", "Win", "MainMenu"]:
                    change_state("Play")
                if event.key == 27 and state in ["Loose", "Win", "Play"]:
                    change_state("MainMenu")
            except:
                print("Imput Error")
    won = True

    if not letter_discover:
        won = False
    for letter in word:
        if letter not in letter_discover:
            won = False
    if won and state != "Win":
        state = "Win"

    # UI Update#
    render_state(state)
    pygame.display.update()
    # ___________ #

