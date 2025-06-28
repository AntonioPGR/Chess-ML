from enum import Enum


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
