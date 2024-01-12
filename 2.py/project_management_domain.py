class Project:
    def __init__(self, name):
        self.name = name
        self.construction_stages = []

    def add_construction_stage(self, construction_stage):
        self.construction_stages.append(construction_stage)

class ConstructionStage:
    def __init__(self, name):
        self.name = name
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)