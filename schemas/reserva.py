from typing import List

from pydantic import BaseModel
from datetime import datetime, timedelta

from model.reserva import Reserva

class ReservaSchema(BaseModel):
    sala_id: int = 1
    data_reserva: str = "12/07/2023"  # Exemplo de data no formato "dia/mês/ano"
    horario_reserva: str = "10:00"
    duracao_reserva: int = 1

    def to_model(self):
        # Convertendo a data da reserva para o formato datetime
        data_reserva = datetime.strptime(self.data_reserva, "%d/%m/%Y")

        return {
            "sala_id": self.sala_id,
            "data_reserva": data_reserva,
            "horario_reserva": self.horario_reserva,
            "duracao_reserva": self.duracao_reserva
        }

class ListagemReservaSchema(BaseModel):
    sala_id: int = 1
    # data_reserva: datetime
    inicio_reserva: datetime
    fim_reserva: datetime

def apresenta_reservas(reservas: List[Reserva]):
    result = []
    for reserva in reservas:
        h, m = reserva.horario_reserva.split(":")
        hora = int(h)
        minuto = int(m)
        result.append({
            "sala_id": reserva.sala,
            # "data_reserva": reserva.data_reserva,
            # "horario_reserva": reserva.horario_reserva,
            # "duracao_reserva": reserva.duracao_reserva,
            "inicio_reserva": reserva.inicio_reserva,
            "fim_reserva": reserva.fim_reserva,
        })
    return {"reservas": result}
