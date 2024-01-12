# unit_tests.py

import unittest
from architectural_domain import BuildingType, Building, ArchitecturalStyle
from structural_domain import StructuralDesign, StructuralElement, StructuralMaterial

class TestBuildingAndStructuralElementCreation(unittest.TestCase):

    def test_building_creation(self):
        residential_type = BuildingType("Residential")
        modern_style = ArchitecturalStyle("Modern", ["Simplicity", "Clean lines"])

        house = Building("My House", residential_type, modern_style)

        self.assertEqual(house.name, "My House")
        self.assertEqual(house.building_type, residential_type)
        self.assertEqual(house.architectural_style, modern_style)

    def test_structural_element_creation(self):
        concrete_design = StructuralDesign("Concrete Design")
        steel_material = StructuralMaterial("Steel", 500)  # Strength in some unit

        column = StructuralElement(concrete_design, steel_material)

        self.assertEqual(column.design, concrete_design)
        self.assertEqual(column.material, steel_material)

if __name__ == '__main__':
    unittest.main()
