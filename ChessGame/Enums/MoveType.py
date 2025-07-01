from enum import Enum


class MoveType(Enum):
  NORMAL = "normal"
  CASTLE = "castle"
  EN_PASSANT = "enpassant"
  PROMOTION = "promotion"