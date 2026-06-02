import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("resultados.csv")

# Quitar filas con COLAPSO para que las gráficas funcionen
df = df[df["Assign"] != "COLAPSO"]

# Convertir columnas numéricas
columnas = ["N", "Assign", "Lookup", "Print", "Unassign", "Done", "Memoria"]
for col in columnas:
    df[col] = pd.to_numeric(df[col])

operaciones = ["Assign", "Lookup", "Unassign", "Print", "Memoria"]

for operacion in operaciones:
    for tipo in df["Tipo"].unique():
        datos = df[df["Tipo"] == tipo]

        plt.figure(figsize=(10, 6))

        for estructura in datos["Estructura"].unique():
            sub = datos[datos["Estructura"] == estructura]
            plt.plot(sub["N"], sub[operacion], marker="o", label=estructura)

        plt.xlabel("Cantidad de elementos (N)")

        if operacion == "Memoria":
            plt.ylabel("Memoria utilizada (MB)")
            plt.title(f"Uso de memoria - Datos {tipo}")
            nombre_archivo = f"grafico_memoria_{tipo}.png"
        else:
            plt.ylabel("Tiempo promedio (segundos)")
            plt.title(f"Tiempo de {operacion} - Datos {tipo}")
            nombre_archivo = f"grafico_{operacion.lower()}_{tipo}.png"

        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(nombre_archivo)
        plt.close()

print("Gráficos generados correctamente.")