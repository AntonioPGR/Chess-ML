from typing import Optional
from Pieces.NotationMap import PieceNotationMap
from Pieces.Piece import Piece, PieceColor
from helpers.BoardPosition import BoardPosition


class Board:
  START_PIECES_STRING = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
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
        self.board[board_index] = PieceNotationMap[char]
        board_index += 1

  def getPieceByBoardPosition(self, boardPos: BoardPosition) -> Optional[Piece]:
    return self.getPieceByListPosition(boardPos.toListPosition())

  def getPieceByListPosition(self, pos: int) -> Optional[Piece]:
    return self.board[pos]

  def isValidMove(self, fromPos: BoardPosition, toPos: BoardPosition) -> bool:
    piece = self.board[fromPos.toListPosition()]
    target = self.board[toPos.toListPosition()]
    if (
      piece is None or
      piece.color != self.turnColor or
      (target is not None and target.color == self.turnColor) or
      not (piece.isValidMove(fromPos, toPos, self.board) or piece.isSpecialMove(fromPos, toPos, self.board))
    ):
      return False
    return True

  def movePiece(self, from_pos: BoardPosition, to_pos: BoardPosition):
    if not self.isValidMove(from_pos, to_pos):
        return
    piece = self.board[from_pos.toListPosition()]
    piece.saveMovent(from_pos, to_pos)
    self.board[to_pos.toListPosition()] = piece
    self.board[from_pos.toListPosition()] = None
    self.turnColor = PieceColor.BLACK if self.turnColor == PieceColor.WHITE else PieceColor.WHITE

