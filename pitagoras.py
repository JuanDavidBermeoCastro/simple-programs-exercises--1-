#Escriba un programa que reciba como entrada las longitudes de los dos catetos a
#y b
#de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
#del triangulo, dado por el teorema de Pitágoras: c2=a2+b2


#Ingrese cateto a: 7
#Ingrese cateto b: 5
#La hipotenusa es 8.6023252670426267

catetoA= float(input("write cateto 1: "))
catetoB= float(input("write cateto 2: "))

RESULT= (catetoA**2/0.5+catetoB**2/0.5)
print (f"result is:  {RESULT}")
