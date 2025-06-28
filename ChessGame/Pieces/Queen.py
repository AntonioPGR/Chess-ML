from typing import Optional

from helpers.BoardHelper import BoardHelper
from Pieces.Piece import Piece
from Pieces.Settings import PieceColor, PieceType
from helpers.BoardPosition import BoardPosition


class Queen(Piece):
  def __init__(self, color: PieceColor):
    super().__init__(PieceType.QUEEN, color)

  def isValidMove(self, from_pos: BoardPosition, to_pos: BoardPosition, board: list[Optional[Piece]]) -> bool:
    row_diff = abs(from_pos.row - to_pos.row)
    col_diff = abs(from_pos.col - to_pos.col)
    is_diagonal = row_diff == col_diff
    is_straight = from_pos.row == to_pos.row or from_pos.col == to_pos.col
    if (
      not (is_diagonal or is_straight) or
      not BoardHelper.isPathClear(from_pos, to_pos, board)
    ):
      return False
    to_index = to_pos.toListPosition()
    target_piece = board[to_index]
    return target_piece is None or target_piece.color != self.color