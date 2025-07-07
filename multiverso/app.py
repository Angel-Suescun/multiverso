import streamlit as st
from PIL import Image
import os

from universos.generador import generar_universos, conectar_universos
from simulacion.visualizador import graficar_multiverso
from simulacion.ruta_corta import ruta_corta  # Usas esta función, no ruta_mas_corta

# --- Configuración de la página
st.set_page_config(page_title="🌌 Multiverso Neuronal", layout="wide")
st.title("🧠 Multiverso Neuronal con Estructuras de Datos")

# --- Inicialización del estado de sesión
if "universos" not in st.session_state:
    st.session_state.universos = None

if "imagen" not in st.session_state:
    st.session_state.imagen = None

if "ruta" not in st.session_state:
    st.session_state.ruta = None

# --- Botón para generar universos
if st.button("🔄 Generar Multiverso"):
    universos = generar_universos(36)
    conectar_universos(universos)
    st.session_state.universos = universos
    st.session_state.ruta = None
    graficar_multiverso(universos, nombre_archivo="multiverso.png")
    st.session_state.imagen = "multiverso.png"
    st.success("🌌 Multiverso generado exitosamente")

# --- Mostrar imagen actual del multiverso
if st.session_state.imagen and os.path.exists(st.session_state.imagen):
    st.image(Image.open(st.session_state.imagen), caption="🧠 Vista del Multiverso", use_container_width=True)

# --- Buscar ruta más corta
if st.session_state.universos:
    st.header("🧭 Buscar Ruta Más Corta entre Universos")

    ids = list(range(len(st.session_state.universos)))

    origen_id = st.selectbox("Universo origen", ids, format_func=lambda i: st.session_state.universos[i].nombre)
    destino_id = st.selectbox("Universo destino", ids, format_func=lambda i: st.session_state.universos[i].nombre)

    if st.button("🔍 Buscar ruta"):
        origen = st.session_state.universos[origen_id]
        destino = st.session_state.universos[destino_id]
        camino = ruta_corta(origen, destino)

        if camino:
            nombres = [f"{n.nombre} (ID {n.id})" for n in camino]
            st.success(" → ".join(nombres))

            ruta_ids = [n.id for n in camino]
            archivo_ruta = f"ruta_{origen.id}_{destino.id}.png"
            graficar_multiverso(
                st.session_state.universos,
                nombre_archivo=archivo_ruta,
                ruta=ruta_ids
            )
            st.session_state.imagen = archivo_ruta
            st.session_state.ruta = ruta_ids

            # Mostrar imagen con la ruta debajo del texto
            if os.path.exists(archivo_ruta):
                st.image(Image.open(archivo_ruta), caption="🧭 Ruta Visualizada", use_container_width=True)
        else:
            st.error("🚫 No hay ruta entre esos dos universos.")
