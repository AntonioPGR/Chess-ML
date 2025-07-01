import pygame
from Board import Board
from BoardUI import BoardUI
from Enums.ScreenPosition import ScreenPosition

SCREEN_WIDTH = 784
SCREEN_HEIGHT = 784

def loadGame():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  board = Board()
  boardUi = BoardUI(screen, board)

  running = True
  from_pos : ScreenPosition | None = None
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        from_pos = ScreenPosition.fromTuple(event.pos)
        boardUi.handleMouseDown(from_pos)
      elif event.type == pygame.MOUSEBUTTONUP and from_pos:
        to_pos = ScreenPosition.fromTuple(event.pos)
        boardUi.handleMovePiece(from_pos, to_pos)
        from_pos = None

    boardUi.renderBoard()
    pygame.display.flip()
  pygame.quit()

if __name__ == '__main__': loadGame()

