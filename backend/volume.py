import math

class Volume:
    """
    Calculate the volume for 3D shapes
    Definitions:
    - calculate_volume_cube
    - calculate_volume_cuboid
    - calculate_volume_cylinder
    - calculate_volume_cone
    - calculate_volume_sphere
    - calculate_volume_hemisphere
    """
    
    def __init__(self, length=0, width=0, height=0, radius=0):
        self.length = length
        self.width = width
        self.height = height
        self.radius = radius

    @staticmethod
    def calculate_volume_cube(length):
        """
        Function to calculate the volume of a cube
        :param length: Length of the cube's side
        :return: Total volume calculated
        """
        return length ** 3

    @staticmethod
    def calculate_volume_cuboid(length, width, height):
        """
        Function to calculate the volume of a cuboid
        :param length: Length of the cuboid
        :param width: Width of the cuboid
        :param height: Height of the cuboid
        :return: Total volume calculated
        """
        return length * width * height

    @staticmethod
    def calculate_volume_cylinder(radius, height):
        """
        Function to calculate the volume of a cylinder
        :param radius: Radius of the cylinder's base
        :param height: Height of the cylinder
        :return: Total volume calculated
        """
        return math.pi * (radius ** 2) * height
    
    @staticmethod
    def calculate_volume_cone(radius, height):
        """
        Function to calculate the volume of a cone
        :param radius: Radius of the cone's base
        :param height: Height of the cone
        :return: Total volume calculated
        """
        return (1/3) * math.pi * (radius ** 2) * height
    
    @staticmethod
    def calculate_volume_sphere(radius):
        """
        Function to calculate the volume of a sphere
        :param radius: Radius of the sphere
        :return: Total volume calculated
        """
        return (4/3) * math.pi * (radius ** 3)
    
    @staticmethod
    def calculate_volume_hemisphere(radius):
        """
        Function to calculate the volume of a hemisphere
        :param radius: Radius of the hemisphere
        :return: Total volume calculated
        """
        return (1/2) * (4/3) * math.pi * (radius ** 3)
    
