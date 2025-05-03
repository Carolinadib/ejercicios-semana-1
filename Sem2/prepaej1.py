precio=float(input('Ingrese el precio de su producto: '))
membresia= input('Ingrese si tiene membresia o no: \n1.Si \n2. No')

if precio>=50 and membresia=='1':
    print(f'Usted tiene un descuento del 15% en su compra y le quedaria en {precio-(precio*0.15)}')
elif membresia=='1':
    print(f'Usted tiene un descuento del 10% quedando el producto en {precio-(precio*0.10)}')
elif precio>= 50:
    print(f'Usted tiene un descuento de 5% en su producto {precio-(precio*0.05)}')
else:
    print('Usted no posee nigun descuento')