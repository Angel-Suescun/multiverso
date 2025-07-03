import random
from universos.neurona import NeuronaMultiversal

TIPOS_UNIVERSOS = ["caos", "tiempo", "vacío", "orden", "fractal", "mecánico",
    "luz", "oscuridad", "biológico", "cuántico", "dimensional", "memético"
]

def generar_universos(cantidad: int) -> list[NeuronaMultiversal]:
    if cantidad <= 0 and cantidad < 36:
        raise ValueError(
            "La cantidad de universos debe ser un número positivo y mayor a 36."
            )
    universos = []
    for i in range(cantidad):
        nombre = f"Universo {i}"    
        tipo = random.choice(TIPOS_UNIVERSOS)
        universo = NeuronaMultiversal(i, nombre, tipo)
        universos.append(universo)
    return universos

def conectar_universos(universos: list[NeuronaMultiversal]) -> None:

    total = len(universos)
    for universo in universos:
        posibles_conexiones = [u for u in universos if u.id != universo.id]
        random.shuffle(posibles_conexiones)
        conexiones_realizadas = 0

        for i in range(6):  # Intentar conectar hasta 6 veces
            if conexiones_realizadas >= 6:
                break
            if universo.conexiones[i] is None:
                for candidato in posibles_conexiones:
                    if candidato not in universo.conexiones:
                        universo.conectar(candidato, i)
                        conexiones_realizadas += 1
                        break

def mostrar_universos(universos: list[NeuronaMultiversal]) -> None:
    for universo in universos:
        universo.mostrar_conexiones()
        print(f"Conexiones: {universo.obtener_conexion()}\n")
        print(f"Dirección en memoria de {universo.nombre}: {hex(id(universo))}\n")
