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
