from django.shortcuts import render

def factorizar_numero(n):
    factores = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1

    return factores


def factorizacion(request):
    resultado = None

    if request.method == "POST":
        numero = int(request.POST.get("numero"))
        factores = factorizar_numero(numero)

        # Convertir lista a "2 × 3 × 3 × 5"
        resultado = " × ".join(str(f) for f in factores)

        return render(request, "factorizacion/fac.html", {"resultado": resultado})

    return render(request, "factorizacion/fac.html")


def info(request):
    return render(request, "factorizacion/inf.html")


def index(request):
    return render(request, "factorizacion/index.html")
