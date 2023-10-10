"""
author: Daan Steur
Version: 1
Date: January 16 2022
classes: 
Volume: Calculate the volume for 3D shapes
CurvedSurfaceArea: Calculate the curved surface area for 3D shapes
SurfaceArea: Calculate the total surface area of shapes and 3D shapes
Licence: MIT
"""
# import libaries
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


    def calculate_volume_cube(self):
        """
        Function to calculate the volume of a cube
        :return: total volume calculated
        """
        return self.length ** 3

    def calculate_volume_cuboid(self):
        """
        Function to calculate the volume of a cuboid
        :return: total volume calculated
        """
        return self.length * self.width * self.height

    def calculate_volume_cylinder(self):
        """
        Function to calculate the volume of a cylinder
        :return: total volume calculated
        """
        return math.pi * (self.radius ** 2) * self.height

    def calculate_volume_cone(self):
        """
        Function to calculate the volume of a cone
        :return: total volume calculated
        """
        return (1/3) * math.pi * (self.radius ** 2) * self.height

    def calculate_volume_sphere(self):
        """
        Function to calculate the volume of a sphere
        :return: total volume calculated
        """
        return (4/3) * math.pi * self.radius ** 3

    def calculate_volume_hemisphere(self):
        """
        Function to calculate the volume of a hemisphere
        :return: total volume calculated
        """
        return (2/3) * math.pi * self.radius ** 3


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

    def calculate_curved_area_cube(self):
        """
        Function to calculate the curved surface area of a cube
        :return: total curved surface area calculated
        """
        square_area = SurfaceArea.calculate_area_square(self.length)
        return 4 * square_area

    def calculate_curved_area_cuboid(self):
        """
        Function to calculate the curved surface area of a cuboid
        :return: total curved surface area calculated
        """
        return 2 * (self.height * (self.length + self.width))

    def calculate_curved_area_cylinder(self):
        """
        Function to calculate the curved surface area of a cylinder
        :return: total curved surface area calculated
        """
        return 2 * math.pi * self.radius * self.height

    def calculate_curved_area_cone(self):
        """
        Function to calculate the curved surface area of a cone
        :return: total curved surface area calculated
        """
        slant_height = math.sqrt(self.radius ** 2 + self.height ** 2)
        return math.pi * self.radius * slant_height

    def calculate_curved_area_sphere(self):
        """
        Function to calculate the curved surface area of a sphere
        :return: total curved surface area calculated
        """
        return 4 * math.pi * self.radius ** 2

    def calculate_curved_area_hemisphere(self):
        """
        Function to calculate the curved surface area of a hemisphere
        :return: total curved surface area calculated
        """
        return 2 * math.pi * self.radius ** 2

    

class SurfaceArea:
    """
    Calculate the total surface area of shapes
    Definitions:
    - Shapes:
      - calculate_area_square
      - calculate_area_rectangle
      - calculate_area_circle
      - calculate_area_triangle
    - 3D Shapes:
      - calculate_area_cube
      - calculate_area_cuboid
      - calculate_area_cylinder
      - calculate_area_cone
      - calculate_area_sphere
      - calculate_area_hemisphere
    """

    def __init__(self, length=0, width=0, height=0, radius=0):
        self.length = length
        self.width = width
        self.height = height
        self.radius = radius

    @staticmethod
    def calculate_area_square(length):
        """
        Function to calculate the area of a square given a length
        :param length: int
        :return: total area calculated
        """
        return length ** 2

    @staticmethod
    def calculate_area_rectangle(width, height):
        """
        Function to calculate the area of a rectangle
        :param width: int width of the rectangle
        :param height: int height of the rectangle
        :return: total area calculated
        """
        return width * height

    @staticmethod
    def calculate_area_circle(radius):
        """
        Function to calculate the area of a circle
        :param radius: radius of circle
        :return: total area calculated
        """
        return math.pi * (radius ** 2)

    @staticmethod
    def calculate_area_triangle(base, height):
        """
        Function to calculate the area of a triangle
        :param base: base width of triangle
        :param height: height of triangle
        :return: total area calculated
        """
        return 0.5 * base * height

    @staticmethod
    def calculate_area_cube(length):
        """
        Function to calculate the surface area of a cube
        :param length: length of cube
        :return: total surface area calculated
        """
        return 6 * SurfaceArea.calculate_area_square(length)

    def calculate_area_cuboid(self):
        """
        Function to calculate the surface area of a cuboid
        :return: total surface area calculated
        """
        return 2 * ((self.length * self.width) +
                    (self.width * self.height) +
                    (self.height * self.length))

    def calculate_area_cylinder(self):
        """
        Function to calculate the surface area of a cylinder
        :return: total surface area calculated
        """
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius ** 2))

    def calculate_area_cone(self):
        """
        Function to calculate the surface area of a cone
        :return: total surface area calculated
        """
        slant_height = math.sqrt(self.radius ** 2 + self.height ** 2)
        return math.pi * self.radius * (self.radius + slant_height)

    @staticmethod
    def calculate_area_sphere(radius):
        """
        Function to calculate the surface area of a sphere
        :param radius: radius of sphere
        :return: total surface area calculated
        """
        return 4 * math.pi * (radius ** 2)

    @staticmethod
    def calculate_area_hemisphere(radius):
        """
        Function to calculate the surface area of a hemisphere
        :param radius: radius of hemisphere
        :return: total surface area calculated
        """
        return 3 * math.pi * (radius ** 2)


