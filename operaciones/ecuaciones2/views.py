from django.shortcuts import render
import cmath

def ecuaciones2(request):
    resultado = None
    resultado_lista = []
    a_val = b_val = c_val = ""

    if request.method == 'POST':
        a_val = request.POST.get('a', '')
        b_val = request.POST.get('b', '')
        c_val = request.POST.get('c', '')

        try:
            a = float(a_val)
            b = float(b_val)
            c = float(c_val)

            if a == 0:
                resultado = "❌ No es una ecuación de segundo grado"
            else:
                discriminante = b**2 - 4*a*c
                x1 = (-b + (cmath.sqrt(discriminante))) / (2*a)
                x2 = (-b - (cmath.sqrt(discriminante))) / (2*a)

                if discriminante >= 0:
                    resultado = f"x₁ = {x1.real:.2f}, x₂ = {x2.real:.2f}"
                else:
                    resultado = (
                        f"x₁ = {x1.real:.2f}{'+' if x1.imag >= 0 else ''}{x1.imag:.2f}i, "
                        f"x₂ = {x2.real:.2f}{'+' if x2.imag >= 0 else ''}{x2.imag:.2f}i"
                    ) 

            # Separamos el resultado en lista para la plantilla
            resultado_lista = [parte.strip() for parte in resultado.split(',')]

        except ValueError:
            resultado = "⚠️ Por favor ingrese valores numéricos válidos"
            resultado_lista = []

    return render(request, "ecuaciones2/ecu.html", {
        "resultado": resultado,
        "resultado_lista": resultado_lista,
        "a_val": a_val,
        "b_val": b_val,
        "c_val": c_val
    })


def info(request):
    return render(request, "ecuaciones2/inf.html")


def index(request):
    return render(request, "ecuaciones2/index.html")
