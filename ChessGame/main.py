import pygame
from ChessGame.Board import Board
from ChessGame.BoardUI import BoardUI

SCREEN_WIDTH = 784
SCREEN_HEIGHT = 784

def loadGame():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  board = Board()
  boardUi = BoardUI(screen, board)

  running = True
  from_pos = None
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        from_pos = event.pos
        boardUi.handleMouseDown(from_pos)
      elif event.type == pygame.MOUSEBUTTONUP and from_pos:
        boardUi.handleMovePiece(from_pos, event.pos)
        from_pos = None

    boardUi.renderBoard()
    pygame.display.flip()
  pygame.quit()

if __name__ == '__main__': loadGame()

