# Definimos una variable x con una cadena
x = "El valor de (a+b)*c es"
# Podemos realizar múltiples asignaciones
a, b, c = 4, 3, 2
# Realizamos unas operaciones con a,b,c
d = (a + b) * c
# Definimos una variable booleana
imprimir = True
# Si imprimir, print()
if imprimir:
 print(x, d)
# Salida: El valor de (a+b)*c es 14

print('Hola mundo!')


def en_pantalla(frase1, frase2):
   print(frase1, frase2) 
en_pantalla('Me gusta', 'Python')
# Resultado: Me gusta Python

def suma(a, b):
  return a + b
x = suma(2, 3)
print(x)


def f1(a): # Función que "encierra" a f2 (enclosing)
  print(a)
b = 100
def f2(x): # Función anidada
  print(x) # Llamamos a f2 desde
f1
f2(b)
f1('Python')

def maxmin(lista):
  return max(lista), min(lista) # Devielveuna tupla de 2 elementos
l = [1, 3, 5, 6, 0]
maximo, minimo = maxmin(l) # Desempaqueta la tupla en 2 variables
print(minimo, maximo, sep= ' ')


a = 'Python' #Scope global (al módulo)
print('Valor fuera:', a)
def funcion():
    a=33
print('Valor dentro:', a) #Scope local a la función
funcion()
print('Valor fuera:', a)



G = 'Esta variable es de ámbito Global'

def f1():
    E = 'Esta variable es local a f1. Enclosing a f2'

    def f2():
        L = 'Esta variable es local a f2'
        print(L, E, G, sep='\n')

    f2()

f1()


def suma(a, b): # Modificamos a y b en el scope de suma()
 a = 3
 b = 4
 return a+b
a, b = 5, 10
print(suma(a, b))
print(a, b) # a y b no han cambiado fuera de la función
