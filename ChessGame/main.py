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
  x_down = y_down = x_up = y_up = None
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.MOUSEBUTTONDOWN:
        x_down, y_down = pygame.mouse.get_pos()
      if event.type == pygame.MOUSEBUTTONUP:
        x_up, y_up = pygame.mouse.get_pos()
      if x_down is not None and y_down is not None and x_up is not None and y_up is not None:
        boardUi.handleClick((x_down, y_down), (x_up, y_up))
        x_down = y_down = x_up = y_up = None

    pygame.display.flip()
  pygame.quit()

if __name__ == '__main__': loadGame()

