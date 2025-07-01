from Enums.MoveType import MoveType
from Pieces.Piece import Piece
from Enums.PieceColor import PieceColor
from Enums.BoardPosition import BoardPosition


class PieceMove:
  fromSquare: BoardPosition
  toSquare: BoardPosition
  piece: Piece
  captured: Piece | None = None
  putInCheck: PieceColor | None = None
  putInMate: PieceColor | None = None
  moveType: MoveType
  notation: string


