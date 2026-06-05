import pytest
from parkinguv.tarifas import calcular_tarifa


def test_primeros_30_minutos_son_gratis():
    tarifa = calcular_tarifa(minutos=30, vip=False)

    assert tarifa == 0


def test_minuto_31_cobra_una_hora():
    tarifa = calcular_tarifa(minutos=31, vip=False)

    assert tarifa == 500


def test_90_minutos_cobra_una_hora_o_fraccion():
    tarifa = calcular_tarifa(minutos=90, vip=False)

    assert tarifa == 500


def test_91_minutos_cobra_dos_horas_o_fraccion():
    tarifa = calcular_tarifa(minutos=91, vip=False)

    assert tarifa == 1000


def test_tarifa_maxima_diaria_es_12000():
    tarifa = calcular_tarifa(minutos=1440, vip=False)

    assert tarifa == 12000


def test_tarifa_no_supera_tope_diario():
    tarifa = calcular_tarifa(minutos=2000, vip=False)

    assert tarifa == 12000
