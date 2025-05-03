a= float(input('Ingrese el primer numero: '))
b= float(input('Ingrese el segundo numero: '))
c= float(input('Ingrese el tercer numero: '))

discriminante= b**2-4*a*c

if discriminante>0:
    print('La solucion de la ecuacion tiene dos soluciones reales distintas ')
elif discriminante==0:
    print('La ecuacion cuadrática tiene una solución real repetida')
else: 
    print('Ninguna de las soluciones son números reales')