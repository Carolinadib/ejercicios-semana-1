print('Bienvenido a la pizzeria Bella Napoli')
print('Ingrese el tipo de pizza que desea: \n1. Vegatariana\n2. No Vegetariana')
cliente=input('Seleccione la opcion correspondiente: ')

if cliente== '1' :
    print('Los ingredientes para las pizzas vegetarianas son: \n1. Pimiento \n2. Tofu')
    opcion1=input('Indique los ingredientes que quiere en la pizza: ')
    print(f'Su pizza es vegetariana con tomate, mozarella y {opcion1}')
else:
    print('Los ingredientes para las pizzas no vegetarianas son: \n1. Peperoni \n2. Jamon \n3. Salmon ')
    opcion2=input('Indique los ingredientes que quiere en la pizza: ')
    print(f'Su pizza es una no vegetariana con tomate, mozarella y {opcion2}')
print('Gracias por su compra')