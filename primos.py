## primos
a=int(input("Por favor ingrese un numero "))
for i in range(1,a+1,1):
  res = a/i 
  print("El residuo entre", a, "y", i, "es:", res)
