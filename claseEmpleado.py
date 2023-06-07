

class Empleado:
    __dni: int
    __nombre: str
    __direccion: str
    __telefono: str

    def __init__(self, dni=None, nombre=None, direccion=None, telefono=None):
        self.__dni = int(dni)
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    def getDNI(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def mostrarDatosSubsidiado(self):
        print(f"{self.__nombre} {self.__dni} {self.__direccion}")

    def nomYtel(self):
        print(f"{self.__nombre} {self.__telefono}")

