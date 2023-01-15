import numpy as numpy

while True:
    print("""
    Bienvenido, a la calculadora
    
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) División
    5) Exponente
    6) Raiz
    7) Seno
    8) Apagar calculadora
    """)
    opcion = int(input("Elige una opción: ") )
    if opcion == 1:
        V1 = float(input("Introduce tu primer número: ") )
        V2 = float(input("Introduce tu segundo número: ") )
        print(" ")
        print("RESULTADO: La suma de",V1,"+",V2,"es igual a",V1+V2)
    elif opcion == 2:
        V1 = float(input("Introduce tu primer número: ") )
        V2 = float(input("Introduce tu segundo número: ") )
        print(" ")
        print("RESULTADO: La resta de",V1,"-",V2,"es igual a",V1-V2)
    elif opcion == 3:
        V1 = float(input("Introduce tu primer número: ") )
        V2 = float(input("Introduce tu segundo número: ") )
        print(" ")
        print("RESULTADO: La multiplicación de",V1,"*",V2,"es igual a",V1*V2)
    elif opcion == 4:
        V1 = float(input("Introduce tu primer número: ") )
        V2 = float(input("Introduce tu segundo número: ") )
        print(" ")
        print("RESULTADO: La división de",V1,"*",V2,"es igual a",V1/V2)    
    elif opcion == 5:
        V1 = float(input("Introduce tu primer número: ") )
        V2 = float(input("Introduce tu segundo número: ") )
        print(" ")
        print("RESULTADO: El exponente de",V1,"*",V2,"es igual a",V1**V2)
    elif opcion == 6:
        V1 = float(input("Introduce tu primer número: ") )
        raiz = numpy.sqrt(V1)
        print(" ")
        print("RESULTADO: Raiz de",V1,"es igual a", raiz)
    elif opcion == 7:
        V1 = float(input("Introduce tu primer número: ") )
        radianes=[numpy.pi/V1]
        numpy.cos(radianes)
        print(" ")
        print("RESULTADO: El coseno de",V1,radianes)  
    elif opcion == 8:
        break
    else:
        print("Opción incorrecta")

   
