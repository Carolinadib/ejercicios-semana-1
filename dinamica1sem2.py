# Piedra, papel o tijera
jugador1=input('El jugador 1 ingrese su opcion: ')
jugador2=input('El jugador 2 ingrese su opcion: ')

if jugador1==jugador2 :
    print('Empate')
elif (jugador1=='piedra'and jugador2=='papel') or (jugador1=='papel'and jugador2=='tijera') or (jugador1=='tijera' and jugador2=='piedra'):
    print('Gana el jugador 2')
else:
    print('Gana el jugador 1')