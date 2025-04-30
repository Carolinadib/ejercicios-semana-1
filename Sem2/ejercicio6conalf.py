nombre=input('Ingrese su nombre: ')
sexo=input('Ingrese su sexo F o M: ')
if (sexo=='F'and nombre.lower() < 'm') or (sexo=='M' and nombre.lower() >'n'):
    print('Usted pertenece al grupo A')
else:
    print('Usted pertenece al grupo B')