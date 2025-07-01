from abc import ABC, abstractmethod
import os
import pygame
from Pieces.Settings import PieceType, PieceColor, PieceSize
from Enums.BoardPosition import BoardPosition
from helpers.Moves import Move


class Piece(ABC):
  def __init__(
    self,
    pieceType: PieceType,
    color: PieceColor,
  ):
    self.type = pieceType
    self.color = color
    self.size = PieceSize[pieceType]
    self._loadImage()
    self.moves_history : list[Move] = []

  def _loadImage(self):
    base_path = os.path.join(os.path.dirname(__file__), "../assets")
    filename = f"{self.color.value}-{self.type.value}.png"
    full_path = os.path.join(base_path, filename)
    self.image = pygame.image.load(full_path)

  @abstractmethod
  def isValidMove(self, from_pos: BoardPosition, to_pos: BoardPosition, board: list) -> bool:
    pass

  def isSpecialMove(self, from_pos: BoardPosition, to_pos: BoardPosition, board: list) -> bool:
    return False

  def saveMovent(self, fromMove:BoardPosition, toMove:BoardPosition):
    move = Move(fromMove, toMove)
    self.moves_history.append(move)
