from django.shortcuts import render
import random   # 👈 agregar esto

def suma(request):
    resultado = None
    operacion = None

    if request.method == "POST":
        num1 = float(request.POST.get("numero1"))
        num2 = float(request.POST.get("numero2"))

        resultado = num1 + num2
        operacion = f"{num1} + {num2}"

    return render(request, "suma/sum.html", {
        "resultado": resultado,
        "operacion": operacion
    })

def info(request):
    return render(request, "suma/inf.html")

def index(request):
    return render(request, "suma/index.html")

# 👇 
def ejer(request):
    mensaje = None

    # ejercicio aleatorio
    n1 = random.randint(1, 20)
    n2 = random.randint(1, 20)
    correcta = n1 + n2

    if request.method == "POST":
        n1 = int(request.POST.get("n1"))
        n2 = int(request.POST.get("n2"))
        correcta = int(request.POST.get("correcta"))
        respuesta = int(request.POST.get("respuesta"))

        if respuesta == correcta:
            mensaje = "Correcto ✅"
        else:
            mensaje = f"Incorrecto ❌. La respuesta es {correcta}"

    return render(request, "suma/ejer.html", {
        "n1": n1,
        "n2": n2,
        "mensaje": mensaje,
        "correcta": correcta
    })
