from claseEmpleado import Empleado

class Planta(Empleado):
    __sueldoBasico: float
    __antiguedad: float

    def __init__(self, dni=None, nombre=None, direccion=None, telefono=None, sueldoBasico =None, antiguedad=None):
        super().__init__(dni, nombre, direccion, telefono)
        self.__sueldoBasico = float(sueldoBasico)
        self.__antiguedad = float(antiguedad)

    def mostrarPlanta(self):
        print(f"{self.getNombre()} {self.getDNI()} {self.getDireccion()} {self.getTelefono()} {self.__sueldoBasico} {self.__antiguedad}")

    def sueldo(self):
        return(self.__sueldoBasico + ((0.01*self.__sueldoBasico)*self.__antiguedad))
