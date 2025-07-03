from universos.neurona import NeuronaMultiversal

class Viajero:
    def __init__(self, nombre: str, id: int, universo_actual: 'NeuronaMultiversal') -> None:
        self.nombre = nombre
        self.id = id
        self.universo_actual = universo_actual

    def __str__(self):
        return f"Viajero {self.nombre} (ID: {self.id}) en el universo {self.universo}"

    def viajar(self, destino: str):
        print(f"{self.nombre} está viajando al universo {destino}.")