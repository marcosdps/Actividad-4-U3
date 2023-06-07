from claseContratado import Contratado
from claseEmpleado import Empleado
from clasePlanta import Planta
from claseExterno import Externo
from manejadorEmpleado import ManejadorEmpleado


if __name__ == "__main__":
    mEmpleados = ManejadorEmpleado()
    i=0
    i=mEmpleados.cargarDatos("planta","planta.csv",i)
    i=mEmpleados.cargarDatos("contratado","contratado.csv",i)
    mEmpleados.cargarDatos("externo","externo.csv",i)

    interfaz = """\n---------MENU DE OPCIONES---------
    -1- Agregar horas trabajadas
    -2- Mostrar el monto de una tarea
    -3- Listar empleados que pueden recibir ayuda economica
    -4- Mostrar sueldos a cobrar y datos
    -5- Mostrar datos
    -0- SALIR"""
    print(interfaz)
    opcion = int(input("Ingrese una opcion: "))
    while opcion != 0:
        match opcion:
            case 1:
                dniBuscado = int(input("Ingrese el DNI: "))
                cantHoras = int(input("Horas trabajadas: "))
                mEmpleados.modificarCantHoras(dniBuscado, cantHoras)
            case 2:
                tareaAbuscar = input("Ingrese una tarea a buscar: ")
                mEmpleados.calcularMontoTarea(tareaAbuscar)
            case 3: 
                mEmpleados.ayudaEconomica()
            case 4:
                mEmpleados.mostrarSueldosYdatos()
            case 5:
                mEmpleados.mostrarDatos()
        print(interfaz)
        opcion = int(input("Ingrese una opcion: "))