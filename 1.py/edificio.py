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