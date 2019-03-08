## primosB
cont=0
i=0
a=int(input("Por favor ingrese un numero "))
while i<a+1:
  i=i+1
  if a % i == 0:
    cont=cont+1
    
if cont > 2:
  print("El numero", a, "no es primo")
else:
  print("El numero", a, "si es primo")