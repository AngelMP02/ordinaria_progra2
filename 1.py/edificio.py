# edificio.py
from abc import ABC, abstractmethod

class Edificio(ABC):
    def __init__(self, estilo):
        self.estilo = estilo

    @abstractmethod
    def duplica(self):
        pass

class EdificioResidencial(Edificio):
    def __init__(self, estilo, numero_habitaciones):
        super().__init__(estilo)
        self.numero_habitaciones = numero_habitaciones

    def duplica(self):
        return EdificioResidencial(self.estilo, self.numero_habitaciones)

class EdificioComercial(Edificio):
    def __init__(self, estilo, area_venta):
        super().__init__(estilo)
        self.area_venta = area_venta

    def duplica(self):
        return EdificioComercial(self.estilo, self.area_venta)

class EdificioIndustrial(Edificio):
    def __init__(self, estilo, capacidad_produccion):
        super().__init__(estilo)
        self.capacidad_produccion = capacidad_produccion

    def duplica(self):
        return EdificioIndustrial(self.estilo, self.capacidad_produccion)
