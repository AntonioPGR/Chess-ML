from dataclasses import dataclass
from helpers.ScreenPosition import ScreenPosition


@dataclass(frozen=True)
class BoardPosition:
    row: int
    col: int

    @classmethod
    def fromScreenPosition(cls, screenPosition: ScreenPosition, borderSize: int, squareSize: int) -> "BoardPosition":
        row = (screenPosition.y - borderSize) // squareSize
        col = (screenPosition.x - borderSize) // squareSize
        return cls(row, col)

    @classmethod
    def fromListPosition(cls, pos: int) -> "BoardPosition":
        return BoardPosition(pos // 8, pos % 8)

    def isOnBoard(self) -> bool:
        return 0 <= self.row < 8 and 0 <= self.col < 8

    def toListPosition(self) -> int:
        return self.row * 8 + self.col

    def equals(self, boardFromPos: "BoardPosition"):
        return self.row == boardFromPos.row and self.col == boardFromPos.col

    def isInSameCol(self, boardFromPos: "BoardPosition"):
        return self.col == boardFromPos.col

    def isInSameRow(self, boardFromPos: "BoardPosition"):
        return self.row == boardFromPos.row