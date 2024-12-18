import streamlit as st 
import pandas as pd

def generar_estadisticas(df):
    """
    Genera Estadísticas descriptivas de un dataframe
    """
    return df.describe()

def exportar_excel(df):
    """
    Exporta un dataframe a un archivo excel
    """

    with open("estadisticas_descriptivas.xlsx", "wb") as archivo:
        df.to_excel(archivo, index=False, sheet_name = "Estadísticas")
    
    return "estadisticas_descriptivas.xlsx"

st.title("Analizador de Archivos Excel o CSV")

archivo_subido = st.file_uploader("Sube tu archivo excel o csv", type = ["xlsx", "xls", "csv"])

if archivo_subido is not None:

    st.write("El archivo ha sido cargado")

    if archivo_subido.name.endswith("csv"):
        df = pd.read_csv(archivo_subido)

    else:
        df = pd.read_excel(archivo_subido)

    st.write(" ### DataFrame Original")
    st.dataframe(df)

    df_estadisticas = generar_estadisticas(df)
    st.dataframe(df_estadisticas)

    ruta_archivo = exportar_excel(df_estadisticas)

    with open(ruta_archivo, "rb") as archivo:

        st.download_button (
            label= "Descargar Esdatisticas en Excel",
            data= archivo,
            file_name = "estadisticas_descriptivas.xlsx",
            mime= "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

else: 
    st.write("Por favor cargar el archivo")
