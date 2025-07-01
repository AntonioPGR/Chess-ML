from typing import Optional
from helpers.BoardHelper import BoardHelper
from Pieces.Piece import Piece
from Pieces.Settings import PieceColor, PieceType
from Enums.BoardPosition import BoardPosition


class Pawn(Piece):
  def __init__(self, color: PieceColor):
    super().__init__(PieceType.PAWN, color)

  def isValidMove(self, fromPos: BoardPosition, toPos: BoardPosition, board: list[Optional[Piece]]) -> bool:
    direction = -1 if self.color == PieceColor.WHITE else 1
    toListPos = toPos.toListPosition()
    # Single move forward
    if fromPos.isInSameCol(toPos) and toPos.row == fromPos.row + direction:
      return board[toListPos] is None
    # Double move from starting row
    if (
      fromPos.isInSameCol(toPos) and
      fromPos.row == (6 if self.color == PieceColor.WHITE else 1) and
      toPos.row == fromPos.row + (2 * direction)
    ):
      return BoardHelper.isPathClear(fromPos, toPos, board)
    # Diagonal capture
    if abs(fromPos.col - toPos.col) == 1 and toPos.row == fromPos.row + direction:
      target_piece = board[toListPos]
      return target_piece is not None
    return False

  def isSpecialMove(self, from_pos: BoardPosition, to_pos: BoardPosition, board: list[Optional[Piece]]) -> bool:
    return False