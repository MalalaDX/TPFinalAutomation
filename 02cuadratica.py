#Punto 2 Trabajo integrador Módulo 3 - QA

print('Ingresar los valores de las variables de un polinomio de grado 2 (ax^2 + bx + c = 0): ')
a=0
while a==0:
    try:
        a = float(input('Ingrese un valor para a: '))
        if a==0:
            print('El valor de a no puede ser 0. Intente nuevamente.')
    except:
        print('Ingrese número válido')

    b = float(input('Ingrese un valor para b: '))
    c = float(input('Ingrese un valor para c: '))

    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        # Existen dos soluciones
        raiz_1 = (-b + discriminante**0.5) / (2*a)
        raiz_2 = (-b - discriminante**0.5) / (2*a)
        print(f'Las raíces reales son: {raiz_1} y {raiz_2}')
    elif discriminante == 0:
        # Existe una solución
        raiz_1 = -b / (2*a)
        print(f'Hay una única raiz: {raiz_1}')
    else:
        # No existen raices reales
        print('El discriminante es negativo, no hay raíces reales')