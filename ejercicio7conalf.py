renta=int(input('Ingrese su renta anual: '))

if renta < 10000:
    print('El tipo de impositivo que le corresponde es del 5% ')
elif renta>=10000 and renta<20000:
    print('El tipo de impositivo que le corresponde es del 15%')
elif renta>=20000 and renta<35000:
    print('El tipo de impositivo que le corresponde es del 20%')
elif renta>=35000 and renta<60000:
    print('El tipo de impositivo que le corresponde es del 30%')
else:
    print('El tipo de impositivo que le corresponde es del 45%')