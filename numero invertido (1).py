#Número invertido
#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

#Ingrese numero: 345
#543
#Ingrese numero: 241
#142

# Pedir al usuario que ingrese un número de tres dígitos
number= int(input("Please enter a three-digit integer number: "))
#// es floor divisiòn
# para sacar la unidad de cien (del 142) ver este numero como 100 saca el digito1
digit1 = number//100   
#para sacar la unidad de decena del digito(142)ver este numero como 42 
digit2 = (number//10)%10
#para sacar la uidad de decena del digito(142) seria 2
digit3 = number%10
numinv= (f" resultado {digit3*100+digit2*10+digit1}")
print (f"el resultado es {numinv}")


