num1=float(input('Ingrese el primer numero: '))
num2=float(input('Ingrese el segundo numero: '))
num3=float(input('Ingrese el tercer numero: '))

if num1>num2 and num1>num3: 
    print('El numero 1 es el mayor')
elif num2>num1 and num2>num3:
    print('El numero 2 es el mayor')
else:
    print('El numero 3 es el mayor')
