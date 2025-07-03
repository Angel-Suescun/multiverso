# simulacion/visualizador.py

import matplotlib
matplotlib.use("Agg")  # Usamos un backend que no requiere interfaz gráfica

import networkx as nx
import matplotlib.pyplot as plt

def graficar_multiverso(universos, nombre_archivo="multiverso.png"):
    """
    Genera un gráfico del multiverso como una red dirigida y lo guarda como imagen PNG.
    """
    G = nx.DiGraph()

    # Añadir nodos
    for u in universos:
        G.add_node(u.id, label=u.nombre)

    # Añadir conexiones
    for u in universos:
        for enlace in u.conexiones:
            if enlace:
                G.add_edge(u.id, enlace.id)

    # Calcular posiciones
    pos = nx.spring_layout(G, seed=42)

    # Dibujar nodos
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')

    # Dibujar aristas
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)

    # Dibujar etiquetas
    labels = {u.id: u.nombre for u in universos}
    nx.draw_networkx_labels(G, pos, labels, font_size=9)

    # Ajustes finales
    plt.title("Mapa Visual del Multiverso")
    plt.axis('off')

    # Guardar imagen
    plt.savefig(nombre_archivo, dpi=300)
    print(f"✅ Mapa del multiverso guardado como '{nombre_archivo}'")
