from datetime import timedelta
from sqlalchemy import and_, or_

from model import Reserva, Session


def verificar_conflito_reserva(sala_id, inicio_reserva, fim_reserva):
    session = Session()
    conflito = session.query(Reserva).filter(
        Reserva.sala == sala_id,
        or_(
            and_(Reserva.inicio_reserva >= inicio_reserva, Reserva.inicio_reserva < fim_reserva),
            and_(Reserva.fim_reserva > inicio_reserva, Reserva.fim_reserva <= fim_reserva),
            and_(Reserva.inicio_reserva <= inicio_reserva, Reserva.fim_reserva >= fim_reserva)
        )
    ).first()

    return conflito

