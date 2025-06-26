import pygame
import os
from ChessGame.Board import Board


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
        piece = self.board.getPieceAtPosition(index)
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

  def pixelToSquare(self, pos: tuple[int, int]) -> tuple[int, int]:
    x, y = pos
    col = (x - self.BORDER_SIZE) // self.SQUARE_SIZE
    row = (y - self.BORDER_SIZE) // self.SQUARE_SIZE
    return row, col

  def isOnBoard(self, row: int, col: int) -> bool:
    return 0 <= row < 8 and 0 <= col < 8

  def handleMouseDown(self, pos: tuple[int, int]):
    row, col = self.pixelToSquare(pos)
    if not self.isOnBoard(row, col): return
    index = self.board.getPositionFromRowAndColumn((row, col))
    piece = self.board.getPieceAtPosition(index)
    if not piece or piece.color != self.board.turnColor: return
    self.selectedPiece = index
    w, h = piece.size
    tile_x = self.BORDER_SIZE + col * self.SQUARE_SIZE
    tile_y = self.BORDER_SIZE + row * self.SQUARE_SIZE
    self.dragOffset = (pos[0] - (tile_x + (self.SQUARE_SIZE - w) // 2), pos[1] - (tile_y + (self.SQUARE_SIZE - h) // 2))

  def handleMovePiece(self, from_pos: tuple[int, int], to_pos: tuple[int, int]):
    row_from, col_from = self.pixelToSquare(from_pos)
    row_to, col_to = self.pixelToSquare(to_pos)
    if (
      not self.isOnBoard(row_from, col_from) or
      not self.isOnBoard(row_to, col_to) or
      (row_from == row_to and col_from == col_to)
    ):
      self.selectedPiece = None
      return
    self.board.movePiece((row_from, col_from), (row_to, col_to))
    self.selectedPiece = None
    self.dragOffset = (0, 0)
