from universos.neurona import NeuronaMultiversal

class Viajero:
    def __init__(self, nombre: str, id: int, universo_actual: 'NeuronaMultiversal') -> None:
        self.nombre = nombre
        self.id = id
        self.universo_actual = universo_actual
        self.historial = [universo_actual]

    def mover(self, salida: int) -> None:
        if 0 <= salida < 6:
            destino = self.universo_actual.conexiones[salida]
            if destino:
                print(f"{self.nombre} viaja de {self.universo_actual.nombre} a {destino.nombre} (vía salida {salida})")
                self.universo_actual = destino
                self.historial.append(destino)
            else:
                print(f"✖ {self.nombre} no puede viajar por la salida {salida}: está vacía.")
        else:
            print(f"✖ {self.nombre} no puede viajar por la salida {salida}: no existe.")

    def mostrar_historial(self) -> None:
        print(f"Historial de {self.nombre}:")
        for i, universo in enumerate(self.historial):
            print(f"{i + 1}. {universo.nombre} (ID: {universo.id})")
        print(f"Total de universos visitados: {len(self.historial)}")