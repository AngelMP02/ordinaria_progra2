from architectural_domain import BuildingType, ArchitecturalStyle, Building
from structural_domain import StructuralDesign, StructuralElement, StructuralMaterial
from project_management_domain import Project, ConstructionStage
from regulation_domain import Law, Regulation

class TestBuildingAndConstruction:

    def test_building_creation_and_construction_stage(self):
        # Crear tipos de edificios y estilos arquitectónicos
        residential_type = BuildingType("Residential")
        modern_style = ArchitecturalStyle("Modern", ["Simplicity", "Clean lines"])

        # Crear un edificio
        house = Building("My House", residential_type, modern_style)

        # Crear un proyecto
        project = Project("Dream Project")

        # Crear una etapa de construcción
        construction_stage = ConstructionStage("Foundation")

        # Agregar la etapa al proyecto
        project.add_construction_stage(construction_stage)

        # Agregar el edificio a la etapa de construcción y al proyecto
        house.add_construction_stage(construction_stage)

        # Imprimir los objetos
        print("Building:", house)
        print("Construction Stage Buildings:", construction_stage.buildings)
        print("Project Construction Stages Buildings:", project.construction_stages[0].buildings)

    def test_project_status(self):
        # Crear un proyecto y una etapa de construcción
        project = Project("Dream Project")
        construction_stage = ConstructionStage("Foundation")

        # Agregar la etapa al proyecto
        project.add_construction_stage(construction_stage)

        # Imprimir el estado inicial del proyecto
        print("Initial Project Status:", project.get_project_status())

        # Crear un edificio y agregarlo a la etapa de construcción
        house = Building("My House", BuildingType("Residential"), ArchitecturalStyle("Modern", []))
        house.add_construction_stage(construction_stage)

        # Imprimir el estado actualizado del proyecto
        print("Updated Project Status:", project.get_project_status())

# Crear una instancia de las pruebas y ejecutarlas
tests = TestBuildingAndConstruction()
tests.test_building_creation_and_construction_stage()
tests.test_project_status()
