import math


TARIFA_HORA_O_FRACCION = 500
MINUTOS_GRATIS = 30
TOPE_DIARIO = 12000
DESCUENTO_VIP = 0.20


def calcular_tarifa(minutos: int, vip: bool = False) -> int:
    if minutos < 0:
        raise ValueError("Los minutos no pueden ser negativos")

    if minutos <= MINUTOS_GRATIS:
        return 0

    minutos_cobrables = minutos - MINUTOS_GRATIS
    horas_o_fraccion = math.ceil(minutos_cobrables / 60)
    total = horas_o_fraccion * TARIFA_HORA_O_FRACCION

    if vip:
        total = total * (1 - DESCUENTO_VIP)

    if total > TOPE_DIARIO:
        total = TOPE_DIARIO

    return int(total)
