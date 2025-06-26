from abc import ABC, abstractmethod
from enum import Enum
import os
from typing import Optional
import pygame
from BoardHelper import BoardHelper


class PieceType(Enum):
  PAWN = "pawn"
  KNIGHT = "knight"
  BISHOP = "bishop"
  ROOK = "rook"
  KING = "king"
  QUEEN = "queen"

class PieceColor(Enum):
  WHITE = "white"
  BLACK = "black"

PieceSize = {
  PieceType.PAWN: (66, 87),
  PieceType.KNIGHT: (76, 76),
  PieceType.BISHOP: (76, 78),
  PieceType.ROOK: (76, 83),
  PieceType.KING: (76, 76),
  PieceType.QUEEN: (76, 68),
}

class Piece(ABC):
  def __init__(
    self,
    pieceType: PieceType,
    color: PieceColor,
  ):
    self.type = pieceType
    self.color = color
    self.size = PieceSize[pieceType]
    self._loadImage()

  def _loadImage(self):
    base_path = os.path.join(os.path.dirname(__file__), "assets")
    filename = f"{self.color.value}-{self.type.value}.png"
    full_path = os.path.join(base_path, filename)
    self.image = pygame.image.load(full_path)

  @abstractmethod
  def isValidMove(self, from_pos: tuple[int, int], to_pos: tuple[int, int], board: list) -> bool:
    pass

class Pawn(Piece):
  def __init__(self, color: PieceColor):
    super().__init__(PieceType.PAWN, color)

  def isValidMove(self, from_pos: tuple[int, int], to_pos: tuple[int, int], board: list[Optional[Piece]]) -> bool:
    from_row, from_col = from_pos
    to_row, to_col = to_pos
    direction = -1 if self.color == PieceColor.WHITE else 1
    pos = BoardHelper.getPositionFromRowAndColumn(to_pos)
    # Single move forward
    if from_col == to_col and to_row == from_row + direction:
      return board[pos] is None
    # Double move from starting row
    if (from_col == to_col and
            from_row == (6 if self.color == PieceColor.WHITE else 1) and
            to_row == from_row + (2 * direction)):
      between_pos = BoardHelper.getPositionFromRowAndColumn((from_row + direction, to_col))
      return board[pos] is None and board[between_pos] is None
    # Diagonal capture
    if abs(from_col - to_col) == 1 and to_row == from_row + direction:
      target_piece = board[pos]
      return target_piece is not None and target_piece.color != self.color
    #TODO: En passant
    return False

class Knight(Piece):
  def __init__(self, color: PieceColor):
    super().__init__(PieceType.KNIGHT, color)

  def isValidMove(self, from_pos: tuple, to_pos: tuple, board: list[Optional[Piece]]) -> bool:
    from_row, from_col = from_pos
    to_row, to_col = to_pos
    return True

class Bishop(Piece):
  def __init__(self, color: PieceColor):
    super().__init__(PieceType.BISHOP, color)

  def isValidMove(self, from_pos: tuple, to_pos: tuple, board: list[Optional[Piece]]) -> bool:
    from_row, from_col = from_pos
    to_row, to_col = to_pos
    return True

class Rook(Piece):
  def __init__(self, color: PieceColor):
    super().__init__(PieceType.ROOK, color)

  def isValidMove(self, from_pos: tuple, to_pos: tuple, board: list[Optional[Piece]]) -> bool:
    from_row, from_col = from_pos
    to_row, to_col = to_pos
    return True

class King(Piece):
  def __init__(self, color: PieceColor):
    super().__init__(PieceType.KING, color)

  def isValidMove(self, from_pos: tuple, to_pos: tuple, board: list[Optional[Piece]]) -> bool:
    from_row, from_col = from_pos
    to_row, to_col = to_pos
    return True

class Queen(Piece):
  def __init__(self, color: PieceColor):
    super().__init__(PieceType.QUEEN, color)

  def isValidMove(self, from_pos: tuple, to_pos: tuple, board: list[Optional[Piece]]) -> bool:
    from_row, from_col = from_pos
    to_row, to_col = to_pos
    return True

PieceNotationMap = {
  'r': Rook(PieceColor.BLACK),
  'n': Knight(PieceColor.BLACK),
  'b': Bishop(PieceColor.BLACK),
  'q': Queen(PieceColor.BLACK),
  'k': King(PieceColor.BLACK),
  'p': Pawn(PieceColor.BLACK),
  'R': Rook(PieceColor.WHITE),
  'N': Knight(PieceColor.WHITE),
  'B': Bishop(PieceColor.WHITE),
  'Q': Queen(PieceColor.WHITE),
  'K': King(PieceColor.WHITE),
  'P': Pawn(PieceColor.WHITE),
}