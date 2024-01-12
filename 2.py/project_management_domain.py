# Dominio de Gestión de Proyectos
class Project:
    def __init__(self, name):
        self.name = name
        self.stages = []

    def add_stage(self, stage):
        self.stages.append(stage)

class ConstructionStage:
    def __init__(self, name):
        self.name = name