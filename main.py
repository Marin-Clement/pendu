import pygame
import sys
from pygame.locals import *

MESSAGE_CLEAR_EVENT = USEREVENT + 1

images = []
hangman_status = 0

word = "akunamatata"

letter_discover = []

shown_word = ""


game_message = ""
last_message_time = 0


state = ""


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


for i in range(7):
    image = pygame.image.load(f"images/hangman{i}.png")
    images.append(image)


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)



X = 1080
Y = 720

display_surface = pygame.display.set_mode((X, Y))

pygame.display.set_caption('Pendu')

font = pygame.font.Font('freesansbold.ttf', 32)

# UI for WORD #
word_UI = font.render(shown_word, True, black)
word_Rect = word_UI.get_rect()
word_Rect.center = ((X // 2) - ((len(word) * 1.5) * 9) - 250, 500)
write_word()
# ___________ #

# UI for GameMessage #
game_message_UI = font.render(shown_word, True, black)
game_message_rect = (10, 10)
# __________________ #


while True:

    # UI Update#
    display_surface.fill(white)
    display_surface.blit(images[hangman_status], ((X // 2) - 300, 200))

    pygame.draw.rect(display_surface, (96, 96, 96), [700, 0, X, Y])
    pygame.draw.rect(display_surface, black, [700, 0, 5, Y])

    word_UI = font.render(shown_word, True, black)
    display_surface.blit(word_UI, word_Rect)

    game_message_UI = font.render(game_message, True, black)
    display_surface.blit(game_message_UI, game_message_rect)
    # ___________ #

    for event in pygame.event.get():
        if event.type == MESSAGE_CLEAR_EVENT:
            game_message = ""

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            try:
                if chr(event.key) in word:
                    if chr(event.key) in letter_discover:
                        show_command_message("character already discover !!!", 2)
                    else:
                        letter_discover.append(chr(event.key))
                        write_word()

                elif hangman_status <= 4:
                    hangman_status += 1

                elif hangman_status == 5:
                    hangman_status += 1
                    show_command_message("Loose !!!", 2)
                else:
                    print("please stop")
            except:
                print("Imput Error")

    won = True

    for letter in word:
        if letter not in letter_discover:
            won = False

    pygame.display.update()
