from typing import Optional

from helpers.BoardHelper import BoardHelper
from Pieces.Piece import Piece
from Pieces.Settings import PieceColor, PieceType
from helpers.BoardPosition import BoardPosition


class Rook(Piece):
  def __init__(self, color: PieceColor):
    super().__init__(PieceType.ROOK, color)

  def isValidMove(self, fromPos: BoardPosition, toPos: BoardPosition, board: list[Optional[Piece]]) -> bool:
    if (
      fromPos.isInSameRow(toPos) or
      fromPos.isInSameCol(toPos)
    ):
      return BoardHelper.isPathClear(fromPos, toPos, board)
    return False