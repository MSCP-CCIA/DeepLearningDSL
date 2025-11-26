import pandas as pd
import numpy as np

# Simulamos el famoso dataset IRIS (Datos de flores)
# 4 columnas de datos (Largo/Ancho de pétalos/sépalos)
X = np.random.rand(100, 4)
# 1 columna de target (0 o 1)
y = np.random.randint(0, 2, 100)

df = pd.DataFrame(X, columns=["f1", "f2", "f3", "f4"])
df["target"] = y

df.to_csv("iris_dataset.csv", index=False)
print("✅ Archivo 'iris_dataset.csv' generado con éxito.")