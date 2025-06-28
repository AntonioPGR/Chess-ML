import pygame
import os
from Board import Board
from helpers.BoardPosition import BoardPosition
from helpers.ScreenPosition import ScreenPosition


class BoardUI:
  BORDER_SIZE = 8
  SQUARE_SIZE = 96

  BOARD_BACKGROUND = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets/board.png"))
  DISPLAY_ICON = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets/icon.png"))
  DISPLAY_CAPTION = "Chess Board"

  selectedPiece = None
  dragOffset = (0, 0)

  def __init__(self, screen: pygame.Surface, board: Board):
    self.screen = screen
    self.board = board
    self.renderBoard()
    pygame.display.set_caption(self.DISPLAY_CAPTION)
    pygame.display.set_icon(self.DISPLAY_ICON)

  def drawPiece(self, image: pygame.Surface, row: int, col: int):
    w, h = image.get_size()
    tile_x = self.BORDER_SIZE + col * self.SQUARE_SIZE
    tile_y = self.BORDER_SIZE + row * self.SQUARE_SIZE
    x = tile_x + (self.SQUARE_SIZE - w) // 2
    y = tile_y + (self.SQUARE_SIZE - h) // 2
    self.screen.blit(image, (x, y))

  def renderBoard(self):
    self.screen.blit(self.BOARD_BACKGROUND, (0, 0))
    dragged_piece = None
    for index in range(64):
        piece = self.board.getPieceByListPosition(index)
        if piece is None:
            continue
        if index == self.selectedPiece:
            dragged_piece = piece
        else:
            self.drawPiece(piece.image, index // 8, index % 8)
    if dragged_piece:
        mx, my = pygame.mouse.get_pos()
        ox, oy = self.dragOffset
        self.screen.blit(dragged_piece.image, (mx - ox, my - oy))


  def handleMouseDown(self, screenPos: ScreenPosition):
    boardPos = BoardPosition.fromScreenPosition(screenPos, self.BORDER_SIZE, self.SQUARE_SIZE)
    if not boardPos.isOnBoard():
      return
    piece = self.board.getPieceByBoardPosition(boardPos)
    if not piece or piece.color != self.board.turnColor:
      return

    self.selectedPiece = boardPos.toListPosition()

    w, h = piece.size
    tile_x = self.BORDER_SIZE + boardPos.col * self.SQUARE_SIZE
    tile_y = self.BORDER_SIZE + boardPos.row * self.SQUARE_SIZE
    self.dragOffset = (screenPos.x - (tile_x + (self.SQUARE_SIZE - w) // 2), screenPos.y - (tile_y + (self.SQUARE_SIZE - h) // 2))


  def handleMovePiece(self, screenFromPos: ScreenPosition, screenToPos: ScreenPosition):
    boardFromPos = BoardPosition.fromScreenPosition(screenFromPos, self.BORDER_SIZE, self.SQUARE_SIZE)
    boardToPos = BoardPosition.fromScreenPosition(screenToPos, self.BORDER_SIZE, self.SQUARE_SIZE)
    if (
      not boardFromPos.isOnBoard() or
      not boardToPos.isOnBoard() or
      boardToPos.equals(boardFromPos)
    ):
      self.selectedPiece = None
      return
    self.board.movePiece(boardFromPos, boardToPos)
    self.selectedPiece = None
    self.dragOffset = (0, 0)
