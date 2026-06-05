from locust import HttpUser, task, between


class ClienteParkingUV(HttpUser):
    wait_time = between(1, 3)

    @task
    def calcular_tarifa_cliente_normal(self):
        with self.client.post(
            "/calcular-tarifa",
            json={
                "minutos": 91,
                "vip": False
            },
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure("La API no respondió correctamente")
                return

            total = response.json().get("total")

            if total != 1000:
                response.failure(f"Tarifa incorrecta. Esperado 1000, obtenido {total}")

    @task
    def calcular_tarifa_cliente_vip(self):
        with self.client.post(
            "/calcular-tarifa",
            json={
                "minutos": 91,
                "vip": True
            },
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure("La API no respondió correctamente")
                return

            total = response.json().get("total")

            if total != 800:
                response.failure(f"Tarifa incorrecta. Esperado 800, obtenido {total}")
