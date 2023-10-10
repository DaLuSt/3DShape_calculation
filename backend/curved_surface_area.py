import math
from surface_area import SurfaceArea

class CurvedSurfaceArea:
    """
    Calculate the curved surface area for 3D shapes
    Definitions:
    - calculate_curved_area_cube
    - calculate_curved_area_cuboid
    - calculate_curved_area_cylinder
    - calculate_curved_area_cone
    - calculate_curved_area_sphere
    - calculate_curved_area_hemisphere
    """

    def __init__(self, length=0, width=0, height=0, radius=0):
        self.length = length
        self.width = width
        self.height = height
        self.radius = radius

    @staticmethod
    def calculate_curved_area_cube(length):
        """
        Function to calculate the curved surface area of a cube
        :param length: Length of the cube's side
        :return: Total curved surface area calculated
        """
        square_area = SurfaceArea.calculate_area_square(length)
        return 4 * square_area
    
    @staticmethod
    def calculate_curved_area_cuboid(length, width, height):
        """
        Function to calculate the curved surface area of a cuboid
        :param length: Length of the cuboid
        :param width: Width of the cuboid
        :param height: Height of the cuboid
        :return: Total curved surface area calculated
        """
        return 2 * (height * (length + width))

    @staticmethod
    def calculate_curved_area_cylinder(radius, height):
        """
        Function to calculate the curved surface area of a cylinder
        :param radius: Radius of the cylinder's base
        :param height: Height of the cylinder
        :return: Total curved surface area calculated
        """
        return 2 * math.pi * radius * height

    @staticmethod
    def calculate_curved_area_cone(radius, height):
        """
        Function to calculate the curved surface area of a cone
        :param radius: Radius of the cone's base
        :param height: Height of the cone
        :return: Total curved surface area calculated
        """
        slant_height = math.sqrt(radius ** 2 + height ** 2)
        return math.pi * radius * slant_height

    @staticmethod
    def calculate_curved_area_sphere(radius):
        """
        Function to calculate the curved surface area of a sphere
        :param radius: Radius of the sphere
        :return: Total curved surface area calculated
        """
        return 4 * math.pi * radius ** 2

    @staticmethod
    def calculate_curved_area_hemisphere(radius):
        """
        Function to calculate the curved surface area of a hemisphere
        :param radius: Radius of the hemisphere
        :return: Total curved surface area calculated
        """
        return 2 * math.pi * radius ** 2
