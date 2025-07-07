import streamlit as st
from PIL import Image
import os

from universos.generador import (
    generar_universos,
    conectar_universos,
    agregar_universo,
    eliminar_universo,
)
from simulacion.visualizador import graficar_multiverso
from simulacion.ruta_corta import ruta_corta

st.set_page_config(page_title="🌌 Multiverso Neuronal", layout="wide")
st.title("🧠 Multiverso Neuronal con Estructuras de Datos")

# --- Estados iniciales
if "universos" not in st.session_state:
    st.session_state.universos = None

if "imagen" not in st.session_state:
    st.session_state.imagen = None

if "ruta" not in st.session_state:
    st.session_state.ruta = None

# --- Generar multiverso
if st.button("🔄 Generar Multiverso"):
    universos = generar_universos(36)
    conectar_universos(universos)
    st.session_state.universos = universos
    st.session_state.ruta = None
    graficar_multiverso(universos, nombre_archivo="multiverso.png")
    st.session_state.imagen = "multiverso.png"
    st.success("🌌 Multiverso generado exitosamente")
    st.image(Image.open("multiverso.png"), caption="🧠 Multiverso generado", use_container_width=True)

# --- Mostrar imagen persistente
if st.session_state.imagen and os.path.exists(st.session_state.imagen):
    st.image(Image.open(st.session_state.imagen), caption="🧠 Vista actual del Multiverso", use_container_width=True)

# --- Si ya hay universos creados
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
            if os.path.exists(archivo_ruta):
                st.image(Image.open(archivo_ruta), caption="🧭 Ruta Visualizada", use_container_width=True)
        else:
            st.error("🚫 No hay ruta entre esos dos universos.")

    # --- Agregar universo
    st.header("➕ Agregar un nuevo universo")
    nuevo_nombre = st.text_input("Nombre del nuevo universo", value="Nuevo Universo")
    if st.button("Agregar universo"):
        agregar_universo(st.session_state.universos, nuevo_nombre)
        graficar_multiverso(st.session_state.universos, nombre_archivo="multiverso.png")
        st.session_state.imagen = "multiverso.png"
        st.success(f"Universo '{nuevo_nombre}' agregado.")
        st.image(Image.open("multiverso.png"), caption="🧠 Multiverso actualizado", use_container_width=True)

    # --- Eliminar universo
    st.header("➖ Eliminar un universo")
    opciones_ids = [u.id for u in st.session_state.universos]
    if opciones_ids:
        eliminar_id = st.selectbox("Selecciona el ID del universo a eliminar", opciones_ids)
        if st.button("Eliminar universo"):
            eliminar_universo(st.session_state.universos, eliminar_id)
            graficar_multiverso(st.session_state.universos, nombre_archivo="multiverso.png")
            st.session_state.imagen = "multiverso.png"
            st.success(f"Universo con ID {eliminar_id} eliminado.")
            st.image(Image.open("multiverso.png"), caption="🧠 Multiverso actualizado", use_container_width=True)
