anoactual= 2025
anonacimiento=int(input('Ingrese su ano de nacimiento: '))

edad= anoactual-anonacimiento

if edad<13:
    print(f'Usted tiene {edad} anos y se encuentra en la etapa de Infancia')
elif 13<=edad<20:
    print(f'Usted tiene {edad} anos y se encuentra en la Adolescencia')
elif 20<=edad<65:
    print(f'Usted tiene {edad} anos y se encuentra en la etapa de la Adultez')
else:
    print(f'Usted pertenece a la tercera edad y tiene {edad} anos')