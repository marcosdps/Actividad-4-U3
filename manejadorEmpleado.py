from claseEmpleado import Empleado
from clasePlanta import Planta
from claseContratado import Contratado
from claseExterno import Externo
import datetime
import numpy as np
import csv

class ManejadorEmpleado:

    def __init__(self):
        self.__arregloEmpleados = np.empty(int(input("Ingrese la cantidad de empleados de la empresa: ")),dtype = Empleado)
    

    def cargarDatos(self,tipo, archi_A_leer, i):
        with open(archi_A_leer,"r")as archi:
            reader = csv.reader(archi, delimiter=";")
            for fila in reader:
                if tipo == "planta":
                    self.__arregloEmpleados[i] = Planta(*fila)
                elif tipo == "contratado":
                    self.__arregloEmpleados[i] = Contratado(*fila)
                elif tipo == "externo":
                    self.__arregloEmpleados[i] = Externo(*fila)
                i +=1
        return i
    
    def mostrarDatos(self):
        for i in range(15):
            if i<5:
                self.__arregloEmpleados[i].mostrarPlanta()
            elif i>=5 and i<10:
                self.__arregloEmpleados[i].mostrarContratado()
            elif i>=10:
                self.__arregloEmpleados[i].mostrarExterno()

    def modificarCantHoras(self, dniBuscado, cantHoras):
        i=0
        while i<self.__arregloEmpleados.size and dniBuscado != self.__arregloEmpleados[i].getDNI():
            i +=1
        if i< self.__arregloEmpleados.size:
            self.__arregloEmpleados[i].modificarHoras(cantHoras)

    def calcularMontoTarea(self, tareaAbuscar):
        monto =0
        for i in range(self.__arregloEmpleados.size):
            if type(self.__arregloEmpleados[i]) == Externo:
                if tareaAbuscar == self.__arregloEmpleados[i].getTarea():
                    fecha = datetime.datetime.strptime(self.__arregloEmpleados[i].getFechaFinalizacion(), "%d/%m/%Y")
                    if fecha > datetime.datetime.now():
                        monto += self.__arregloEmpleados[i].getCostoObra()
                        print(f"Monto a pagar: {monto}")
                
    def ayudaEconomica(self):
        for i in range(self.__arregloEmpleados.size):  
            if self.__arregloEmpleados[i].sueldo() < 150000:
                self.__arregloEmpleados[i].mostrarDatosSubsidiado()

    def mostrarSueldosYdatos(self):
        for i in range(self.__arregloEmpleados.size):  
            print(self.__arregloEmpleados[i].sueldo())
            self.__arregloEmpleados[i].nomYtel()