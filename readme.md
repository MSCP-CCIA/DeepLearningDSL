
Cree un entorno virtual e instale las dependencias:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  
    pip install -r requirements.txt
    ```

### Ejecución

Para ejecutar un script `.dl` desde la consola:

```bash
python3 main.py examples/script.dl
```

-----

## 📂 Estructura del Proyecto

El código fuente está organizado modularmente para separar la definición del lenguaje de su implementación lógica.

  * `grammar/`: Contiene `DL.g4`, la especificación formal de la gramática.
  * `src/generated/`: Código fuente (Lexer, Parser, Visitor) generado automáticamente por ANTLR4.
  * `src/core/`: Contiene `DLInterpreter.py`, el núcleo lógico que gestiona la memoria, los ámbitos (scopes) y el recorrido del AST.
  * `src/backend/`: Módulos de enlace con librerías externas.
      * `TFWrapper.py`: Interfaz para TensorFlow/Keras.
      * `MatrixLib.py`: Operaciones de álgebra lineal con NumPy.
      * `StandardLib.py`: Funciones de I/O, gráficos y algoritmos clásicos.

-----

## 📝 Especificación del Lenguaje

### Tipos de Datos

El lenguaje soporta los siguientes tipos primitivos y compuestos:

  * **Integer / Float:** Números escalares.
  * **String:** Cadenas de texto delimitadas por comillas dobles.
  * **Boolean:** `true` o `false`.
  * **Matrix:** Listas multidimensionales definidas por corchetes. Se convierten internamente a `numpy.ndarray`.

### Declaración de Variables

Se utiliza la palabra reservada `var`.

```javascript
var tasa_aprendizaje = 0.01;
var nombre_modelo = "Perceptron_v1";
var dataset = [[1, 0], [0, 1]];
```

### Operadores

Los operadores aritméticos soportan "broadcasting" cuando se aplican a matrices.

| Símbolo | Operación | Comportamiento en Matrices |
| :---: | :--- | :--- |
| `+` | Suma | Suma elemento a elemento |
| `-` | Resta | Resta elemento a elemento |
| `*` | Multiplicación | Producto Matricial (Dot Product) |
| `/` | División | División elemento a elemento |
| `%` | Módulo | Módulo elemento a elemento |
| `^` | Potencia | Potencia elemento a elemento |

### Control de Flujo

**Condicionales**

```javascript
if (accuracy > 0.95) {
    write("log.txt", "Modelo aceptado");
} else {
    print("Se requiere reentrenamiento");
}
```

**Ciclos**
Soporta iteración definida (`for`) e indefinida (`while`).

```
// Iteración sobre lista o matriz
var datos = [10, 20, 30];
for (x in datos) {
    print(x);
}

// Ciclo condicional
var i = 0;
while (i < 5) {
    i = i + 1;
}
```

-----

## 📚 Biblioteca Estándar

Funciones nativas disponibles en el ámbito global.

### Entrada/Salida

  * `read_csv(ruta)`: Lee un archivo CSV y retorna una matriz numérica.
  * `write(ruta, contenido)`: Escribe una cadena de texto en la ruta especificada.

### Matemáticas y Matrices

  * `transpose(matriz)`: Retorna la matriz transpuesta.
  * `inverse(matriz)`: Calcula la inversa de una matriz cuadrada.
  * `slice(matriz, inicio_col, fin_col)`: Extrae un subconjunto de columnas.
  * **Trigonometría:** `sin(x)`, `cos(x)`, `tan(x)`, `sqrt(x)`, `log(x)`. Estas funciones son vectorizadas.

### Visualización

  * `plot(datos, [titulo])`: Genera y guarda automáticamente una gráfica en formato PNG. Soporta listas simples, matrices o diccionarios de métricas.

### Machine Learning Clásico

  * `kmeans(matriz, k)`: Aplica el algoritmo K-Means y retorna las etiquetas de los clústeres.
  * `linear_regression(x, y)`: Ajusta una regresión lineal y retorna `[pendiente, intercepto]`.

-----

## 🧠 Deep Learning API

Interfaz orientada a objetos para la construcción de redes neuronales secuenciales.

### Clase Sequential

**Instanciación del modelo:**

```
var model = new Sequential();
```

**Métodos del Modelo**

1.  **`add(tipo, unidades, activacion)`**: Añade una capa al modelo.

      * Tipos soportados: "Dense".
      * Activaciones: "relu", "sigmoid", "softmax", "tanh", "linear".

    <!-- end list -->

    ```
    model.add("Dense", 128, "relu");
    ```

2.  **`compile(optimizador, loss, metricas)`**: Configura el proceso de aprendizaje.

    ```
    model.compile("adam", "categorical_crossentropy", ["accuracy"]);
    ```

3.  **`fit(x, y, epocas)`**: Ejecuta el entrenamiento. Retorna un diccionario con el historial de métricas.

    ```
    var history = model.fit(X_train, y_train, 50);
    ```

4.  **`predict(x)`**: Realiza inferencias sobre nuevos datos.

    ```
    var predicciones = model.predict(X_test);
    ```

-----

## 🧪 Ejemplo de Uso

El siguiente script ilustra un flujo de trabajo completo: carga de datos, preprocesamiento matricial, entrenamiento de una red neuronal y generación de reportes.

```
print(">>> INICIANDO PIPELINE DE DATOS <<<");

// 1. Ingesta de Datos
var raw_data = read_csv("datasets/procesos_industriales.csv");

// 2. Preprocesamiento (Slicing y Normalización)
var X = slice(raw_data, 0, 8); // Primeras 8 columnas
var y = slice(raw_data, 8, 9); // Última columna (Target)

// Operación matricial para ingeniería de características
var X_log = log(X); 

// 3. Definición de la Red Neuronal
var nn = new Sequential();
nn.add("Dense", 64, "relu");
nn.add("Dense", 32, "relu");
nn.add("Dense", 1, "sigmoid");

// 4. Compilación y Entrenamiento
nn.compile("adam", "binary_crossentropy", ["accuracy"]);
print("Entrenando modelo...");
var history = nn.fit(X_log, y, 100);

// 5. Evaluación y Reporte
var final_acc = history["accuracy"];

// Lógica de decisión
if (final_acc[99] > 0.85) {
    write("reporte_calidad.txt", "APROBADO: El modelo cumple los estándares.");
} else {
    write("reporte_calidad.txt", "RECHAZADO: Se requiere ajuste de hiperparámetros.");
}

// 6. Visualización
plot(history, "Curva_Aprendizaje");

print(">>> PROCESO FINALIZADO <<<");
```

```
```