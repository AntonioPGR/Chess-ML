from dataclasses import dataclass

@dataclass(frozen=True)
class ScreenPosition:
    x: int
    y: int

    @classmethod
    def fromTuple(cls, pos: tuple[int, int]) -> "ScreenPosition":
      return cls(pos[0], pos[1])

    @classmethod
    def fromNumbers(cls, x:int, y:int) -> "ScreenPosition":
      return cls(x, y)
