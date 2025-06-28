from dataclasses import dataclass
from helpers.BoardPosition import BoardPosition


@dataclass(frozen=True)
class Move:
  fromSquare: BoardPosition
  toSquare: BoardPosition

