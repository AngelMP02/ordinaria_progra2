# unit_tests.py

import unittest
from architectural_domain import BuildingType, Building, ArchitecturalStyle
from structural_domain import StructuralDesign, StructuralElement, StructuralMaterial
from project_management_domain import Project, ConstructionStage
from regulation_domain import Law, Regulation

class TestBuildingAndConstruction(unittest.TestCase):

    def test_building_creation_and_construction_stage(self):
        residential_type = BuildingType("Residential")
        modern_style = ArchitecturalStyle("Modern", ["Simplicity", "Clean lines"])

        house = Building("My House", residential_type, modern_style)

        self.assertEqual(house.name, "My House")
        self.assertEqual(house.building_type, residential_type)
        self.assertEqual(house.architectural_style, modern_style)

        project = Project("Dream Project")
        construction_stage = ConstructionStage("Foundation")

        house.add_construction_stage(construction_stage)
        project.add_construction_stage(construction_stage)

        self.assertEqual(len(house.construction_stages), 1)
        self.assertEqual(len(project.construction_stages), 1)
        self.assertEqual(len(construction_stage.buildings), 1)

if __name__ == '__main__':
    unittest.main()
