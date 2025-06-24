import pygame

from files.Board import Board
from files.Piece import PieceType, PieceColor, Piece


def _loadImages() -> dict:
  images = {}
  for color in PieceColor:
    images[color] = {}
    for piece_type in PieceType:
      key = f"{color.value}-{piece_type.value}"
      path = f"assets/{key}.png"
      images[color][piece_type] = pygame.image.load(path)
  return images


class BoardUI:
  BORDER_SIZE = 8
  SQUARE_SIZE = 96
  BOARD_BACKGROUND_URL = "assets/board.png"
  DISPLAY_NAME = "Chess Board"
  DISPLAY_ICON_URL = "assets/icon.png"

  def __init__(self, screen: pygame.Surface):
    self.screen = screen
    self.piecesImages = _loadImages()
    self.renderDisplay()

  def renderDisplay(self):
    pygame.display.set_caption(self.DISPLAY_NAME)
    icon_image = pygame.image.load(self.DISPLAY_ICON_URL)
    pygame.display.set_icon(icon_image)
    board_image = pygame.image.load(self.BOARD_BACKGROUND_URL)
    self.screen.blit(board_image, (0, 0))

  def renderBoard(self, board: Board):
    for i in range(64):
      piece = board.get_piece(i)
      if piece is not None: self.renderPieceAtPosition(i, piece)

  def renderPieceAtPosition(self, pos: int, piece: Piece):
    if piece.color in self.piecesImages and piece.type in self.piecesImages[piece.color]:
      image = self.piecesImages[piece.color][piece.type]
      piece_width, piece_height = piece.size
      row = pos // 8
      col = pos % 8
      tile_x = self.BORDER_SIZE + col * self.SQUARE_SIZE
      tile_y = self.BORDER_SIZE + row * self.SQUARE_SIZE
      x = tile_x + (self.SQUARE_SIZE - piece_width) // 2
      y = tile_y + (self.SQUARE_SIZE - piece_height) // 2
      self.screen.blit(image, (x, y))
