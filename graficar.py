import pandas as pd
from matplotlib import pyplot as plt
import os
os.makedirs("generadoss",exist_ok=True)

# Leer archivo Excel
archivo_excel = "datos/ejemplo.xlsx"
contador = 1
contador_barra = 1 
contador_pastel = 1
while contador <= 6:
    
    if contador_barra <= 3:
        data_hoja = pd.read_excel(
        archivo_excel, sheet_name=f"BARRAS{contador_barra}", engine="openpyxl"
        )
        contador_barra = contador_barra + 1
        print(f"Datos leidos de la Hoja{contador}")
        # Graficar datos de la hoja
        eje_x = data_hoja.iloc[:, 0]  # Asumiendo que la primera columna es el eje X
        eje_y_barras = data_hoja.iloc[:, 1]  # Asumiendo que la segunda columna es el eje Y
        # Asumiendo que la tercera columna es el eje Y para el pastel
        eje_y_pastel = data_hoja.iloc[:, 2]
        # Crear la gráfica de barras
        fig, ax = plt.subplots()
        ax.bar(eje_x, eje_y_barras, color="green", label=f"Datos de Hoja {contador}")
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")
        ax.set_xticklabels(eje_x, rotation=45)
        ax.set_title(f"Gráfica de la Hoja {contador}")
        fig.savefig(f"generadoss/grafica_barras_hoja_{contador}.png", bbox_inches="tight")
        plt.close(fig)  # Cerrar la figura para liberar memoria
    else:
       data_hoja = pd.read_excel(
       archivo_excel, sheet_name=f"PASTEL{contador_pastel}", engine="openpyxl"
       )
       contador_pastel = contador_pastel + 1
       eje_x = data_hoja.iloc[:, 0]  # Asumiendo que la primera columna es el eje X
       eje_y_barras = data_hoja.iloc[:, 1]  # Asumiendo que la segunda columna es el eje Y
        # Asumiendo que la tercera columna es el eje Y para el pastel
       eje_y_pastel = data_hoja.iloc[:, 2]
       # codigo para leer el archivo Excel
       # Crear la gráfica de pastel
       fig, ax = plt.subplots()
       ax.pie(
          eje_y_pastel,
          labels=eje_x,
        )
       ax.set_title(f"Gráfica de Pastel de la Hoja {contador}")
       fig.savefig(f"generadoss/grafica_pastel_hoja_{contador}.png", bbox_inches="tight")
       plt.close(fig)  # Cerrar la figura para liberar memoria
       
    # Incrementar el contador
    contador = contador + 1

print("Gráficas generadas y guardadas en la carpeta 'generados'.")