import pygame
import sys
from pygame.locals import *

pygame.init()


white = (255, 255, 255)
black = (0, 0, 0)

X = 1080
Y = 720


display_surface = pygame.display.set_mode((X, Y))

pygame.display.set_caption('Pendu')

font = pygame.font.Font('freesansbold.ttf', 32)

text = font.render('Hello World', True, black)

textRect = text.get_rect()

textRect.center = (X // 2, Y // 2)

images = []
hangman_status = 0

for i in range(7):
    image = pygame.image.load(f"images/hangman{i}.png")
    images.append(image)

while True:

    display_surface.fill(white)

    display_surface.blit(images[hangman_status], ((X // 2) - 50, 50))

    display_surface.blit(text, textRect)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            try:
                if hangman_status <= 4:
                    hangman_status += 1
                elif hangman_status == 5:
                    hangman_status += 1
                    print("loose")
                else:
                    print("please stop")
            except:
                print("Imput Error")

        pygame.display.update()
