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


a = 10
b = 3
if a > b:
 print ('SI se cumple la condición')

 print ('Ya estamos fuera del if') 

a = 2
b = 1
if a < b:
 print ('se cumple la condición')

 print('fuera del if')

a = 2
b = 1
if a < b:
    print('se cumple la condición')

print('fuera del if')


if a > b:
    print('a es mayor que b')


a = 10
b = 10
if a > b:
  print ('A es menor que B')
elif a == b:
  print ('A es igual a B')
else:
  print ('A es mayor que B')

  print ('Ya hemos salido del condicional')

nota=int(input("Introduce tu nota:  "))
if nota<5:
  print("Suspenso")
elif nota<7:
  print("Aprobado")
elif nota<9:
  print("Notable")
else:
  print("Sobresaliente")
  #cuando ponga introduce tu nota: escribe el número que quieras y saldrá dependiendo de éste suspenso/aprobado/notable o sobresaliente

edad=int(input("Introduce edad: "))
if edad<18:
 print("No puedes pasar")
elif edad>100:
 print("Edad incorrecta")
else:
 print("Adelante")
 #lo mismo que en el ejemplo anterior

keys = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'van Rossum', 60]
d = dict(zip(keys, values))
for k, v in d.items(): # d.items devuelve tupla con clave, valor
 print('{}: {}'.format(k, v))

# Programa que pide una nota por consola y valora si el alumno ha aprobado o no.
notaIn=int(input("Introduzca nota:"))
if notaIn<5:
 calificacion="Suspenso"
else: calificacion="Aprobado"
print(calificacion)
# IF no sólo evalúa un boleano, también si una variable contiene información
variable = 19
if variable:
 print("Contiene información")
else:
 print("No contiene información")
#En este ejemplo sí evalúa un boleano
variable = 19
if variable == True:
 print("Contiene información")
else:
 print("No contiene información")
# Programa que pide una edad por consola y valora si el usuario es mayor de edad o no.
edad=int(input("Introduce edad: "))
if edad<18:
 print("No puedes pasar")
elif edad>100:
 print("Edad incorrecta")
else:
 print("Adelante")
# Programa que pide una nota por consola y valora las posibles calificaciones del alumno.
nota=int(input("Introduce tu nota: "))
if nota<5:
 print("Suspenso")
elif nota<7:
 print("Aprobado")
elif nota<9:
 print("Notable")
else:
 print("Sobresaliente")
# IF abreviado
n_num1 = 5
n_num2 = 10
if n_num1 > n_num2: print(n_num1 , "es mayor que" , n_num2)
# IF...ELSE abreviado
a = 2
b = 330
print("A") if a > b else print("B")
# Se pueden concatenar operadores de comparación:
edad=117
if 0<edad<100: # Sería como poner: if edad>0 and edad<100
 print("Edad correcta")
else:
 print("Edad incorrecta")
# Otro ejemplo de operadores de comparación concatenados
salarioPresidente = int(input("Introduce salario presidente: "))
print("El salario del presidente es de" ,salarioPresidente)
salarioDirector = int(input("Introduce salario Director: "))
print("El salario del director es de" , salarioDirector)
salarioJefe = int(input("Introduce salario jefe: "))
print("El salario del jefe es de" , salarioJefe)
salarioOperario = int(input("Introduce salario operario: "))
print("El salario del operario es de" , salarioOperario)
if salarioOperario<salarioJefe<salarioDirector<salarioPresidente:
 print("Todo ok")
else:
 print("Algo no va bien")
# Operadores AND y OR
distancia = int(input("Introduce distancia: "))
numHermanos = int(input("Introduce número de hermanos en el centro: "))
notaMedia = int(input("Introduce notaMedia: "))
if distancia>20 or numHermanos<2 or notaMedia<=5:
 print("NO eres candidato a la beca")
else:
 print("Sí eres candidato a la beca")
# Operador IN
opcion = input("ELige opcion: opcion1, opcion2, opcion3, opcion4: ")
pasoMinusculas = opcion.lower()
if pasoMinusculas in("opcion1",
"opcion2", "opcion3", "opcion4"):
 print("Opción válida: " + pasoMinusculas)
else:
 print("Opción inválida: " + pasoMinusculas)
# If anidados. Queremos comprar un coche. Necesitamos ser mayores de edad y tener 20000€
n_edad = int(input("Introduzca su edad:"))
n_dinero = int(input("Introduzca presupuesto: "))
if n_edad < 18:
 print("No tienes la edad suficiente para conducir.")
else:
 if n_dinero < 20000:
  print("Tienes la edad pero no el dinero para comprar el coche.")
 else:
  print("Puedes comprar el coche.")




  # DICCIONARIOS
"""Los diccionarios, también llamados matrices asociativas, deben su nombre a que son colecciones que relacionan una clave y un
valor. Un diccionario es una colección desordenada, modificable e indexada. En Python, los diccionarios se escriben entre llaves y 
tienen claves y valores."""
# Declaración de un diccionario
# Declaración de un diccionario
miDiccionario = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(miDiccionario)

# Acceder a valores en un diccionario
peliculas = {"Love Actually": "Richard Curtis",
             "Kill Bill": "Tarantino",
             "Amélie": "Jean-Pierre Jeunet"}
print(peliculas["Love Actually"])

# Reasignar valores en un diccionario
peliculas["Kill Bill"] = "Quentin Tarantino"
print(peliculas)

# Usar una tupla dentro de un diccionario
miDiccionario3 = {"nombre": "Jordan",
                  "Equipo": "Bulls",
                  "Anillos": [1991, 1992, 1993, 1996, 1997, 1998]}
print(miDiccionario3["Anillos"])

# Eliminar valores de un diccionario
peliculas = {"Love Actually": "Richard Curtis",
             "Kill Bill": "Tarantino",
             "Amélie": "Jean-Pierre Jeunet"}
peliculas.pop("Love Actually")
print(peliculas)

# Crear un diccionario a partir de dos listas
lista_claves = ["nombre", "edad"]
lista_valores = ["Angel", 43]
diccionario = dict(zip(lista_claves, lista_valores))
print(diccionario)

# Comprobar si una clave está en el diccionario
print("nombre" in diccionario)

# Imprimir las claves y valores del diccionario
peliculas = {"Love Actually": "Richard Curtis",
             "Kill Bill": "Tarantino",
             "Amélie": "Jean-Pierre Jeunet"}
for clave, valor in peliculas.items():
    print(clave, ":", valor)

# Longitud de un diccionario
peliculas = {"Love Actually": "Richard Curtis",
             "Kill Bill": "Tarantino",
             "Amélie": "Jean-Pierre Jeunet"}
print(len(peliculas))

# Agregar elementos a un diccionario
miDiccionario = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
miDiccionario["color"] = "red"
print(miDiccionario)

# Eliminar el último elemento insertado
miDiccionario = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
miDiccionario.popitem()
print(miDiccionario)

# Eliminar un elemento por clave
miDiccionario = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del miDiccionario["model"]
print(miDiccionario)

# Vaciar un diccionario
miDiccionario = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
miDiccionario.clear()
print(miDiccionario)

# Copiar un diccionario
miDiccionario = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
miDict = miDiccionario.copy()
print(miDict)

# Diccionarios anidados
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily["child1"])
