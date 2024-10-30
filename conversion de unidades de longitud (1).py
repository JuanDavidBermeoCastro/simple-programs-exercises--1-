#Conversión de unidades de longitud
#Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.

#Ingrese longitud: 45
#45 cm = 17.7165 in
#Ingrese longitud: 13
#13 cm = 5.1181 in

#le pido al usuario que ingrese los centimetros 
longitud= float(input("enter centimeters: "))
#hago la operacion de conversion asignandole un valor a las pulgadas para posteriormente multiplicarlas por los centimetros 
pulgada=2.4 
conversion = (pulgada* longitud)
#creo una salida para mostrar el resultado 
print(f"the conversion is equal to:  {conversion}")


