from claseEmpleado import Empleado

class Externo(Empleado):
    __tarea: str
    __fechaInicio: str
    __fechaFinalizacion: str
    __montoViatico: float
    __costoObra: float
    __seguroDeVida: float

    def __init__(self, dni=None, nombre=None, direccion=None, telefono=None, tarea=None, fechaInicio=None,
                 fechaFinalizacion=None, montoViatico=None, costoObra=None, seguroDeVida=None):
        super().__init__(dni, nombre, direccion, telefono)
        self.__tarea = tarea
        self.__fechaInicio = fechaInicio
        self.__fechaFinalizacion = fechaFinalizacion
        self.__montoViatico = float(montoViatico)
        self.__costoObra = float(costoObra)
        self.__seguroDeVida = float(seguroDeVida)

    def mostrarExterno(self):
        print(f"{self.getNombre()} {self.getDNI()} {self.getDireccion()} {self.getTelefono()} {self.__tarea} {self.__fechaInicio} {self.__fechaFinalizacion} {self.__montoViatico} {self.__costoObra} {self.__seguroDeVida}")

    def getTarea(self):
        return self.__tarea
    
    def getCostoObra(self):
        return self.__costoObra
    
    def getFechaFinalizacion(self):
        return self.__fechaFinalizacion
    
    def sueldo(self):
        return(self.__costoObra - self.__montoViatico - self.__seguroDeVida)