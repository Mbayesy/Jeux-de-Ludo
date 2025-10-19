"""Jeu de ludo avec pygame"""
HEIGHT = 600
WIDTH = 600
ROWS = 15
COLUMNS = 15
SQUARE_SIZE = WIDTH // COLUMNS

import pygame
import sys
from game import Game

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de ludo avec pygame")

clock = pygame.time.Clock()
game = Game()

while True:

    screen.fill((255, 255, 255))
    game.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    game.draw(screen)
    game.play_turn(screen)
    pygame.display.flip()
    clock.tick(60)