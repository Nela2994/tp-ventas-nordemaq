
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_excel(
    "datos/ventas_nordemaq.xlsx",
    sheet_name="Informe de Ventas",
    header=1
)

datos = datos[[
    "Modelo",
    "Venta al Dealer",
    "Actividad"
]]

datos = datos.dropna()

datos["Venta al Dealer"] = pd.to_datetime(
    datos["Venta al Dealer"]
)

datos["Mes"] = datos["Venta al Dealer"].dt.month

ventas_mes = datos.groupby("Mes").size()

plt.figure(figsize=(10,5))

ventas_mes.plot()

plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Cantidad de ventas")

plt.savefig(
    "resultados/grafico_ventas.png"
)

print("Analisis finalizado correctamente")
