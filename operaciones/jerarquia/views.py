import ast
import operator
from django.shortcuts import render

# Operaciones permitidas
OPERADORES = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}

# Función para evaluar expresiones matemáticas de forma segura
def evaluar_expresion(node):
    # Operaciones binarias (ej: 2 + 3)
    if isinstance(node, ast.BinOp):
        left = evaluar_expresion(node.left)
        right = evaluar_expresion(node.right)
        oper = OPERADORES[type(node.op)] 
        return oper(left, right)

    # Números (compatibles con Python 3.8+)
    elif isinstance(node, ast.Constant):  
        if isinstance(node.value, (int, float)):
            return node.value
        else:
            raise ValueError("Solo se permiten números.")

    elif isinstance(node, ast.Num):  # Compatibilidad con Python <3.8
        return node.n

    # Operaciones unarias (ej: -5)
    elif isinstance(node, ast.UnaryOp):
        if isinstance(node.op, ast.USub):
            return -evaluar_expresion(node.operand)

    # Expresión general
    elif isinstance(node, ast.Expression):
        return evaluar_expresion(node.body)

    raise ValueError("Expresión no válida o no permitida.")


def jerarquia(request):
    resultado = None
    expresion = ""

    if request.method == "POST":
        expresion = request.POST.get("expresion", "")

        try:
            # Convertir texto a árbol AST
            tree = ast.parse(expresion, mode="eval")
            resultado = evaluar_expresion(tree.body)
        except Exception:
            resultado = "Error: expresión no válida"

        return render(request, "jerarquia/jer.html", {
            "resultado": resultado,
            "expresion": expresion
        })

    return render(request, "jerarquia/jer.html")


def info(request):
    return render(request, "jerarquia/inf.html")


def index(request):
    return render(request, "jerarquia/index.html")
