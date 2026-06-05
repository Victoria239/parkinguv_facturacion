import pytest
from parkinguv.tarifas import calcular_tarifa


def test_primeros_30_minutos_son_gratis():
    tarifa = calcular_tarifa(minutos=30, vip=False)

    assert tarifa == 0
