edadcliente=int(input('Ingrese su edad: '))
if edadcliente <= 4 :
    print('Su entrada es gratis')
elif edadcliente > 4 and edadcliente<=18 :
    print('Su entrada cuesta 5 euros')
else:
    print('Su entrada cuesta 10 euros')