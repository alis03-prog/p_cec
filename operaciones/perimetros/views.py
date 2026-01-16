from django.shortcuts import render
import math

def perimetros(request):
    resultado = None
    figura = None

    if request.method == "POST":
        figura = request.POST.get("figura")

        try:
            # Cuadrado → 4 × lado
            if figura == "cuadrado":
                lado = float(request.POST.get("lado"))
                resultado = 4 * lado

            # Rectángulo → 2(base + altura)
            elif figura == "rectangulo":
                base = float(request.POST.get("base"))
                altura = float(request.POST.get("altura"))
                resultado = 2 * (base + altura)

            # Triángulo → suma de los tres lados
            elif figura == "triangulo":
                lado1 = float(request.POST.get("lado1"))
                lado2 = float(request.POST.get("lado2"))
                lado3 = float(request.POST.get("lado3"))
                resultado = lado1 + lado2 + lado3

            # Círculo → 2πr   ← (AGREGADO)
            elif figura == "circulo":
                radio = float(request.POST.get("radio"))
                resultado = 2 * math.pi * radio

        except (ValueError, TypeError):
            resultado = "Error: Ingrese valores numéricos válidos."

    return render(request, "perimetros/per.html", {
        "resultado": resultado,
        "figura": figura
    })


def info(request):
    return render(request, "perimetros/inf.html")


def index(request):
    return render(request, "perimetros/index.html")
