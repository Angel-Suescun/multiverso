# main.py

from universos.generador import generar_universos, conectar_universos, mostrar_universos

# Paso 1: Generar 36 universos
universos = generar_universos(36)

# Paso 2: Conectarlos aleatoriamente
conectar_universos(universos)

# Paso 3: Mostrar la red
mostrar_universos(universos)
