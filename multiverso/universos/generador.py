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

def conectar_universos(universos: list) -> None:
    random.seed()  # Asegura aleatoriedad
    n = len(universos)

    # Inicialmente todos sin conexiones
    for u in universos:
        u.conexiones = [None] * 6
        u.entradas = 0

    # Paso 1: asegurar 1 salida aleatoria por neurona
    for origen in universos:
        # Verificar que el origen tenga espacio para conexiones totales
        total_origen = origen.entradas + sum(1 for c in origen.conexiones if c)
        if total_origen >= 6:
            continue
            
        posibles_destinos = [u for u in universos if u != origen]
        # Filtrar destinos que tengan espacio para conexiones totales
        posibles_destinos = [u for u in posibles_destinos 
                            if (u.entradas + sum(1 for c in u.conexiones if c)) < 6]
        if not posibles_destinos:
            continue

        destino = random.choice(posibles_destinos)

        for i in range(6):
            if origen.conexiones[i] is None:
                origen.conectar(destino, i)
                break

    # Paso 2: agregar entre 0 y 4 conexiones aleatorias adicionales por nodo
    for origen in universos:
        num_salidas_deseadas = random.randint(1, 5)
        conexiones_actuales = sum(1 for c in origen.conexiones if c)
        restantes = num_salidas_deseadas - conexiones_actuales

        intentos = 100
        while restantes > 0 and intentos > 0:
            # Verificar que el origen tenga espacio para conexiones totales
            total_origen = origen.entradas + sum(1 for c in origen.conexiones if c)
            if total_origen >= 6:
                break
                
            destino = random.choice(universos)
            if destino == origen or destino in origen.conexiones:
                intentos -= 1
                continue
                
            # Verificar que el destino tenga espacio para conexiones totales
            total_destino = destino.entradas + sum(1 for c in destino.conexiones if c)
            if total_destino >= 6:
                intentos -= 1
                continue

            for i in range(6):
                if origen.conexiones[i] is None:
                    origen.conectar(destino, i)
                    restantes -= 1
                    break
            intentos -= 1

    # Verificación: todos con al menos una entrada
    for u in universos:
        if u.entradas == 0:
            # Buscar orígenes que tengan espacio para conexiones totales
            posibles_origenes = [o for o in universos if o != u and u not in o.conexiones]
            posibles_origenes = [o for o in posibles_origenes 
                               if (o.entradas + sum(1 for c in o.conexiones if c)) < 6]
            if posibles_origenes:
                origen = random.choice(posibles_origenes)
                for i in range(6):
                    if origen.conexiones[i] is None:
                        origen.conectar(u, i)
                        break

def mostrar_universos(universos: list[NeuronaMultiversal]) -> None:
    for universo in universos:
        universo.mostrar_conexiones()
        print(f"Conexiones: {universo.obtener_conexion()}\n")
        print(f"Dirección en memoria de {universo.nombre}: {hex(id(universo))}\n")


def agregar_universo(universos, nombre):
    nuevo_id = max([u.id for u in universos]) + 1 if universos else 0
    nueva = NeuronaMultiversal(id=nuevo_id, nombre=nombre, tipo=random.choice(TIPOS_UNIVERSOS))
    
    # Inicializar conexiones del nuevo universo
    nueva.conexiones = [None] * 6
    nueva.entradas = 0

    # 1. SALIDAS: conectar el nuevo universo hacia otros (1-3 salidas)
    posibles_destinos = [u for u in universos 
                        if (u.entradas + sum(1 for c in u.conexiones if c)) < 6]
    random.shuffle(posibles_destinos)

    num_salidas = random.randint(1, min(3, len(posibles_destinos)))
    conexiones_salida = 0
    
    for destino in posibles_destinos:
        if conexiones_salida >= num_salidas:
            break
        
        # Verificar límites totales antes de conectar
        total_nueva = nueva.entradas + sum(1 for c in nueva.conexiones if c is not None)
        total_destino = destino.entradas + sum(1 for c in destino.conexiones if c)
        
        if total_nueva >= 6 or total_destino >= 6:
            continue
            
        # Buscar un slot libre en el nuevo universo
        for i in range(6):
            if nueva.conexiones[i] is None:
                nueva.conectar(destino, i)
                conexiones_salida += 1
                break

    # 2. ENTRADAS: conectar otros universos hacia él (al menos 1)
    posibles_origenes = [u for u in universos 
                        if (u.entradas + sum(1 for c in u.conexiones if c)) < 6]
    random.shuffle(posibles_origenes)

    conexiones_entrantes = 0
    min_entradas = 1  # Garantizar al menos 1 entrada
    
    for origen in posibles_origenes:
        # Verificar límites totales antes de conectar
        total_nueva = nueva.entradas + sum(1 for c in nueva.conexiones if c is not None)
        total_origen = origen.entradas + sum(1 for c in origen.conexiones if c is not None)
        
        if total_nueva >= 6 or total_origen >= 6 or conexiones_entrantes >= min_entradas:
            break
            
        # Buscar un slot libre en el universo origen
        for i in range(6):
            if origen.conexiones[i] is None:
                origen.conectar(nueva, i)
                conexiones_entrantes += 1
                break

    # 3. Agregar a la lista
    universos.append(nueva)


def eliminar_universo(universos, id_eliminar):
    objetivo = next((u for u in universos if u.id == id_eliminar), None)
    if not objetivo:
        return

    # Quitar todas las conexiones hacia él
    for u in universos:
        for i in range(6):
            if u.conexiones[i] is not None and u.conexiones[i].id == id_eliminar:
                u.conexiones[i] = None
                objetivo.entradas -= 1

    # Eliminar el universo
    universos.remove(objetivo)
