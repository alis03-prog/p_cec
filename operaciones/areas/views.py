from django.shortcuts import render
import math

def areas(request):
    resultado = None
    figura = None

    if request.method == "POST":
        figura = request.POST.get("figura")

        try:
            # Cuadrado → lado²
            if figura == "cuadrado":
                lado = float(request.POST.get("lado"))
                resultado = lado * lado

            # Rectángulo → base × altura
            elif figura == "rectangulo":
                base = float(request.POST.get("base"))
                altura = float(request.POST.get("altura"))
                resultado = base * altura

            # Triángulo → (base × altura) / 2
            elif figura == "triangulo":
                base = float(request.POST.get("base"))
                altura = float(request.POST.get("altura"))
                resultado = (base * altura) / 2

            # Círculo → π * r²
            elif figura == "circulo":
                radio = float(request.POST.get("radio"))
                resultado = math.pi * (radio ** 2)

        except (ValueError, TypeError):
            resultado = "Error: Ingrese valores numéricos válidos."

    return render(request, "areas/are.html", {
        "resultado": resultado,
        "figura": figura
    })

def info(request):
    return render(request, "areas/inf.html")

def index(request):
    return render(request, "areas/index.html")
