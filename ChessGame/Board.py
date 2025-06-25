from typing import Optional

from ChessGame.Piece import Piece, PieceNotationMap, PieceColor


class Board:

  START_PIECES_STRING = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
  turnColor = PieceColor.WHITE

  def __init__(self):
    self.board: list[Optional[Piece]] = [None for _ in range(64)]
    self._initializeBoard()

  def _initializeBoard(self):
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

  def getPieceAtPosition(self, pos: int) -> Optional[Piece]:
    return self.board[pos]

  def movePiece(self, from_pos: tuple[int, int], to_pos: tuple[int, int]) -> None:
    from_index = from_pos[0] * 8 + from_pos[1]
    to_index = to_pos[0] * 8 + to_pos[1]
    if (
      from_index == to_index or
      self.board[from_index] is None or
      self.board[from_index].color != self.turnColor or
      (self.board[to_index] is not None and self.board[to_index].color == self.turnColor)
    ): return;
    self.board[to_index] = self.board[from_index]
    self.board[from_index] = None
    self.turnColor = PieceColor.BLACK if self.turnColor == PieceColor.WHITE else PieceColor.WHITE
