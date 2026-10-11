class Paquete:
    def __init__(self,codigo,pesokilo,tarifa,seguroadicional):
        self.codigo=codigo
        self.pesokilo=pesokilo
        self.tarifa=tarifa
        
        self.__seguroadicional=seguroadicional

    @property

    def seguroadicional(self):
        return self.__seguroadicional
    @seguroadicional.setter
    def seguroadicional(self,valor):
        if valor<0:
            raise ValueError("El seguro no puede ser negativo ni ser cero")
        self.__seguroadicional=valor
    def costetotal(self):
        return self.tarifa + self.__seguroadicional

    def __str__(self):
        return (f"Codigo de producto:{self.codigo}, Peso: {self.pesokilo} , Coste Total del producto: {self.costetotal()}")
if __name__== "__main__":
    try:
        p1=Paquete(1,20,23.2,30.0)
        

        print(p1)
    except ValueError as e:
        print("Error ",e)
    try:
        p1=Paquete(1,20,23.2,30.0)
        p1.seguroadicional=-5.0
    
        print(p1)
    except ValueError as e:
        print("Error ",e)

    try:
        print(p1.__seguroadicional)
    except AttributeError as e:
        print(f"Error : {e}")