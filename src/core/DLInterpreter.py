import numpy as np
from src.generated.DLVisitor import DLVisitor
from src.generated.DLParser import DLParser
from src.backend.MatrixLib import MatrixLib
from src.backend.TFWrapper import TFWrapper
from src.backend.StandardLib import StandardLib
import sys

class DLInterpreter(DLVisitor):
    def __init__(self):
        self.memory = {}
        self.memory_stats = {}

    def visitProgram(self, ctx: DLParser.ProgramContext):
        return self.visitChildren(ctx)

    def visitStatVarDecl(self, ctx: DLParser.StatVarDeclContext):
        return self.visit(ctx.varDeclaration())

    def visitStatAssign(self, ctx: DLParser.StatAssignContext):
        return self.visit(ctx.assignment())

    def visitStatPrint(self, ctx: DLParser.StatPrintContext):
        return self.visit(ctx.printStmt())

    def visitStatIf(self, ctx: DLParser.StatIfContext):
        return self.visit(ctx.ifStatement())

    def visitStatWhile(self, ctx: DLParser.StatWhileContext):
        return self.visit(ctx.whileStatement())

    def visitStatFor(self, ctx: DLParser.StatForContext):
        return self.visit(ctx.forStatement())

    def visitStatExpr(self, ctx: DLParser.StatExprContext):
        return self.visit(ctx.expression())

    def visitStatMethodCall(self, ctx):
        # Esta regla fue removida en la gramática final,
        # pero por si acaso ANTLR dejó rastro, la ignoramos o redirigimos.
        return self.visitChildren(ctx)

    def visitVarDeclaration(self, ctx: DLParser.VarDeclarationContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        # Guardamos valor Y peso
        self.memory[name] = value
        self.memory_stats[name] = self._calculate_size(value)  # <--- NUEVO

        return value

    def visitAssignment(self, ctx: DLParser.AssignmentContext):
        left_node = ctx.expression(0)
        right_node = ctx.expression(1)
        var_name = left_node.getText()
        value = self.visit(right_node)
        # Guardamos valor Y peso
        self.memory[var_name] = value
        self.memory_stats[var_name] = self._calculate_size(value)  # <--- NUEVO

        return value

    def visitBlock(self, ctx: DLParser.BlockContext):
        for statement in ctx.statement():
            self.visit(statement)
        return None

    def visitIfStatement(self, ctx: DLParser.IfStatementContext):
        condition = self.visit(ctx.expression())
        if condition:
            return self.visit(ctx.block(0))
        elif ctx.ELSE():
            return self.visit(ctx.block(1))
        return None

    def visitWhileStatement(self, ctx: DLParser.WhileStatementContext):
        condition = self.visit(ctx.expression())
        while condition:
            self.visit(ctx.block())
            condition = self.visit(ctx.expression())
        return None

    def visitForStatement(self, ctx: DLParser.ForStatementContext):
        iterator_name = ctx.ID().getText()
        iterable = self.visit(ctx.expression())
        try:
            iterator = iter(iterable)
        except TypeError:
            raise Exception(f"Error: '{iterable}' no es iterable.")
        for item in iterator:
            self.memory[iterator_name] = item
            self.visit(ctx.block())
        return None

    def visitPrintStmt(self, ctx: DLParser.PrintStmtContext):
        value = self.visit(ctx.expression())
        print(value)
        return None

    def visitAtomNew(self, ctx: DLParser.AtomNewContext):
        new_ctx = ctx.newExpr()
        class_name = new_ctx.ID().getText()
        if class_name == "Sequential":
            return TFWrapper()
        else:
            raise Exception(f"Clase '{class_name}' no existe.")

    def visitExprMethodCall(self, ctx: DLParser.ExprMethodCallContext):
        # Estructura: expression . ID ( args )
        obj = self.visit(ctx.expression(0))  # El objeto antes del punto
        method_name = ctx.ID().getText()
        # Recolectar argumentos
        args = []
        # Los argumentos empiezan desde el índice 1 de las expresiones
        # (el índice 0 es el objeto mismo)
        if len(ctx.expression()) > 1:
            for i in range(1, len(ctx.expression())):
                args.append(self.visit(ctx.expression(i)))
        # Verificar si es nuestro Wrapper de TensorFlow
        if isinstance(obj, TFWrapper):
            method = getattr(obj, method_name, None)
            if method:
                return method(*args)
            else:
                raise Exception(f"Método '{method_name}' no existe en Sequential.")

        raise Exception(f"El objeto '{obj}' no tiene métodos soportados.")


    def visitAtomNumber(self, ctx: DLParser.AtomNumberContext):
        text = ctx.getText()
        return float(text) if '.' in text else int(text)

    def visitAtomString(self, ctx: DLParser.AtomStringContext):
        return ctx.getText()[1:-1]  # Quitamos comillas

    def visitAtomId(self, ctx: DLParser.AtomIdContext):
        name = ctx.getText()
        if name in self.memory:
            return self.memory[name]
        raise Exception(f"Error: Variable '{name}' no definida.")

    def visitAtomBool(self, ctx: DLParser.AtomBoolContext):
        return ctx.getText() == 'true'

    def visitAtomList(self, ctx: DLParser.AtomListContext):
        list_ctx = ctx.list_()
        elements = []
        if list_ctx.expression():
            for expr in list_ctx.expression():
                elements.append(self.visit(expr))
        return MatrixLib.to_numpy(elements)

    def visitExprAddSub(self, ctx: DLParser.ExprAddSubContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        # 1. Si es una suma y ALGUNO de los dos es texto -> Concatenar
        if ctx.PLUS() and (isinstance(left, str) or isinstance(right, str)):
            return str(left) + str(right)

        # 2. Si no es texto, seguimos con la lógica matemática (Matrices o Números)
        is_matrix = isinstance(left, np.ndarray) or isinstance(right, np.ndarray)

        if ctx.PLUS():
            return MatrixLib.add(left, right) if is_matrix else left + right
        else:
             return MatrixLib.sub(left, right) if is_matrix else left - right



    def visitExprMultDiv(self, ctx: DLParser.ExprMultDivContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        is_matrix = isinstance(left, np.ndarray) or isinstance(right, np.ndarray)
        if ctx.MULT():
            return MatrixLib.mult(left, right) if is_matrix else left * right
        elif ctx.DIV():
            return np.divide(left, right) if is_matrix else left / right
        else:
            return left % right

    def visitExprRelational(self, ctx: DLParser.ExprRelationalContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if ctx.GT(): return left > right
        if ctx.LT(): return left < right
        if ctx.GTE(): return left >= right
        if ctx.LTE(): return left <= right

        return False


    def visitExprEquality(self, ctx: DLParser.ExprEqualityContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.EQ(): return left == right
        return left != right

    def visitStatPlot(self, ctx: DLParser.StatPlotContext):
        plot_node = ctx.plotStmt()
        args = []
        if plot_node.expression():
            for expr in plot_node.expression():
                args.append(self.visit(expr))
        return StandardLib.plot(*args)


    def visitExprIndex(self, ctx: DLParser.ExprIndexContext):
        structure = self.visit(ctx.expression(0))
        index = self.visit(ctx.expression(1))
        try:
            return structure[index]
        except TypeError:
            raise Exception(f"Error: El objeto '{structure}' no es indexable.")
        except KeyError:
            raise Exception(f"Error: La clave '{index}' no existe en la estructura.")
        except IndexError:
            raise Exception(f"Error: Índice {index} fuera de rango.")

    def visitExprFuncCall(self, ctx: DLParser.ExprFuncCallContext):
        func_name = ctx.ID().getText()
        args = []
        if ctx.expression():
            for expr in ctx.expression():
                args.append(self.visit(expr))
        if func_name == "plot":
            return StandardLib.plot(*args)
        elif func_name == "read_csv":
            return StandardLib.read_csv(*args)
        elif func_name == "kmeans":
            return StandardLib.kmeans(*args)
        elif func_name == "linear_regression":
            return StandardLib.linear_regression(*args)
        elif func_name == "write":
            return StandardLib.write_file(*args)
        elif func_name in ["sin", "cos", "tan", "log", "sqrt"]:
            return StandardLib.math_op(func_name, *args)
        elif func_name == "transpose":
            return MatrixLib.transpose(*args)
        elif func_name == "inverse":
            return MatrixLib.inverse(*args)
        elif func_name == "slice":
            return StandardLib.slice_data(*args)
        elif func_name == "memory":
            print("\n=== REPORTE DE MEMORIA RAM (EN VIVO) ===")
            print(f"{'VARIABLE':<15} | {'TIPO':<15} | {'TAMAÑO'}")
            print("-" * 45)
            total_usage = 0
            for name, val in self.memory.items():
                current_size = self._calculate_size(val)
                self.memory_stats[name] = current_size
                tipo = type(val).__name__
                if isinstance(val, TFWrapper): tipo = "NeuralNetwork"
                if isinstance(val, np.ndarray): tipo = f"Matrix {val.shape}"
                print(f"{name:<15} | {tipo:<15} | {self._format_bytes(current_size)}")
                total_usage += current_size
            print("-" * 45)
            print(f"TOTAL USADO: {self._format_bytes(total_usage)}\n")
            return total_usage
        raise Exception(f"Función '{func_name}' no definida.")

    def _calculate_size(self, value):
        """Calcula el tamaño en bytes de cualquier objeto del DSL"""
        try:
            # 1. Matrices de NumPy (tienen propiedad .nbytes exacta)
            if isinstance(value, np.ndarray):
                return value.nbytes
            # 2. Modelos de Deep Learning (usamos el método que creamos)
            elif isinstance(value, TFWrapper):
                return value.get_estimated_size()
            # 3. Tipos básicos (int, float, str, bool, list)
            else:
                return sys.getsizeof(value)
        except:
            return 0

    def _format_bytes(self, size):
        power = 2 ** 10
        n = 0
        power_labels = {0: '', 1: 'KB', 2: 'MB', 3: 'GB'}
        while size > power:
            size /= power
            n += 1
        return f"{size:.2f} {power_labels.get(n, '')}bytes"