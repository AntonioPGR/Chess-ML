from typing import Optional

from files.Piece import Piece, PieceNotationMap


class Board:

  START_PIECES_STRING = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

  def __init__(self):
    self.board: list[Optional[Piece]] = [None for _ in range(64)]
    self._initialize_board()

  def _initialize_board(self):
    board_index = 0
    for char in self.START_PIECES_STRING:
      if char.isdigit():
        board_index += int(char)
      elif char == '/':
        continue
      else:
        piece_type, piece_color = PieceNotationMap[char]
        self.board[board_index] = Piece(piece_type, piece_color)
        board_index += 1

  def get_piece(self, pos: int) -> Optional[Piece]:
    return self.board[pos]

  def move_piece(self, from_pos: int, to_pos: int):
    piece = self.get_piece(from_pos)
    if piece is not None:
      self.board[to_pos] = piece
      self.board[from_pos] = None

  def remove_piece(self, pos: int):
    self.board[pos] = None
