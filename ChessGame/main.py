import pygame

from ChessGame.Board import Board
from ChessGame.BoardUI import BoardUI, Piece, PieceType, PieceColor

SCREEN_WIDTH = 784
SCREEN_HEIGHT = 784

def loadGame():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  board = Board()
  boardUi = BoardUI(screen, board)

  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        boardUi.handleClick(x, y)

    pygame.display.flip()
  pygame.quit()

if __name__ == '__main__': loadGame()

