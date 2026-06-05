from behave import given, when, then
from parkinguv.tarifas import calcular_tarifa


@given("un cliente sin membresía VIP")
def step_cliente_sin_vip(context):
    context.vip = False


@given("un cliente con membresía VIP")
def step_cliente_con_vip(context):
    context.vip = True


@when("el cliente permanece {minutos:d} minutos en el parqueadero")
def step_cliente_permanece_minutos(context, minutos):
    context.tarifa = calcular_tarifa(minutos=minutos, vip=context.vip)


@then("el valor a pagar debe ser {valor:d} pesos")
def step_validar_valor(context, valor):
    assert context.tarifa == valor
