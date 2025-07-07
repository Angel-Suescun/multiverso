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
    n = len(universos)
    # Paso 1: asegurar al menos una salida y entrada por neurona
    for i in range(n):
        origen = universos[i]
        posibles_destinos = [u for u in universos if u != origen and u.entradas < 6]

        if not posibles_destinos:
            continue  # ya no hay destino posible

        destino = random.choice(posibles_destinos)

        # Buscar índice libre de salida en origen
        for idx in range(6):
            if origen.conexiones[idx] is None:
                origen.conectar(destino, idx)
                break

    # Paso 2: conexiones adicionales aleatorias sin violar la regla de 6 conexiones por nodo
    intentos = 10000
    while intentos > 0:
        a = random.choice(universos)
        b = random.choice(universos)
        if a == b:
            intentos -= 1
            continue

        # Condición: que ambos tengan espacio y no se conecten entre sí ya
        if sum(1 for e in a.conexiones if e) >= 6 or b.entradas >= 6:
            intentos -= 1
            continue

        # No repetir conexiones
        if b in a.conexiones:
            intentos -= 1
            continue

        # Buscar índice libre en 'a'
        for i in range(6):
            if a.conexiones[i] is None:
                a.conectar(b, i)
                break

        intentos -= 1

    # Verificación final: todos tienen al menos una entrada y una salida
    for u in universos:
        if u.entradas == 0:
            print(f"⚠ {u.nombre} no tiene entradas")
        if all(e is None for e in u.conexiones):
            print(f"⚠ {u.nombre} no tiene salidas")

def mostrar_universos(universos: list[NeuronaMultiversal]) -> None:
    for universo in universos:
        universo.mostrar_conexiones()
        print(f"Conexiones: {universo.obtener_conexion()}\n")
        print(f"Dirección en memoria de {universo.nombre}: {hex(id(universo))}\n")
