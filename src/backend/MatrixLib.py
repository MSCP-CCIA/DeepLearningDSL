import numpy as np


class MatrixLib:

    @staticmethod
    def to_numpy(data):
        """Convierte una lista de listas de Python a un Array de NumPy"""
        return np.array(data)

    @staticmethod
    def add(a, b):
        return np.add(a, b)

    @staticmethod
    def sub(a, b):
        return np.subtract(a, b)

    @staticmethod
    def mult(a, b):
        """
        Maneja multiplicación inteligente:
        - Matriz * Matriz = Producto Punto (Matmul)
        - Matriz * Escalar = Multiplicación escalar
        """
        if isinstance(a, np.ndarray) and isinstance(b, np.ndarray):
            return np.matmul(a, b)
        else:
            return np.multiply(a, b)

    @staticmethod
    def get_shape(a):
        if isinstance(a, np.ndarray):
            return list(a.shape)
        return []
# --- AGREGAR ESTO AL FINAL DE MatrixLib ---

    @staticmethod
    def transpose(a):
        """Calcula la transpuesta (filas x columnas invertidas)"""
        # .T es la forma rápida de numpy, pero aseguramos que sea array primero
        return np.array(a).T

    @staticmethod
    def inverse(a):
        """Calcula la inversa de una matriz cuadrada"""
        try:
            return np.linalg.inv(np.array(a))
        except np.linalg.LinAlgError:
            print("Error: La matriz no es invertible (es singular).")
            return None