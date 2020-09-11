#PARTICIPANTES
#Kevin arredondo
#kevin cardenas 
#cristian cantillo
emples = {}
option = ''
#cristian cantillo
while option != '6':
    if option == '1':
        ide= input('Introduce IDE del empleado: ')
        name = input('Introduce el nombre del empleado: ')
        cargo = input('Introduce la Cargo del empleado: ')
        sal = input('Introduce el salario del empleado: ')
        emple = {'nombre':name, 'Cargo':cargo, 'salario':sal}
        emples[ide] = emple

        #kevin arredondo
    if option == '2':
        ide = input('Introduce IDE del empleado: ')
        if ide in emples:
            del emples[ide]
        else:
            print('No existe el empleado con el id', ide)
    if option == '3':
        id = input('Introduce IDE del empleado: ')
        if id in emples:
            print('IDE:', ide)
            for key, value in emples[ide].items():
                print(key.title() + ':', value)
        else:
            print('No existe el empleado con el ide', ide)

            #Kevin cardenas
    if option == '4':
        print('Lista de empleados')
        for key, value in emples.items():
            print(key, value['nombre'])
    
    option = input('Menú de opciones\n(1) Añadir empleado\n(2) Eliminar empleado\n(3) Mostrar empleado\n(4) Listar empleados\n(6) Terminar\nElige una opción:')