from architectural_domain import BuildingType, ArchitecturalStyle, Building
from structural_domain import StructuralDesign, StructuralMaterial, StructuralElement
from project_management_domain import Project, ConstructionStage
from regulation_domain import Law, Regulation
from unit_tests import test_building_creation, test_structural_element_creation

if __name__ == "__main__":
    test_building_creation()
    test_structural_element_creation()
    # Llamar a más pruebas según sea necesario
