import math


TARIFA_HORA_O_FRACCION = 500
MINUTOS_GRATIS = 30
TOPE_DIARIO = 12000
DESCUENTO_VIP = 0.20


def calcular_tarifa(minutos: int, vip: bool = False) -> int:
    _validar_minutos(minutos)

    if minutos <= MINUTOS_GRATIS:
        return 0

    total = _calcular_total_sin_descuento(minutos)

    if vip:
        total = _aplicar_descuento_vip(total)

    total = _aplicar_tope_diario(total)

    return int(total)


def _validar_minutos(minutos: int) -> None:
    if minutos < 0:
        raise ValueError("Los minutos no pueden ser negativos")


def _calcular_total_sin_descuento(minutos: int) -> int:
    minutos_cobrables = minutos - MINUTOS_GRATIS
    horas_o_fraccion = math.ceil(minutos_cobrables / 60)

    return horas_o_fraccion * TARIFA_HORA_O_FRACCION


def _aplicar_descuento_vip(total: float) -> float:
    return total * (1 - DESCUENTO_VIP)


def _aplicar_tope_diario(total: float) -> float:
    return min(total, TOPE_DIARIO)
