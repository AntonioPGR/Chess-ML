
class BoardHelper:
  @staticmethod
  def getPositionFromRowAndColumn(pos: tuple[int, int]) -> int:
    return pos[0] * 8 + pos[1]

  @staticmethod
  def isOnBoard(row: int, col: int) -> bool:
      return 0 <= row < 8 and 0 <= col < 8