from django.shortcuts import render
import random


def resta(request):
    resultado = None
    operacion = None
    if request.method == "POST":
        num1 = int(request.POST.get("numero1"))
        num2 = int(request.POST.get("numero2"))
        resultado = num1 - num2
        operacion =f" {num1} - {num2} "
        return render(request, "resta/res.html", {
            "resultado": resultado,
            "operacion": operacion 
            })


    return render(request, "resta/res.html")

def info(request):
    return render(request, "resta/inf.html") 
def index(request):
    return render(request, "resta/index.html") 
# 👇 
def ejer(request):
    mensaje = None

    # ejercicio aleatorio
    n1 = random.randint(1, 20)
    n2 = random.randint(1, 20)
    correcta = n1 - n2

    if request.method == "POST":
        n1 = int(request.POST.get("n1"))
        n2 = int(request.POST.get("n2"))
        correcta = int(request.POST.get("correcta"))
        respuesta = int(request.POST.get("respuesta"))

        if respuesta == correcta:
            mensaje = "Correcto ✅"
        else:
            mensaje = f"Incorrecto ❌. La respuesta es {correcta}"

    return render(request, "resta/ejer.html", {
        "n1": n1,
        "n2": n2,
        "mensaje": mensaje,
        "correcta": correcta
    })
