#!/usr/bin/env python3
"""Script de prueba para verificar las conexiones al agregar universos"""

from universos.generador import generar_universos, conectar_universos, agregar_universo, mostrar_universos

def test_agregar_universo():
    print("=== PRUEBA: Agregar universo ===\n")
    
    # Crear un multiverso pequeño para prueba
    universos = generar_universos(5)
    conectar_universos(universos)
    
    print("ANTES de agregar:")
    mostrar_universos(universos)
    print("\n" + "="*50 + "\n")
    
    # Agregar un nuevo universo
    print("Agregando 'Universo Test'...")
    agregar_universo(universos, "Universo Test")
    
    print("\nDESPUÉS de agregar:")
    mostrar_universos(universos)
    
    # Verificar que el nuevo universo tenga conexiones
    nuevo_universo = universos[-1]  # El último agregado
    print(f"\n🔍 VERIFICACIÓN del nuevo universo '{nuevo_universo.nombre}':")
    print(f"  - ID: {nuevo_universo.id}")
    print(f"  - Entradas: {nuevo_universo.entradas}")
    print(f"  - Salidas: {sum(1 for c in nuevo_universo.conexiones if c is not None)}")
    print(f"  - Conexiones salida: {nuevo_universo.obtener_conexion()}")
    
    # Verificar conexiones entrantes
    conexiones_entrantes = []
    for u in universos[:-1]:  # Todos excepto el nuevo
        for i, conexion in enumerate(u.conexiones):
            if conexion and conexion.id == nuevo_universo.id:
                conexiones_entrantes.append(f"{u.nombre} -> {nuevo_universo.nombre}")
    
    print(f"  - Conexiones entrantes: {conexiones_entrantes}")
    
    if nuevo_universo.entradas == 0 and sum(1 for c in nuevo_universo.conexiones if c is not None) == 0:
        print("❌ ERROR: El nuevo universo NO tiene conexiones!")
    else:
        print("✅ OK: El nuevo universo tiene conexiones.")

if __name__ == "__main__":
    test_agregar_universo()
