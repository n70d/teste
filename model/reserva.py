from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from model import Base


class Reserva(Base):
    __tablename__ = 'reserva'

    id = Column(Integer, primary_key=True)
    duracao_reserva = Column(Integer)
    inicio_reserva = Column(DateTime)
    fim_reserva = Column(DateTime)
    sala = Column(Integer, ForeignKey("sala.pk_sala"), nullable=False)

    def __init__(self, duracao_reserva: int = 1, inicio_reserva: Union[DateTime, None] = None, fim_reserva: Union[DateTime, None] = None):
        self.duracao_reserva = duracao_reserva
        self.inicio_reserva = inicio_reserva
        # self.horario_reserva = horario_reserva

        self.fim_reserva = fim_reserva
