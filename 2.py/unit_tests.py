import unittest
from architectural_domain import BuildingType, Building, ArchitecturalStyle
from structural_domain import StructuralDesign, StructuralElement, StructuralMaterial
from project_management_domain import Project, ConstructionStage

class TestBuildingAndConstruction(unittest.TestCase):

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

        # Verificar que el edificio esté en la etapa de construcción y en el proyecto
        self.assertEqual(len(house.construction_stages), 1)
        self.assertEqual(len(project.construction_stages), 1)
        self.assertEqual(len(construction_stage.buildings), 1)

    def test_project_status(self):
        # Crear un proyecto y una etapa de construcción
        project = Project("Dream Project")
        construction_stage = ConstructionStage("Foundation")

        # Agregar la etapa al proyecto
        project.add_construction_stage(construction_stage)

        # Verificar el estado inicial del proyecto
        self.assertEqual(project.get_project_status(), "Not Started")

        # Crear un edificio y agregarlo a la etapa de construcción
        house = Building("My House", BuildingType("Residential"), ArchitecturalStyle("Modern", []))
        house.add_construction_stage(construction_stage)

        # Verificar el estado actualizado del proyecto
        self.assertEqual(project.get_project_status(), "In Progress")

if __name__ == '__main__':
    unittest.main()
