## primos
cont=0
a=int(input("Por favor ingrese un numero "))
for i in range(1,a+1,1):
  if a % i == 0:
    cont=cont+1
    
if cont > 2:
  print("El numero", a, "no es primo")
else:
  print("El numero", a, "si es primo")
  
