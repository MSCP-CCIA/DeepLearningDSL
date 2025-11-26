import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from antlr4 import *
from src.generated.DLLexer import DLLexer
from src.generated.DLParser import DLParser
from src.core.DLInterpreter import DLInterpreter


def execute_code(code_text, interpreter):
    """Compila y ejecuta un bloque de texto usando un intérprete existente"""
    try:
        input_stream = InputStream(code_text)
        lexer = DLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = DLParser(stream)

        # Agregamos un listener de errores personalizado para no llenar la consola de basura
        parser.removeErrorListeners()

        # Parseamos
        tree = parser.program()

        # Ejecutamos (visitamos)
        interpreter.visit(tree)
    except Exception as e:
        print(f"❌ Error: {e}")


def run_file(filepath):
    """Modo Consola: Ejecuta un archivo completo"""
    if not os.path.exists(filepath):
        print(f"Error: El archivo '{filepath}' no existe.")
        return

    print(f"=== EJECUTANDO {filepath} ===")
    interpreter = DLInterpreter()

    # Leemos el archivo nosotros mismos para pasarlo como string
    # Esto evita problemas de encoding con FileStream a veces
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()

    execute_code(code, interpreter)


def run_repl():
    """Modo Interfaz de Texto (REPL): Ejecución interactiva"""
    print("=== DeepLearningDSL Interactive Shell (v1.0) ===")
    print("Escribe 'exit' para salir. Las variables se mantienen en memoria.")
    print("-" * 50)

    # Instanciamos el intérprete UNA SOLA VEZ para mantener la memoria
    interpreter = DLInterpreter()

    while True:
        try:
            # El prompt clásico
            user_input = input("DL> ")

            if user_input.strip() == "exit":
                print("Adiós!")
                break

            if not user_input.strip():
                continue

            # Ejecutamos la línea
            execute_code(user_input, interpreter)

        except KeyboardInterrupt:
            print("\nInterrupción detectada. Escribe 'exit' para salir.")
        except EOFError:
            break


def main():
    # Lógica de decisión
    if len(sys.argv) > 1:
        # Opción A: Ejecutar por consola
        run_file(sys.argv[1])
    else:
        # Opción B: Interfaz de Texto / REPL
        run_repl()


if __name__ == '__main__':
    main()