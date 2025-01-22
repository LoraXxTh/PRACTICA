##4. Crear un archivo.py, escribir un Hola mundo que se imprima en consola.

print("Hola mundo")

##5. Escribir un programa que salude con el nombre de entrada desde teclado
##Input: "Gianmarco"
##Output: "Hola, Gianmarco"

nombre = input("¿Cuál es tu nombre?: ")
print("Hola,", nombre)

##6. Escribe un programa que pida tu edad y muestre si es mayor de edad o no lo es.

edad = int(input("¿cual es tu edad?: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Aún no eres mayor de edad.")

##7. Escribe un programa que pida un numero entero y determine si es par o impar

numero = int(input("Elige un número entero: "))

if numero % 2 == 0:
    print(numero, "es par.")
else:
    print(numero, "es impar.")

##8. Escribe un program que que pida un numero entero y calcule la suma de 1 hasta el numero ingresado.
##Usar formula de suma de numeros enteros
#formula = (n*(n+1)/2)

n = int(input("Ingrese un número entero: "))

resultado = int(n*(n+1)/2)
print ("Sumatoria de números desde 1 hasta el " + str(n) + "es: " + str(resultado))