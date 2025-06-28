from typing import Optional
from Pieces.Piece import Piece
from Pieces.Settings import PieceColor
from helpers.BoardPosition import BoardPosition


class BoardHelper:

  @staticmethod
  def getPieceByRowAndColumn(row: int, col: int, board: list):
    board_pos = BoardHelper.getListPositionByRowAndColumn(row, col)
    return board[board_pos]

  @staticmethod
  def getListPositionByRowAndColumn(row: int, col: int,) -> int:
    return row * 8 + col

  @staticmethod
  def isPathClear(from_pos: BoardPosition, to_pos: BoardPosition, board: list[Optional[Piece]]) -> bool:
    row_step = col_step = 0
    if from_pos.row == to_pos.row:  # horizontal
      col_step = 1 if to_pos.col > from_pos.col else -1
    elif from_pos.col == to_pos.col:  # vertical
      row_step = 1 if to_pos.row > from_pos.row else -1
    elif abs(from_pos.row - to_pos.row) == abs(from_pos.col - to_pos.col):  # diagonal
      row_step = 1 if to_pos.row > from_pos.row else -1
      col_step = 1 if to_pos.col > from_pos.col else -1
    else:
      return False
    current_row = from_pos.row + row_step
    current_col = from_pos.col + col_step
    while current_row != to_pos.row or current_col != to_pos.col:
      index = current_row * 8 + current_col
      if board[index] is not None:
        return False
      current_row += row_step
      current_col += col_step
    return True

  @staticmethod
  def isInCheck(board: list[Optional[Piece]], color: PieceColor) -> bool:
    king_pos = None
    for pos, piece in enumerate(board):
      if piece and piece.type == "KING" and piece.color == color:
        king_pos = pos
        break
    if king_pos is None:
      return False
    for pos, piece in enumerate(board):
      if piece and piece.color != color:
        if piece.isValidMove(BoardPosition.fromListPosition(pos), BoardPosition.fromListPosition(king_pos), board):
          return True
    return False

  @staticmethod
  def isCheckMate(board: list[Optional[Piece]], color: PieceColor) -> bool:
    if not BoardHelper.isInCheck(board, color):
      return False
    for from_pos, piece in enumerate(board):
      if piece and piece.color == color:
        for to_pos in range(64):
          new_board = board.copy()
          if piece.isValidMove(BoardPosition.fromListPosition(from_pos), BoardPosition.fromListPosition(to_pos), new_board):
            new_board[to_pos] = piece
            new_board[from_pos] = None
            if not BoardHelper.isInCheck(new_board, color):
              return False
    return True
