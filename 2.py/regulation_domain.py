# regulation_domain.py

class Law:
    def __init__(self, name):
        self.name = name

class Regulation:
    def __init__(self, law, restrictions):
        self.law = law
        self.restrictions = restrictions

   
    def check_compliance(self, building):
        # Lógica para verificar el cumplimiento de las regulaciones por parte de un edificio
        pass
