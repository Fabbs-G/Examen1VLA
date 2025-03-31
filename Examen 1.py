"""
Primer examen de Python de VLA
Nombre: Fabián Guevara
"""

#Menu principal
def menuprincipal():
    print("¿Cuál ejercicio desea revisar?")
    print("1.Ejercicio 1")
    print("2.Ejercicio 2")
    print("3.Salir")

    opcion = input("Ingrese su selección: ")
    if (opcion == "1"):
        ejercicio1()
    elif (opcion == "2"):
        ejercicio2()
    elif (opcion == "3"):
        quit()
    else:
        print("Escoja una de las opciones")
        menuprincipal()
        
#Ejercicio 1
def ejercicio1():
    print("¿Cuál formula notable desea desarrollar?")
    print("1.(a+b)²")
    print("2.(a-b)²")
    print("3.(a+b)(a-b)")

    opcion = input("Ingrese su selección: ")
    if (opcion == "1"):
        a = int(input("Ingrese el valor de a: "))
        b = int(input("Ingrese el valor de b: "))
        resultado = ((a**2)+(2*(a*b))+(b**2))
        print("El cuadrado de una suma es: a²+2ab+b²")
        print("El resultado es: "+str(resultado))
    elif (opcion == "2"):
        a = int(input("Ingrese el valor de a: "))
        b = int(input("Ingrese el valor de b: "))
        resultado = (a**2-2*(a*b)+b**2)
        print("El cuadrado de una diferencia es: a²-2ab+b²")
        print("El resultado es: "+str(resultado))
    elif (opcion == "3"):
        a = int(input("Ingrese el valor de a: "))
        b = int(input("Ingrese el valor de b: "))
        resultado = (a**2-b**2)
        print("La suma de una diferencia es: a²-b²")
        print("El resultado es: "+str(resultado))
    else:
        print("Escoja una de las opciones")
        ejercicio1()

    opcion = input("¿Desea realizar otra fórmula? (si/no)")
    if (opcion == "si"):
        ejercicio1()
    elif (opcion == "no"):
        menuprincipal()
    

#Ejercicio 2

def ejercicio2():
    nombre = input("Ingrese su nombre: ")
    fecha = input("Ingrese la fecha: ")
    precio = int(input("Ingrese el precio del artículo: "))
    monto = int(input("Ingrese el monto con que va a pagar: "))
    if (precio >= 100):
        descuento = precio*0.2
    elif (precio < 100) and (precio >= 50):
        descuento = precio*0.1
    else:
        descuento = 0
    vuelto = monto - (precio-descuento)
    print("\nTienda Swite")
    print("Fecha: "+fecha)
    print("Nombre: "+nombre)
    print("Precio: "+str(precio))
    print("Descuento: "+str(descuento))
    print("Monto a cancelar: "+str(precio-descuento))
    print("Cantidad con que cancela: "+str(monto))
    print("Vuelto: "+str(vuelto))

    opcion = input("¿Desea realizar otra compra? (si/no)")
    if (opcion == "si"):
        ejercicio2()
    elif (opcion == "no"):
        menuprincipal()


menuprincipal()
