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

  def handleClick(self, x: int, y: int):
    col = (x - self.BORDER_SIZE) // self.SQUARE_SIZE
    row = (y - self.BORDER_SIZE) // self.SQUARE_SIZE

    if not (0 <= row < 8 and 0 <= col < 8):
        return

    if self.selectedPiece is None:
        if self.board.getPieceAtPosition(row * 8 + col) is not None:
            self.selectedPiece = (row, col)
        return

    self.board.movePiece(self.selectedPiece, (row, col))
    self.selectedPiece = None
    self.renderBoard()