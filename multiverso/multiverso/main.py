# main.py

from universos.generador import generar_universos, conectar_universos
from viajeros.viajero import Viajero
from simulacion.visualizador import graficar_multiverso

def mostrar_opciones(universo):
    print(f"\nEstás en {universo.nombre} ({universo.tipo})")
    print("Salidas disponibles:")
    for i, enlace in enumerate(universo.conexiones):
        if enlace:
            print(f" [{i}] -> {enlace.nombre} ({enlace.tipo})")
        else:
            print(f" [{i}] -> [Vacío]")

def main():
    # Generar y conectar universos
    universos = generar_universos(36)
    conectar_universos(universos)
    print(universos[0])  # Mostrar el primer universo para verificar
    # Crear viajero
    viajero = Viajero("Explorador", 5 ,universos[0])

    print("Bienvenido al Multiverso Neuronal. Navega por los universos.\n")

    while True:
        mostrar_opciones(viajero.universo_actual)
        comando = input("Elige salida (0-5) o 'q' para salir: ").strip()

        if comando.lower() == 'q':
            print("¡Hasta la próxima!")
            break

        if comando.isdigit():
            salida = int(comando)
            viajero.mover(salida)
        else:
            print("Entrada inválida. Intenta de nuevo.")

        print("\nRuta actual del viajero:")
        viajero.mostrar_historial()
    
    graficar_multiverso(universos)

if __name__ == "__main__":
    main()
    

# Después de generar y conectar universos...


