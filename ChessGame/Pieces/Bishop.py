from typing import Optional

from helpers.BoardHelper import BoardHelper
from Pieces.Piece import Piece
from Pieces.Settings import PieceColor, PieceType
from helpers.BoardPosition import BoardPosition


class Bishop(Piece):
  def __init__(self, color: PieceColor):
    super().__init__(PieceType.BISHOP, color)

  def isValidMove(self, from_pos: BoardPosition, to_pos: BoardPosition, board: list[Optional[Piece]]) -> bool:
    row_diff = abs(from_pos.row - to_pos.row)
    col_diff = abs(from_pos.col - to_pos.col)
    if (
      row_diff != col_diff or
      not BoardHelper.isPathClear(from_pos, to_pos, board)
    ):
      return False
    to_index = to_pos.toListPosition()
    target_piece = board[to_index]
    return target_piece is None or target_piece.color != self.color