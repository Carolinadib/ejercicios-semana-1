print('Puntuacion que le da al empleado: \n1. 0.0  \n2. 0.4  \n3. 0.6 o mas')
puntuacion=float(input('Puntuacion que le da al empleado:'))

if puntuacion==0.0:
    print(f'Su nivel es INACEPTABLE y recibira {puntuacion*2400} dolares ')
elif puntuacion==0.4:
    print(f'Su nivel es ACEPTABLE y recibira {puntuacion*2400} dolares')
else:
    print(f'Su nivel es MERITORIO y recibira {puntuacion*2400} dolares')