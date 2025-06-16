import pygame

SCREEN_WIDTH = 784
SCREEN_HEIGHT = 784

BOARD_IMAGE = pygame.image.load('assets/board.png')
PAWS_IMAGE = pygame.image.load('assets/white-pawn.png')

def loadGame():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(BOARD_IMAGE, (0, 0))

    screen.blit(PAWS_IMAGE, (0, 0))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__': loadGame()

