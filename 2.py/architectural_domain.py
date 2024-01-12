#dominio arquitectura


class BuildingType:
    def __init__(self, name):
        self.name = name

class ArchitecturalStyle:
    def __init__(self, name, characteristics):
        self.name = name
        self.characteristics = characteristics

class Building:
    def __init__(self, name, building_type, architectural_style):
        self.name = name
        self.building_type = building_type
        self.architectural_style = architectural_style
        self.construction_stages = []

    def add_construction_stage(self, construction_stage):
        self.construction_stages.append(construction_stage)
        construction_stage.add_building(self)

