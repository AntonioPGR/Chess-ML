import pygame
import os
from ChessGame.Board import Board
from ChessGame.Piece import PieceType, PieceColor, Piece


class BoardUI:
  BORDER_SIZE = 8
  SQUARE_SIZE = 96
  BOARD_BACKGROUND_URL = os.path.join(os.path.dirname(__file__), "assets/board.png")
  DISPLAY_ICON_URL = os.path.join(os.path.dirname(__file__), "assets/icon.png")
  DISPLAY_NAME = "Chess Board"

  selectedPiece = None

  def __init__(self, screen: pygame.Surface, board: Board):
    self.screen = screen
    self.board = board
    self.renderBoard()

  def renderBoard(self):
    pygame.display.set_caption(self.DISPLAY_NAME)
    pygame.display.set_icon(pygame.image.load(self.DISPLAY_ICON_URL))
    self.screen.blit(pygame.image.load(self.BOARD_BACKGROUND_URL), (0, 0))
    for i in range(64):
      piece = self.board.getPieceAtPosition(i)
      if piece is not None:
        piece_width, piece_height = piece.size
        row, col = i // 8, i % 8
        tile_x, tile_y = self.BORDER_SIZE + col * self.SQUARE_SIZE, self.BORDER_SIZE + row * self.SQUARE_SIZE
        x = tile_x + (self.SQUARE_SIZE - piece_width) // 2
        y = tile_y + (self.SQUARE_SIZE - piece_height) // 2
        self.screen.blit(piece.image, (x, y))

  def pixelToSquare(self, pos: tuple[int, int]) -> tuple[int, int]:
    x, y = pos
    col = (x - self.BORDER_SIZE) // self.SQUARE_SIZE
    row = (y - self.BORDER_SIZE) // self.SQUARE_SIZE
    return row, col

  def isOnBoard(self, row: int, col: int) -> bool:
    return 0 <= row < 8 and 0 <= col < 8

  def handleClick(self, from_pos: tuple[int, int], to_pos: tuple[int, int]):
    row_from, col_from = self.pixelToSquare(from_pos)
    row_to, col_to = self.pixelToSquare(to_pos)
    if (
      not self.isOnBoard(row_from, col_from) or
      not self.isOnBoard(row_to, col_to) or
      (row_from == row_to and col_from == col_to)
    ): return
    self.board.movePiece((row_from, col_from), (row_to, col_to))
    self.selectedPiece = None
    self.renderBoard()