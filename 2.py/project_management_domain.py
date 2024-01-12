# project_management_domain.py

class Project:
    def __init__(self, name):
        self.name = name
        self.construction_stages = []

    def add_construction_stage(self, construction_stage):
        self.construction_stages.append(construction_stage)

    def get_project_status(self):
        if any(construction_stage.buildings for construction_stage in self.construction_stages):
            return "In Progress"
        else:
            return "Not Started"
class ConstructionStage:
    def __init__(self, name):
        self.name = name
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)