from typing import Optional
from Pieces.Piece import Piece
from Pieces.Settings import PieceColor, PieceType
from helpers.BoardPosition import BoardPosition


class King(Piece):
  def __init__(self, color: PieceColor):
    super().__init__(PieceType.KING, color)

  def isValidMove(self, fromPos: BoardPosition, toPos: BoardPosition, board: list[Optional[Piece]]) -> bool:
    row_diff = abs(fromPos.row - toPos.row)
    col_diff = abs(fromPos.col - toPos.col)
    if max(row_diff, col_diff) == 1:
      return True
    return False

  def isSpecialMove(self, from_pos: BoardPosition, to_pos: BoardPosition, board: list[Optional[Piece]]) -> bool:
    if len(self.moves_history) != 0 or from_pos.row != to_pos.row:
        return False
    row = from_pos.row
    # Kingside castling
    if to_pos.col == 6:
        rook_pos = BoardPosition(row, 7)
        rook = board[rook_pos.toListPosition()]
        if (
            not isinstance(rook, Piece) or
            rook.type != PieceType.ROOK or
            rook.color != self.color or
            len(rook.moves_history) != 0
        ):
            return False

        if board[BoardPosition(row, 5).toListPosition()] is not None or board[BoardPosition(row, 6).toListPosition()] is not None:
            return False

        # Move rook to f1/f8
        board[BoardPosition(row, 5).toListPosition()] = rook
        board[rook_pos.toListPosition()] = None
        rook.saveMovent(rook_pos, BoardPosition(row, 5))
        return True

    # Queenside castling
    if to_pos.col == 2:
        rook_pos = BoardPosition(row, 0)
        rook = board[rook_pos.toListPosition()]
        if (
            not isinstance(rook, Piece) or
            rook.type != PieceType.ROOK or
            rook.color != self.color or
            len(rook.moves_history) != 0
        ):
            return False
        if (
            board[BoardPosition(row, 1).toListPosition()] is not None or
            board[BoardPosition(row, 2).toListPosition()] is not None or
            board[BoardPosition(row, 3).toListPosition()] is not None
        ):
            return False
        # Move rook to d1/d8
        board[BoardPosition(row, 3).toListPosition()] = rook
        board[rook_pos.toListPosition()] = None
        rook.saveMovent(rook_pos, BoardPosition(row, 3))
        return True
    return False