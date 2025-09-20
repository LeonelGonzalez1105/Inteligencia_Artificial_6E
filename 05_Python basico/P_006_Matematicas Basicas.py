
#operador suma
print(2 + 2)

#operador resta
print(5 - 3)

#operador multiplicacion
print(3 * 4)

#operador division
print(10 / 2) # La division siempre devuelve un numero flotante

#operador division entera
print(10 // 3) # La division entera devuelve la parte entera de la division

#operador modulo
print(10 % 3) # El modulo devuelve el resto de la division

#operador potencia
print(2 ** 3) # La potencia devuelve el resultado de elevar un numero a otro

#operador de precedencia
print(2 + 3 * 4) # La multiplicacion tiene mayor precedencia que la suma
print((2 + 3) * 4) # Los parentesis tienen mayor precedencia que la multiplicacion y la suma



numero1 = 7.263
numero2 = 12

resto = numero1 % numero2
print("Resto: ", resto)



#Codigo de ejemplo calculo de edades
edades=[25, 30, 35, 40, 45] #se utiliza [] para definir una lista

suma_edades = sum(edades) #funcion sum() para sumar los elementos de la lista
cantidad_edades = len(edades) #funcion len() para obtener la cantidad de elementos de la lista

promedio_edad = suma_edades // cantidad_edades #calculo del promedio de edades utilizando division entera

print("En total hay ", cantidad_edades, " edades")
print("Promedio de edades: ", promedio_edad)

#codigo ejemplo: area de un rectangulo
base = 5.5
altura = 3.2
area = base * altura #calculo del area del rectangulo
print("Area del rectangulo: ", area)

#codigo de ejemplo conversion de temperaturas
celsius = 25

farenheit = (celsius * 9/5) +32 #formula de conversion de celsius a farenheit
kelvin = celsius + 273.15 #formula de conversion de celsius a kelvin

print("Temperatura en Farenheit: ", farenheit)
print("Temperatura en Kelvin: ", kelvin)