from architectural_domain import BuildingType,Building,ArchitecturalStyle
from structural_domain import StructuralDesign,StructuralElement,StructuralMaterial
def test_building_creation():
    residential_type = BuildingType("Residential")
    modern_style = ArchitecturalStyle("Modern", ["Simplicity", "Clean lines"])

    house = Building("My House", residential_type, modern_style)

    assert house.name == "My House"
    assert house.building_type == residential_type
    assert house.architectural_style == modern_style

def test_structural_element_creation():
    concrete_design = StructuralDesign("Concrete Design")
    steel_material = StructuralMaterial("Steel", 500)  # Strength in some unit

    column = StructuralElement(concrete_design, steel_material)

    assert column.design == concrete_design
    assert column.material == steel_material
