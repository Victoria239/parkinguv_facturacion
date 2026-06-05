def calcular_tarifa(minutos: int, vip: bool = False) -> int:
    if minutos <= 30:
        return 0

    return 500
