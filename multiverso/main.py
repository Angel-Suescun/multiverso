# main.py

from universos.generador import generar_universos, conectar_universos
from viajeros.viajero import Viajero
from simulacion.visualizador import graficar_multiverso
from simulacion.ruta_corta import ruta_corta

def mostrar_opciones(universo):
    print(f"\nEstás en {universo.nombre} ({universo.tipo})")
    print("Salidas disponibles:")
    for i, enlace in enumerate(universo.conexiones):
        if enlace:
            print(f" [{i}] -> {enlace.nombre} ({enlace.tipo})")
        else:
            print(f" [{i}] -> [Vacío]")

def main():
    # 🌌 Generar y conectar universos
    universos = generar_universos(36)
    conectar_universos(universos)

    print("Bienvenido al Multiverso Neuronal. Navega por los universos.\n")
    
    # 🚶 Crear viajero
    viajero = Viajero("Explorador", 5, universos[0])

    while True:
        mostrar_opciones(viajero.universo_actual)
        comando = input("Elige salida (0-5), 'ruta' para buscar ruta más corta, o 'q' para salir: ").strip()

        if comando.lower() == 'q':
            print("¡Hasta la próxima!")
            break

        if comando.lower() == 'ruta':
            try:
                origen_id = int(input("ID del universo origen (0-35): "))
                destino_id = int(input("ID del universo destino (0-35): "))
                origen = universos[origen_id]
                destino = universos[destino_id]
                camino = ruta_corta(origen, destino)

                if camino:
                    print("\n✅ Ruta más corta encontrada:")
                    for u in camino:
                        print(f"{u.nombre} (ID {u.id})")

                    ids_ruta = [u.id for u in camino]
                    nombre_archivo = f"ruta_{origen.id}_{destino.id}.png"
                    graficar_multiverso(universos, nombre_archivo=nombre_archivo, ruta=ids_ruta)
                else:
                    print("🚫 No hay ruta entre esos universos.")
            except Exception as e:
                print("⚠️ Entrada inválida o error:", e)
            continue

        if comando.isdigit():
            salida = int(comando)
            viajero.mover(salida)
        else:
            print("Entrada inválida. Intenta de nuevo.")

        print("\nRuta actual del viajero:")
        viajero.mostrar_historial()

    # 🖼️ Graficar al final el multiverso completo
    graficar_multiverso(universos, nombre_archivo="multiverso.png")

if __name__ == "__main__":
    main()
