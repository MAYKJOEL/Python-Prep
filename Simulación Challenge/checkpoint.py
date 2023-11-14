# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    #Tu código aca:
    #numero = int(numero)
    if str != type(numero):
        if int == type(numero):
            if numero < 0:
                 print('Nulo')
            elif numero == 0:
                 print('Nulo')
            elif numero > 0:
                fact = 1
                for i in range(numero+1):
                    if i > 0:
                        fact *= i
                return fact
                
        elif float == type(numero):
            print('Nulo')
    elif str == type(numero):
        print('Nulo') 


def EsPrimo(valor):
    '''
    Esta función devuelve el valor booleano True si el número reibido como parámetro es primo, de lo 
    contrario devuelve False..
    En caso de que el parámetro no sea de tipo entero debe retornar nulo.
    Recibe un argumento:
        valor: Será el número a evaluar
    Ej:
        EsPrimo(7) debe retornar True
        EsPrimo(8) debe retornar False
    '''
    #Tu código aca:
    valor1 = valor
    if str != type(valor):
        if int == type(valor):
            if valor < 1:
                 print('Nulo')
            elif valor == 1:
                 print(1)
            elif valor > 1:
                Espri = 0
                for i in range(valor):
                    if i >= 2:
                        if valor1%(i) == 0:
                            Espri += 1
                if Espri == 0:
                    return True
                else:
                    return False
                
        elif float == type(valor):
            print('Nulo')
    elif str == type(valor):
        print('Nulo')
    
class Animal:
    def __init__(self,especie,color):
        self.edad = 0
        self.especie = especie
        self.color = color
    def CumplirAnios(self):
        self.edad += 1
        return self.edad
a = Animal('Perro', 'Blanco')

