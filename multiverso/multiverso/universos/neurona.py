class NeuronaMultiversal:
    def __init__(self, id: int, nombre: str, tipo: str) -> None:
        self.id = id #Identificador único de la neurona
        self.nombre = nombre #Nombre del universo
        self.tipo = tipo #Tipo temático del universo
        self.conexiones = [None] * 6  # Inicializa con 6 conexiones nulas

    def conectar(self, otra_neurona: 'NeuronaMultiversal', indice: int) -> None:
        if 0 <= indice < 6:
            self.conexiones[indice] = otra_neurona
        else:
            raise IndexError("Índice de conexión fuera de rango")
        
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