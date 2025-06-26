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

  def getPositionFromRowAndColumn(self, pos: tuple[int, int]) -> int:
    return pos[0] * 8 + pos[1]

  def getPieceAtPosition(self, pos: int) -> Optional[Piece]:
    return self.board[pos]

  def isValidMove(self, from_pos: tuple[int, int], to_pos: tuple[int, int]) -> bool:
    from_index = self.getPositionFromRowAndColumn(from_pos)
    to_index = self.getPositionFromRowAndColumn(to_pos)
    piece = self.board[from_index]
    target = self.board[to_index]

    if (
      piece is None or
      piece.color != self.turnColor or
      (target is not None and target.color == self.turnColor)
    ):
      return False
    # TODO: implement piece-specific move rules
    return True

  def movePiece(self, from_pos: tuple[int, int], to_pos: tuple[int, int]) -> bool:
    if not self.isValidMove(from_pos, to_pos):
      return False
    from_index = self.getPositionFromRowAndColumn(from_pos)
    to_index = self.getPositionFromRowAndColumn(to_pos)
    self.board[to_index], self.board[from_index] = self.board[from_index], None
    self.turnColor = PieceColor.BLACK if self.turnColor == PieceColor.WHITE else PieceColor.WHITE
    return True
