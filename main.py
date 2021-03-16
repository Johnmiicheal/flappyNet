import pygame
from defs import *

def run_game():
    pygame.init()
    gameDisplay = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
    pygame.display.set_caption('I believe I can fly')

    running = True
    bgImg = pygame.image.load(BG_FILENAME)

    clock = pygame.time.Clock()
    dt = 0
    game_time = 0

    while running:

        dt = clock.tick(FPS)
        game_time += dt


        gameDisplay.blit(bgImg, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False

        pygame.display.update()


if __name__ == "__main__":
    run_game()


