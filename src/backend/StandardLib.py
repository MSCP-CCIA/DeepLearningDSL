import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import os


class StandardLib:

    @staticmethod
    def plot(*args):
        """
        Soporta:
        plot(data)              -> Guarda en 'resultado_grafica.png'
        plot(data, "MiGrafica") -> Guarda en 'MiGrafica.png'
        """
        print(f"--- DEBUG: Ejecutando plot ---")

        try:
            plt.figure(figsize=(10, 6))

            # 1. Detectar si el usuario pasó un nombre personalizado al final
            filename = "resultado_grafica"  # Nombre por defecto
            title = "Gráfica DSL"

            data_to_plot = args

            # Si el último argumento es un string, es el nombre del archivo
            if len(args) > 1 and isinstance(args[-1], str):
                filename = args[-1]
                title = args[-1]
                # Eliminamos el nombre de la lista de datos a graficar
                data_to_plot = args[:-1]

            # 2. Graficar los datos restantes
            # Caso simple: plot(lista, "nombre")
            if len(data_to_plot) == 1:
                data = data_to_plot[0]
                if isinstance(data, dict):
                    for k, v in data.items():
                        plt.plot(v, label=k)
                else:
                    # Aplanar si es necesario
                    if isinstance(data, list):
                        data = np.array(data).flatten()
                    plt.plot(data, label='Valor')

            # Caso X vs Y: plot(x, y, "nombre")
            elif len(data_to_plot) == 2:
                plt.plot(data_to_plot[0], data_to_plot[1], label='Datos')

            # Configuración final
            plt.title(title)
            plt.legend()
            plt.grid(True)

            # Guardado
            ruta = os.path.join(os.getcwd(), f"{filename}.png")
            plt.savefig(ruta)
            print(f" ÉXITO: Gráfica guardada en: {filename}.png")
            plt.close()

        except Exception as e:
            print(f" ERROR EN PLOT: {e}")


    @staticmethod
    def read_csv(path):
        try:
            return pd.read_csv(path.replace('"', '')).values
        except:
            return []

    @staticmethod
    def kmeans(data, k):
        kmeans = KMeans(n_clusters=int(k), n_init='auto')
        kmeans.fit(np.array(data))
        return kmeans.labels_

    @staticmethod
    def linear_regression(x, y):
        reg = LinearRegression().fit(np.array(x).reshape(-1, 1), np.array(y))
        return [float(reg.coef_[0]), float(reg.intercept_)]


    @staticmethod
    def write_file(path, content):
        """Escribe texto en un archivo"""
        try:
            path = path.replace('"', '')
            with open(path, 'w') as f:
                f.write(str(content))
            print(f"Archivo guardado: {path}")
        except Exception as e:
            print(f"Error escribiendo archivo: {e}")

    @staticmethod
    def math_op(op_name, data):
        """Operaciones matemáticas vectorizadas (sin, cos, log, sqrt)"""
        data = np.array(data) # Aseguramos que sea numpy array
        if op_name == "sin": return np.sin(data)
        elif op_name == "cos": return np.cos(data)
        elif op_name == "tan": return np.tan(data)
        elif op_name == "log": return np.log(data)
        elif op_name == "sqrt": return np.sqrt(data)
        else: return 0



    @staticmethod
    def slice_data(data, start_col, end_col):
        """
        Corta una matriz para extraer columnas específicas.
        Equivalente a data[:, start:end] en Python.
        """
        try:
            # Aseguramos que sea array de numpy
            data = np.array(data)
            # El slicing de numpy funciona como [filas, columnas]
            # Usamos el operador : para todas las filas
            return data[:, int(start_col):int(end_col)]
        except Exception as e:
            print(f"Error cortando matriz: {e}")
            return []