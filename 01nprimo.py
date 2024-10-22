#Punto 1 Trabajo integrador Módulo 3 - QA

try:
    numero = int(input("Introduce un número: "))
    
    def es_primo(numero):
        if numero <= 1:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True

    if es_primo(numero):
        print(str(numero) + ' es un número primo.')
    else:
        print(str(numero) + ' no es un número primo.')

except:
    print('El dato ingresado no es válido.')


