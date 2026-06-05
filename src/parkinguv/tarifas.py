import math


def calcular_tarifa(minutos: int, vip: bool = False) -> int:
    if minutos <= 30:
        return 0

    minutos_cobrables = minutos - 30
    horas_o_fraccion = math.ceil(minutos_cobrables / 60)

    return horas_o_fraccion * 500
