Feature: Cálculo de tarifa de parqueadero
  Como gerente de ParkingUV
  Quiero calcular correctamente la tarifa de parqueo
  Para cobrar a los clientes de acuerdo con las reglas del negocio

  Scenario: Cliente permanece dentro del tiempo gratuito
    Given un cliente sin membresía VIP
    When el cliente permanece 30 minutos en el parqueadero
    Then el valor a pagar debe ser 0 pesos

  Scenario: Cliente paga desde el minuto 31
    Given un cliente sin membresía VIP
    When el cliente permanece 31 minutos en el parqueadero
    Then el valor a pagar debe ser 500 pesos

  Scenario: Cliente paga por hora o fracción
    Given un cliente sin membresía VIP
    When el cliente permanece 91 minutos en el parqueadero
    Then el valor a pagar debe ser 1000 pesos

  Scenario: Cliente no supera el tope diario
    Given un cliente sin membresía VIP
    When el cliente permanece 1440 minutos en el parqueadero
    Then el valor a pagar debe ser 12000 pesos

  Scenario: Cliente VIP recibe descuento
    Given un cliente con membresía VIP
    When el cliente permanece 91 minutos en el parqueadero
    Then el valor a pagar debe ser 800 pesos

  Scenario: Cliente VIP recibe descuento antes del tope diario
    Given un cliente con membresía VIP
    When el cliente permanece 1440 minutos en el parqueadero
    Then el valor a pagar debe ser 9600 pesos