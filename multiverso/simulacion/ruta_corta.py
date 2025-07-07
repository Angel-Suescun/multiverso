from simulacion.cola import Cola
from universos.neurona import NeuronaMultiversal

def ruta_corta(origen: 'NeuronaMultiversal', destino: 'NeuronaMultiversal')-> list:
    cola = Cola()
    visitado = []
    padres = {}

    cola.push(origen)
    visitado.append(origen)

    while not cola.is_empty():
        actual = cola.pop()
        if actual == destino:
            # reconstruir camino desde destino hacia origen
            camino = [actual]
            while actual in padres:
                actual = padres[actual]
                camino.insert(0, actual)
            return camino

        for vecino in actual.conexiones:
            if vecino and vecino not in visitado:
                padres[vecino] = actual
                visitado.append(vecino)
                cola.push(vecino)

    return None  # No hay camino
