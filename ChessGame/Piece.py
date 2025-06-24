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

PiecesSizes = {
  PieceType.PAWN: (66, 87),
  PieceType.KNIGHT: (76, 76),
  PieceType.BISHOP: (76, 78),
  PieceType.ROOK: (76, 83),
  PieceType.KING: (76, 76),
  PieceType.QUEEN: (76, 68),
}

PieceNotationMap = {
  'r': (PieceType.ROOK, PieceColor.BLACK),
  'n': (PieceType.KNIGHT, PieceColor.BLACK),
  'b': (PieceType.BISHOP, PieceColor.BLACK),
  'q': (PieceType.QUEEN, PieceColor.BLACK),
  'k': (PieceType.KING, PieceColor.BLACK),
  'p': (PieceType.PAWN, PieceColor.BLACK),
  'R': (PieceType.ROOK, PieceColor.WHITE),
  'N': (PieceType.KNIGHT, PieceColor.WHITE),
  'B': (PieceType.BISHOP, PieceColor.WHITE),
  'Q': (PieceType.QUEEN, PieceColor.WHITE),
  'K': (PieceType.KING, PieceColor.WHITE),
  'P': (PieceType.PAWN, PieceColor.WHITE),
}

class Piece:
  def __init__(self, pieceType: PieceType, color: PieceColor):
    self.type = pieceType
    self.color = color
    self.size = PiecesSizes[pieceType]
