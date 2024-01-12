# project_management_domain.py

class Project:
    def __init__(self, name):
        self.name = name
        self.construction_stages = []

    def add_construction_stage(self, construction_stage):
        self.construction_stages.append(construction_stage)

   
    def get_project_status(self):
        # Devolver el estado actual del proyecto
        pass

class ConstructionStage:
    def __init__(self, name):
        self.name = name
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)
