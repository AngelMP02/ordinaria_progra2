# main.py
from edificio import *
from estilos import *
from fabrica_edificios import *

# Crear instancias de estilos arquitectónicos
estilo_moderno = Moderno()
estilo_clasico = Clasico()
estilo_futurista = Futurista()

# Creación de fábricas
fabrica_residencial_moderno = CreadorResidencial(Moderno(), numero_habitaciones=3)
nuevo_edificio_residencial = fabrica_residencial_moderno.crear_edificio()

fabrica_comercial_clasico = CreadorComercial(Clasico(), area_venta=1000)
nuevo_edificio_comercial = fabrica_comercial_clasico.crear_edificio()

fabrica_industrial_futurista = CreadorIndustrial(Futurista(), capacidad_produccion=500)
nuevo_edificio_industrial = fabrica_industrial_futurista.crear_edificio()

# Verificar clonación y atributos
print(nuevo_edificio_residencial)  # Imprime la instancia directamente
print(nuevo_edificio_comercial)    # Imprime la instancia directamente
print(nuevo_edificio_industrial)   # Imprime la instancia directamente
print(nuevo_edificio_residencial.estilo)  # Imprime la instancia del estilo directamente
print(nuevo_edificio_comercial.estilo)    # Imprime la instancia del estilo directamente
print(nuevo_edificio_industrial.estilo)   # Imprime la instancia del estilo directamente
