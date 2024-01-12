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