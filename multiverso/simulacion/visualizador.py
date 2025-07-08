import matplotlib
matplotlib.use("Agg")

import networkx as nx
import matplotlib.pyplot as plt
import math

def crear_layout_organizado(G):
    """
    Crea un layout organizado en círculos concéntricos basado en la importancia de los nodos.
    """
    nodes = list(G.nodes())
    n_nodes = len(nodes)
    pos = {}
    
    if n_nodes == 0:
        return pos
    
    if n_nodes == 1:
        pos[nodes[0]] = (0, 0)
        return pos
    
    # Calcular centralidad de cada nodo
    try:
        centrality = nx.degree_centrality(G)
    except:
        centrality = {node: 1.0 for node in nodes}
    
    # Ordenar nodos por centralidad (más importante = más central)
    sorted_nodes = sorted(nodes, key=lambda x: centrality[x], reverse=True)
    
    # Dividir en capas concéntricas
    total_nodes = len(sorted_nodes)
    
    if total_nodes <= 6:
        # Para pocos nodos, usar un círculo simple
        for i, node in enumerate(sorted_nodes):
            if i == 0:
                pos[node] = (0, 0)  # El más importante al centro
            else:
                angle = 2 * math.pi * (i-1) / (total_nodes-1)
                radius = 3.0
                pos[node] = (radius * math.cos(angle), radius * math.sin(angle))
    else:
        # Para muchos nodos, usar múltiples capas
        # Capa 1: Centro (1-3 nodos más importantes)
        capa1_size = min(3, max(1, total_nodes // 8))
        # Capa 2: Intermedia (siguiente tercio)
        capa2_size = min(8, max(0, (total_nodes - capa1_size) // 2))
        # Capa 3: Externa (resto)
        capa3_size = total_nodes - capa1_size - capa2_size
        
        current_idx = 0
        
        # CAPA 1 - CENTRO
        for i in range(capa1_size):
            node = sorted_nodes[current_idx]
            if i == 0:
                pos[node] = (0, 0)
            else:
                angle = 2 * math.pi * (i-1) / max(1, capa1_size-1)
                radius = 1.5
                pos[node] = (radius * math.cos(angle), radius * math.sin(angle))
            current_idx += 1
        
        # CAPA 2 - INTERMEDIA
        for i in range(capa2_size):
            node = sorted_nodes[current_idx]
            angle = 2 * math.pi * i / capa2_size
            radius = 4.0
            pos[node] = (radius * math.cos(angle), radius * math.sin(angle))
            current_idx += 1
        
        # CAPA 3 - EXTERNA
        for i in range(capa3_size):
            node = sorted_nodes[current_idx]
            angle = 2 * math.pi * i / capa3_size
            radius = 6.5
            pos[node] = (radius * math.cos(angle), radius * math.sin(angle))
            current_idx += 1
    
    return pos

def graficar_multiverso(universos, nombre_archivo="multiverso.png", ruta=None):
    """
    Genera un gráfico del multiverso con layout organizado en círculos concéntricos.
    Si se proporciona una ruta (lista de IDs), la resalta en rojo.
    """
    G = nx.DiGraph()

    for u in universos:
        G.add_node(u.id, label=u.nombre)

    for u in universos:
        for enlace in u.conexiones:
            if enlace:
                G.add_edge(u.id, enlace.id)

    pos = crear_layout_organizado(G)

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
