class NeuronaMultiversal:
    def __init__(self, id: int, nombre: str, tipo: str) -> None:
        self.id = id #Identificador único de la neurona
        self.nombre = nombre #Nombre del universo
        self.tipo = tipo #Tipo temático del universo
        self.conexiones = [None] * 6  # Inicializa con 6 conexiones nulas
        self.entradas = 0

    def conectar(self, otra_neurona: 'NeuronaMultiversal', indice: int) -> None:
        if not (0 <= indice < 6):
            print(f"Índice de conexión inválido en {self.nombre}.")
            return

        if self.conexiones[indice] is not None:
            print(f"{self.nombre} ya tiene una conexión en la salida {indice}.")
            return

        # Verificar límites: máximo 6 conexiones totales (entradas + salidas) por neurona
        salidas_origen = sum(1 for e in self.conexiones if e)
        total_origen = self.entradas + salidas_origen
        
        salidas_destino = sum(1 for e in otra_neurona.conexiones if e)
        total_destino = otra_neurona.entradas + salidas_destino
        
        if total_origen >= 6:
            print(f"{self.nombre} ya tiene el máximo de conexiones totales (6).")
            return

        if total_destino >= 6:
            print(f"{otra_neurona.nombre} ya tiene el máximo de conexiones totales (6).")
            return

        # Conectar
        self.conexiones[indice] = otra_neurona
        otra_neurona.entradas += 1

        
    def mostrar_conexiones(self)-> None:
        print(f"Universo: {self.nombre} (ID: {self.id}, Tipo: {self.tipo})")
        for i, conexion in enumerate(self.conexiones):
            if conexion:
                print(
                    f"  ↳ Salida {i}: Universo {conexion.id} - {conexion.nombre}({conexion.tipo})"
                    )
            else:
                print(f"  ↳ Salida {i}: Sin conexión")
    
    def obtener_conexion(self) -> list:
        """Devuelve una lista de IDs de las neuronas conectadas."""
        return [n.id for n in self.conexiones if n is not None]