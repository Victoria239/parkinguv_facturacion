\# ParkingUV Facturación



Este proyecto implementa un módulo de facturación para ParkingUV S.A.S. aplicando TDD, BDD con Gherkin, pruebas de rendimiento con Locust, análisis básico de seguridad con Bandit y pipeline con GitHub Actions.



\## Reglas de negocio



1\. Los primeros 30 minutos son gratuitos.

2\. A partir del minuto 31 se cobra $500 por cada hora o fracción.

3\. El cobro máximo por día es de $12.000.

4\. Los clientes con membresía VIP tienen 20% de descuento sobre el total antes de aplicar el tope diario.



\## Tecnologías utilizadas



\- Python

\- Pytest

\- Behave

\- Gherkin

\- FastAPI

\- Locust

\- Bandit

\- GitHub Actions



\## Estructura del proyecto



```text

parkinguv-facturacion/

├── src/

│   └── parkinguv/

│       ├── \_\_init\_\_.py

│       ├── tarifas.py

│       └── api.py

├── tests/

│   └── test\_tarifas.py

├── features/

│   ├── calcular\_tarifa.feature

│   └── steps/

│       └── tarifa\_steps.py

├── locustfile.py

├── requirements.txt

├── README.md

├── .gitignore

└── .github/

&#x20;   └── workflows/

&#x20;       └── ci.yml

