# fabrica_edificios.py
from abc import ABC, abstractmethod
from edificio import EdificioResidencial, EdificioComercial, EdificioIndustrial

class CreadorEdificios(ABC):
    @abstractmethod
    def crear_edificio(self):
        pass

class CreadorResidencial(CreadorEdificios):
    def __init__(self, estilo, numero_habitaciones):
        self.estilo = estilo
        self.numero_habitaciones = numero_habitaciones

    def crear_edificio(self):
        return EdificioResidencial(self.estilo, self.numero_habitaciones)

class CreadorComercial(CreadorEdificios):
    def __init__(self, estilo, area_venta):
        self.estilo = estilo
        self.area_venta = area_venta

    def crear_edificio(self):
        return EdificioComercial(self.estilo, self.area_venta)

class CreadorIndustrial(CreadorEdificios):
    def __init__(self, estilo, capacidad_produccion):
        self.estilo = estilo
        self.capacidad_produccion = capacidad_produccion

    def crear_edificio(self):
        return EdificioIndustrial(self.estilo, self.capacidad_produccion)
