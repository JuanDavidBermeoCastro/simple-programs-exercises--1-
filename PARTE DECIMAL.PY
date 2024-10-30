#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

#Ingrese un numero: 4.5
#0.5
#Ingrese un numero: -1.19
#0.19

# Solicitar al usuario que ingrese un número real
number = float(input("Please enter a real number: "))

# Calcular la parte decimal
decimal_part = number- int(number)

# Mostrar la parte decimal
print(f"The decimal part of {number} is: {decimal_part:.2f}")
