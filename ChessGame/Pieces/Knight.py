from typing import Optional
from Pieces.Piece import Piece
from Pieces.Settings import PieceColor, PieceType
from Enums.BoardPosition import BoardPosition


class Knight(Piece):
  def __init__(self, color: PieceColor):
    super().__init__(PieceType.KNIGHT, color)

  def isValidMove(self, from_pos: BoardPosition, to_pos: BoardPosition, board: list[Optional[Piece]]) -> bool:
    row_diff = abs(from_pos.row - to_pos.row)
    col_diff = abs(from_pos.col - to_pos.col)
    if not ((row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)):
      return False
    to_index = to_pos.toListPosition()
    target_piece = board[to_index]
    return target_piece is None or target_piece.color != self.color