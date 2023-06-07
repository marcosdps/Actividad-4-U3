from claseEmpleado import Empleado

class Contratado(Empleado):
    __fechaInicio: str
    __fechaFinalizacion: str
    __cantHrsTrabajadas: float
    __valorXhr: float

    def __init__(self, dni=None, nombre=None, direccion=None, telefono=None, fechaInicio=None, 
                fechaFinalizacion = None,cantHrsTrabajadas=None, valorXhr=None):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fechaInicio = fechaInicio
        self.__fechaFinalizacion = fechaFinalizacion
        self.__cantHrsTrabajadas = float(cantHrsTrabajadas)
        self.__valorXhr = float(valorXhr)

    def mostrarContratado(self):
        print(f"{self.getNombre()} {self.getDNI()} {self.getDireccion()} {self.getTelefono()} {self.__fechaInicio} {self.__fechaFinalizacion} {self.__cantHrsTrabajadas} {self.__valorXhr}")


    def modificarHoras(self,cantHoras):
        self.__cantHrsTrabajadas += cantHoras

    def sueldo(self):
        return(self.__cantHrsTrabajadas*self.__valorXhr)
