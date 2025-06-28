from Pieces.Bishop import Bishop
from Pieces.Knight import Knight
from Pieces.Queen import Queen
from Pieces.Rook import Rook
from Pieces.Pawn import Pawn
from Pieces.King import King
from Pieces.Settings import PieceColor


PieceNotationMap = {
  'r': Rook(PieceColor.BLACK),
  'n': Knight(PieceColor.BLACK),
  'b': Bishop(PieceColor.BLACK),
  'q': Queen(PieceColor.BLACK),
  'k': King(PieceColor.BLACK),
  'p': Pawn(PieceColor.BLACK),
  'R': Rook(PieceColor.WHITE),
  'N': Knight(PieceColor.WHITE),
  'B': Bishop(PieceColor.WHITE),
  'Q': Queen(PieceColor.WHITE),
  'K': King(PieceColor.WHITE),
  'P': Pawn(PieceColor.WHITE),
}