from django.shortcuts import render
import re

def resolver_ecuaciones1(expresion):
    """
    Resuelve ecuaciones de primer grado del tipo:
    ax + b = c
    """
    expresion = expresion.replace(" ", "")  # Quitar espacios

    # Separar en ambos lados del signo "="
    if "=" not in expresion:
        return "Error: La ecuación debe contener un '='"

    izquierda, derecha = expresion.split("=")

    # Expresión regular para detectar ax + b
    patron = r"([+-]?\d*)x([+-]?\d+)?"

    match = re.fullmatch(patron, izquierda)
    if not match:
        return "Error: Solo se aceptan ecuaciones como 'ax + b = c'"

    a_str, b_str = match.groups()

    # Procesar a
    if a_str in ["", "+"]:
        a = 1
    elif a_str == "-":
        a = -1
    else:
        a = int(a_str)

    # Procesar b
    b = int(b_str) if b_str else 0

    # Procesar c
    try:
        c = int(derecha)
    except ValueError:
        return "Error: El valor a la derecha del '=' debe ser un número"

    # Resolver ax + b = c
    if a == 0:
        if b == c:
            return "La ecuación tiene infinitas soluciones"
        else:
            return "La ecuación no tiene solución"

    x = (c - b) / a
    return x


def ecuaciones1(request):
    resultado = None
    expresion = ""

    if request.method == "POST":
        expresion = request.POST.get("expresion", "")

        try:
            resultado = resolver_ecuaciones1(expresion)
        except Exception:
            resultado = "Error: ecuación no válida"

        return render(request, "ecuaciones1/ecu.html", {
            "resultado": resultado,
            "expresion": expresion
        })

    return render(request, "ecuaciones1/ecu.html")


def info(request):
    return render(request, "ecuaciones1/inf.html")


def index(request):
    return render(request, "ecuaciones1/index.html")
