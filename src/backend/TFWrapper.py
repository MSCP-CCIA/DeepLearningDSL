import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


import tensorflow as tf
import numpy as np


class TFWrapper:
    def __init__(self):
        self.model = tf.keras.models.Sequential()

    def add(self, layer_type, units, activation):
        if layer_type == "Dense":
            self.model.add(tf.keras.layers.Dense(int(units), activation=activation))
        else:
            print(f"Error: Capa '{layer_type}' no soportada aún.")

    def compile(self, optimizer, loss, metrics=None):
        # Convertimos métricas de NumPy a lista de Python si es necesario
        if metrics is not None:
            if isinstance(metrics, np.ndarray):
                metrics = metrics.tolist()

        self.model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    def fit(self, x_train, y_train, epochs):
        x_train = np.array(x_train)
        y_train = np.array(y_train)

        print(f"--- Iniciando entrenamiento ({epochs} épocas) ---")
        # verbose=0 asegura que la barra de progreso de Keras tampoco ensucie
        history = self.model.fit(x_train, y_train, epochs=int(epochs), verbose=0)
        print("--- Entrenamiento finalizado ---")

        return history.history

    def predict(self, x_input):
        x_input = np.array(x_input)
        return np.round(self.model.predict(x_input, verbose=0))


    def get_estimated_size(self):
        """Retorna el tamaño aproximado del modelo en bytes"""
        # Count params retorna el número total de pesos (w) y bias (b)
        total_params = self.model.count_params()
        # Cada float32 pesa 4 bytes
        return total_params * 4