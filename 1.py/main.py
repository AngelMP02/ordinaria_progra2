# main.py
from edificio import *

from fabrica_edificios import *
from estilos import *


# Creación de prototipos
edificio_residencial_moderno = EdificioResidencial(Moderno())
edificio_comercial_clasico = EdificioComercial(Clasico())

# Creación de la fábrica
fabrica = FabricaEdificios()

# Establecer prototipos en la fábrica
fabrica.establecer_prototipo("residencial_moderno", edificio_residencial_moderno)
fabrica.establecer_prototipo("comercial_clasico", edificio_comercial_clasico)

# Crear nuevos edificios usando la fábrica
nuevo_edificio_residencial_moderno = fabrica.crear_edificio("residencial_moderno")
nuevo_edificio_comercial_clasico = fabrica.crear_edificio("comercial_clasico")

# Verificar clonación y atributos
print(isinstance(nuevo_edificio_residencial_moderno, EdificioResidencial))  # True
print(isinstance(nuevo_edificio_comercial_clasico, EdificioComercial))  # True
print(isinstance(nuevo_edificio_residencial_moderno.estilo, Moderno))  # True
print(isinstance(nuevo_edificio_comercial_clasico.estilo, Clasico))  # True
