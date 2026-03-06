#mensaje inicial
print ("¡Hola! Este es mi primer programa en Python." )

#variables simples
nombre = "Karen Ñanco Vásquez"
edad = 35
ciudad = "Osorno"

print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)

#operaciones básicas
numero1 = 10          # primer sumando
numero2 = 5           # segundo sumando
resultado = numero1 + numero2  # se realiza la suma y se guarda el valor
print("La suma de", numero1, "y", numero2, "es:", resultado) # resultado

#exploración del módulo integrado
import math           # Se importó el módulo

""" print (math.pi)

numero = 25 
raiz= math.sqrt(numero)
print(raiz) """

numero_raiz = 25      # Se define el número
raiz = math.sqrt(numero_raiz) # Se usa la función sqrt() del módulo math
print("La raíz cuadrada de", numero_raiz, "es:", raiz) # Se muestra el resultado final

