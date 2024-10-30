#Hora futura
#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

#Hora actual: 3
#Cantidad de horas: 5
#En 5 horas, el reloj marcara las 8
#Hora actual: 11
#Cantidad de horas: 43
#En 43 horas, el reloj marcara las 6

t=float(input("Please write your current time: "))

# Solicitar al usuario el número de horas a añadir
h = int(input("Write an integer number of hours: "))

# Calcular la nueva hora
new_hour = (t + h) % 24  # Usar módulo 24 para volver a empezar al llegar a 24

# Mostrar la hora resultante
print(f"The hour after {h} hours will be: {new_hour:.2f}")
