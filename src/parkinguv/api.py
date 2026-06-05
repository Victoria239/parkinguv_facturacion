from fastapi import FastAPI
from pydantic import BaseModel

from parkinguv.tarifas import calcular_tarifa


app = FastAPI(title="ParkingUV Facturación")


class SolicitudTarifa(BaseModel):
    minutos: int
    vip: bool = False


@app.post("/calcular-tarifa")
def calcular_tarifa_endpoint(solicitud: SolicitudTarifa):
    total = calcular_tarifa(
        minutos=solicitud.minutos,
        vip=solicitud.vip
    )

    return {
        "minutos": solicitud.minutos,
        "vip": solicitud.vip,
        "total": total
    }
