# Definición de clases
class Edificio:
    def __init__(self, estilo):
        self.estilo = estilo

    def duplica(self):
        pass

class EdificioResidencial(Edificio):
    def __init__(self, estilo):
        super().__init__(estilo)
        # Atributos específicos de EdificioResidencial

    def duplica(self):
        return EdificioResidencial(self.estilo)

class EdificioComercial(Edificio):
    def __init__(self, estilo):
        super().__init__(estilo)
        # Atributos específicos de EdificioComercial

    def duplica(self):
        return EdificioComercial(self.estilo)

class EdificioIndustrial(Edificio):
    def __init__(self, estilo):
        super().__init__(estilo)
        # Atributos específicos de EdificioIndustrial

    def duplica(self):
        return EdificioIndustrial(self.estilo)

class EstiloArquitectonico:
    def duplica(self):
        pass

class Moderno(EstiloArquitectonico):
    def duplica(self):
        return Moderno()

class Clasico(EstiloArquitectonico):
    def duplica(self):
        return Clasico()

class Futurista(EstiloArquitectonico):
    def duplica(self):
        return Futurista()

class FabricaEdificios:
    def __init__(self):
        self.prototipos = {}

    def establecer_prototipo(self, tipo, prototipo):
        self.prototipos[tipo] = prototipo

    def crear_edificio(self, tipo):
        try:
            prototipo = self.prototipos[tipo]
            return prototipo.duplica()
        except KeyError:
            raise ValueError(f"No se ha establecido un prototipo para el tipo de edificio: {tipo}")

# Código de prueba
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
