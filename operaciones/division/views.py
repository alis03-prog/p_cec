from django.shortcuts import render
import random

def division(request):
    resultado = None
    error = None
    operacion = None

    if request.method == "POST":
        try:
            num1 = float(request.POST.get("numero1"))
            num2 = float(request.POST.get("numero2"))

            if num2 == 0:
                error = "Error: No se puede dividir entre 0."
            else:
                resultado = num1 / num2
                operacion = f"{num1} entre {num2}"

        except ValueError:
            error = "Ingresa valores numéricos válidos."

    return render(request, "division/div.html", {
        "resultado": resultado,
        "error": error,
        "operacion": operacion
    })


def info(request):
    return render(request, "division/inf.html")


def index(request):
    return render(request, "division/index.html")


# 👇 APARTADO DE EJERCICIO (AGREGADO / CORREGIDO)
def ejer(request):
    mensaje = None

    if request.method == "POST":
        # Recuperar datos del ejercicio
        n1 = int(request.POST.get("n1"))
        n2 = int(request.POST.get("n2"))
        correcta = float(request.POST.get("correcta"))
        respuesta = float(request.POST.get("respuesta"))

        # Comparar respuestas
        if respuesta == correcta:
            mensaje = "Correcto ✅"
        else:
            mensaje = f"Incorrecto ❌. La respuesta es {correcta}"

    else:
        # Generar ejercicio solo en GET
        n1 = random.randint(1, 20)
        n2 = random.randint(1, 20)
        correcta = round(n1 / n2, 2)

    return render(request, "division/ejer.html", {
        "n1": n1,
        "n2": n2,
        "correcta": correcta,
        "mensaje": mensaje
    })
