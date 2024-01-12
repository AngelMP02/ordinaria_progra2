# Dominio de Ingeniería Estructural
class StructuralDesign:
    def __init__(self, name):
        self.name = name

class StructuralMaterial:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

class StructuralElement:
    def __init__(self, design, material):
        self.design = design
        self.material = material
