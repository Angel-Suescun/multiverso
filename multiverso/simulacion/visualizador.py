import matplotlib
matplotlib.use("Agg")

import networkx as nx
import matplotlib.pyplot as plt

def graficar_multiverso(universos, nombre_archivo="multiverso.png", ruta=None):
    """
    Genera un gráfico del multiverso con flechas visibles fuera de los nodos.
    Si se proporciona una ruta (lista de IDs), la resalta en rojo.
    """
    G = nx.DiGraph()

    for u in universos:
        G.add_node(u.id, label=u.nombre)

    for u in universos:
        for enlace in u.conexiones:
            if enlace:
                G.add_edge(u.id, enlace.id)

    pos = nx.spring_layout(G, seed=42, k=2.0, iterations=100)

    plt.figure(figsize=(18, 14))

    # NODOS
    nx.draw_networkx_nodes(
        G, pos,
        node_size=1200,
        node_color='skyblue',
        edgecolors='black'
    )

    # TODAS LAS ARISTAS (grises por defecto)
    nx.draw_networkx_edges(
        G, pos,
        edge_color='gray',
        arrows=True,
        arrowstyle='-|>',
        arrowsize=25,
        connectionstyle='arc3,rad=0.15'
    )

    # ETIQUETAS
    labels = {u.id: u.nombre for u in universos}
    nx.draw_networkx_labels(G, pos, labels, font_size=10, font_weight='bold')

    # 🔴 RUTA DESTACADA
    if ruta and len(ruta) > 1:
        ruta_edges = [(ruta[i], ruta[i+1]) for i in range(len(ruta)-1)]
        nx.draw_networkx_edges(
            G, pos,
            edgelist=ruta_edges,
            edge_color='red',
            arrows=True,
            arrowstyle='-|>',
            arrowsize=35,
            width=3,
            connectionstyle='arc3,rad=0.25'
        )

    plt.title("🌌 Mapa Visual del Multiverso", fontsize=18)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(nombre_archivo, dpi=300)
    plt.close()

    print(f"✅ Mapa visual guardado como '{nombre_archivo}'")
