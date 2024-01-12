# Dominio de Regulación
class Law:
    def __init__(self, name):
        self.name = name

class Regulation:
    def __init__(self, law, restrictions):
        self.law = law
        self.restrictions = restrictions