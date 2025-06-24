import pygame

from files.Board import Board
from files.BoardUI import BoardUI, Piece, PieceType, PieceColor

SCREEN_WIDTH = 784
SCREEN_HEIGHT = 784

def loadGame():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  board_ui = BoardUI(screen)
  board = Board()
  board_ui.renderBoard(board)


  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    pygame.display.flip()
  pygame.quit()

if __name__ == '__main__': loadGame()

