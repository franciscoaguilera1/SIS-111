def calcular_descuento_producto():
    precio_original = 100
    descuento = 30 
    precio_descuento = (precio_original * descuento)/100
    precio_final = precio_original - precio_descuento
    return precio_final
def calcular_descuento_producto_mejorado(precio_original, descuento):
    precio_descuento = (precio_original * descuento)/100
    precio_final = precio_original - precio_descuento
    return precio_final
def calcular_descuento_producto_mejorado_x2(precio_original, descuento):
    precio_final = precio_original - (precio_original * descuento)/100
    return precio_final
def calcular_descuento_producto_mejorado_x3(precio_original, descuento):
    return precio_original * (1 - descuento / 100)

#1. Edad mínima para votar
def Edad_minima_para_votar():
    print("La edad minima es de 18 años")
#2. Número mayor entre dos números
def mayor_dos_num(num1, num2):
    if(num1 == num2): return "IGUALES"
    return num1 if (num1 > num2) else num2
#3. Algoritmo base
def recorrer_digitos(num):
    while(num > 0):
        dig = num % 10
        print(dig)
        num = num // 10
def suma_dig_num(num):
    suma = 0
    while(num > 0):
        dig = num % 10
        suma = suma + dig
        num = num // 10
    return suma

# salida Consola
var_suma = suma_dig_num(78234)
print(var_suma)
