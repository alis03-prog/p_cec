from django.shortcuts import render

def rectas(request):
    resultado = None
    num1 = None
    num2 = None

    if request.method == "POST":
        num1 = int(request.POST.get("numero1")) #Sirve para ingresar el primer numero
        num2 = int(request.POST.get("numero2")) #Sirve para ungresar el segundo numero
        resultado = num1 + num2 #Suma los dos numeros ingresados para crear la recta

        # Sirve para crear una lista para la recta numérica
        minimo = min(num1, num2, resultado) # Es el numero minimo de la recta
        maximo = max(num1, num2, resultado) # Es el numero maximo de la recta

        # Para que la recta tenga un margen
        minimo -= 2 # Se le quita 2 al numero ingresado 
        maximo += 2 # Se le suma 2 al numero ingresado 

        recta = list(range(minimo, maximo + 1)) # aqui se suma mas 1 

        return render(request, "rectas/rec.html", {
            "resultado": resultado,
            "num1": num1,
            "num2": num2,
            "recta": recta
        })

    return render(request, "rectas/rec.html")
    
def info(request):
    return render(request, "rectas/inf.html")

def index(request):
    return render(request, "rectas/index.html")
