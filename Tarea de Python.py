#Trabajo 
#Ejercicio uno, decidir si los siguientes 5 nuemeros estan en orden ascendente, descendente y aleatorio
num1 = int(input("Ingresar el primer número: "))
num2 = int(input("Ingresar el segundo número: "))
num3 = int(input("Ingresar el tercer número: "))
num4 = int(input("Ingresar el cuerto número: "))
num5 = int(input("Ingresar el quinto número: "))
if num1 <= num2 and num2 <= num3 and num3 <= num4 and num4 <= num5
  dato = "EL ORDEN ES ASCENDENTE"
elif num1 >= num2 and num2 >= num3 and num3 >= num4 and num4 >= num5
  dato = "EL ORDEN ES DESCENDENTE"
else:
  dato: "EL ORDEN ES ALEATORIO"
print(dato)
#Busqueda de numero en la lista
nu1 = int(input("Ingresar el primer número: "))
nu2 = int(input("Ingresar el segundo número: "))
nu3 = int(input("Ingresar el tercer número: "))
nu4 = int(input("Ingresar el cuerto número: "))
bus1 = int(input("Ingresar el número de busqueda: "))
if nu1 == bus1 or nu2 == bus1 or nu3 == bus1 or nu4 == bus1
  busqueda = "Numero encontrado en la lista"
else :
  busqueda = "Numero no encontrado en la lista"
#Digitos pares e impares de un numero 
num = int(input("Ingrese el numero: "))
num_par = 0
num_impar = 0
while numero > 0:
    digito = num % 10
    if digito % 2 == 0:
        num_par += 1
    else:
        num_impar += 1
    num = num // 10    
print("Pares: ", num_par)
print("Impares: ", num_impar)
# Promedio de equipos y verificar cual fue el mejor
P1A = int(input("Ingrese los puntos del primer partido del equipo A: "))
P2A = int(input("Ingrese los puntos del segundo partido del equipo A: "))
P3A = int(input("Ingrese los puntos del tercero partido del equipo A: "))
P4A = int(input("Ingrese los puntos del cuarto partido del equipo A: "))
P5A = int(input("Ingrese los puntos del quinto partido del equipo A: "))
promedioA = statistics.mean([P1A, P2A, P3A, P4A, P5A])
P1B = int(input("Ingrese los puntos del primer partido del equipo B: "))
P2B = int(input("Ingrese los puntos del segundo partido del equipo B: "))
P3B = int(input("Ingrese los puntos del tercero partido del equipo B: "))
P4B = int(input("Ingrese los puntos del cuarto partido del equipo B: "))
P5B = int(input("Ingrese los puntos del quinto partido del equipo B: "))
promedioB = statistics.mean([P1B, P2B, P3B, P4B, P5B])
if promedioA > promedioB
  print("El equipo A tiene el mayor promedio de, ",promedioA)
elif promedioB > promedioA
  print("El equipo B tiene el mayor promedio de, ",promedioB)
else promedioA == promedioB 
  print("Los dos equipos tienen el mismo promedio de, ",promedioA)
#Producto mayor de dos numeros
numeros = []
for p in range(4):
    num = int(input("Ingrese numeros a la lista: "))
    numeros.append(num)
producto = numeros[0]*numeros[1]
producto_mayor = 0
for p in range(4):
    for l in range(p + 1, 4):
        producto = numeros[p]*numeros[l]
if producto > producto_mayor:
    producto_mayor = producto
print("el producto mayor es:",producto_mayor)
#Meta de ahorro
meta = int(input("¿Cual es su meta de ahorro?  "))
ingreso_diario = float(input("¿Cuanto dinero desea ingresar hoy?  "))
incremento = int(input("¿Cuanto incrementara su ahorro diario?  "))
Totalh = 0
contadord = 0
while Totalh < meta:
    Totalh = Totalh + ingreso_diario
    ingresod = ingresod + incremento
    contadord = contadord + 1 
print("Se estima un tiempo de: ", contadord, "dias." )
#Verificador de numeros palidromos
numer = (input("Ingrese un numero: "))
opne = 0
end = len(numer) - 1
es_palindromo = True
while open < end:
    if numer[open] != numer[end]:
        es_palindromo = False
    open = open + 1
    end = end - 1
if es_palindromo:
    print("Es un palindromo")
else:
    print("no es un palindromo")
# combinaciones posibles
numersx = []
for i in range(4):
    nume = int(input("ingrese un numero a la lista: "))
    numersx.append(nume)
print("posibles combinacioes:")
for i in range(len(numersx)):
    for j in range(i + 1, len(numers)):
        print(f"({numersx[i]}, {numersx[j]})")
# Verificador de un numero primo
numberx = int(input("Ingresa un número: "))
esp = True
if numberx <= 1:
    esp = False
else:
    divisor = 2
    while divisor < numberx:
        if numberx % divisor == 0:
            esp = False
            break
        divisor += 1
if esp:
    print("Es primo")
else:
    print("No es primo") 
# Suma de números pares
nume = []
# Pedimos 6 números al usuario y sumamos los pares
for i in range(6):
    num = int(input("Ingresa un número: "))
    nume.append(num)
suma_pares = 0
for n in nume:
    if n % 2 == 0:
        suma_pares += n
print("La suma de los números pares es:", suma_pares)









