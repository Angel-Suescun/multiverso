
# 🌌 Multiverso Neuronal con Estructuras de Datos

Un proyecto educativo que simula un multiverso con nodos tipo neurona conectados entre sí mediante una estructura personalizada (no basada en grafos tradicionales).  
Cada universo tiene hasta **6 conexiones unidireccionales**, y el usuario puede:

- Visualizar el mapa del multiverso
- Buscar la **ruta más corta** entre dos universos
- Explorar los caminos usando una interfaz gráfica hecha con **Streamlit**

---

## 🧠 Concepto

Este multiverso se construye **usando únicamente estructuras de datos lineales y no lineales propias**, sin importar librerías como `networkx` para lógica. Las conexiones entre universos imitan una red neuronal dispersa.

Cada universo se comporta como una "neurona", y puede tener hasta 6 enlaces unidireccionales. El usuario puede navegar, generar nuevas redes y visualizar caminos entre mundos.

---

## 🔧 Tecnologías y Librerías

- [Python 3.10+](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – interfaz web
- `matplotlib` – visualización del grafo
- `networkx` – solo usado para dibujar el grafo, no para lógica
- `Pillow` – visualización de imágenes

---

## 🚀 ¿Cómo ejecutar la app?

### 📦 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/multiverso.git
cd multiverso
```

### 🧪 2. Instala dependencias

```bash
pip install -r requirements.txt
```

### 🧭 3. Ejecuta localmente

```bash
streamlit run app.py
```

### 🌍 Pagina Web

 [Pagina Web](https://neuronamultiversal.streamlit.app/)

---

## 📁 Estructura del proyecto

```
multiverso/
├── app.py                      ← Interfaz web en Streamlit
├── requirements.txt            ← Librerías necesarias
├── universos/
│   ├── neurona.py              ← Clase Neurona (estructura personalizada)
│   └── generador.py            ← Generación y conexión de universos
├── simulacion/
│   ├── visualizador.py         ← Dibujo del grafo usando matplotlib + networkx
│   ├── ruta_corta.py           ← Búsqueda de ruta más corta sin grafos
│   └── cola.py                 ← Implementación propia de una cola FIFO
├── viajeros/
│   └── viajero.py              ← (Opcional) Motor para viaje automático
```

---

## 🎯 Funcionalidades

- [x] Crear un multiverso con 36 universos únicos
- [x] Establecer enlaces aleatorios (máx. 6 por universo)
- [x] Visualizar el grafo con flechas y nombres
- [x] Buscar ruta más corta entre dos universos usando estructuras propias
- [x] Destacar esa ruta gráficamente (rojo)
- [x] Interacción desde Streamlit sin perder estado

---

## 💡 Créditos

Desarrollado por Angel Suescun como parte del curso de **Estructuras de Datos** – Universidad Nacional de Colombia.

Inspirado en el concepto de redes neuronales y multiversos.



