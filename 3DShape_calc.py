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
    definitions: 
    calculate_volume_cube
    calculate_volume_cuboid
    calculate_volume_cylinder
    calculate_volume_cone
    calculate_volume_sphere
    calculate_volume_hemisphere
    """

    def __init__(self, length, width, height, radius):
        self.length = length
        self.width = width
        self.height = height
        self.radius = radius

    def calculate_volume_cube(length):
        """
         Function to calculate the volume of a cube
         :param length: length of cube
         :return: total volume calculated
        """
        return length ** 3

    def calculate_volume_cuboid(length, width, height):
        """
        Function to calculate the volume of a cube
        :param length: length of cuboid
        :param width: width of cuboid
        :param height: height of cuboid
        :return: total volume calculated
        """

        return length * width * height

    def calculate_volume_cylinder(radius, height):
        """
        Function to calculate the volume of a cylinder
        :param radius: radius of cylinder
        :param height: height of cylinder
        :return: total volume calculated
        """

        return math.pi * (radius**2) * height

    def calculate_volume_cone(radius, height):
        """
        Function to calculate the volume of a cube
        :param radius: radius of cone
        :param height: height ofcone
        :return: total volume calculated
        """

        return (1/3) * math.pi * (radius**2) * height

    def calculate_volume_sphere(radius):
        """
        Function to calculate the volume of a sphere
        :param radius: radius of sphere
        :return: total volume calculated
        """

        return (4/3) * math.pi * radius**3

    def calculate_volume_hemisphere(radius):
        """
        Function to calculate the volume of a hemisphere
        :param radius: radius of hemisphere
        :return: total volume calculated
        """

        return (2/3) * math.pi * radius**3



class CurvedSurfaceArea:
    """
    Calculate the curved surface area for 3D shapes
    definitions: 
    calculate_curved_area_cube
    calculate_curved_area_cuboid
    calculate_curved_area_cylinder
    calculate_curved_area_cone
    calculate_curved_area_sphere
    calculate_curved_area_hemisphere
    """

    def __init__(self, length, width, height, radius):
        self.length = length
        self.width = width
        self.height = height
        self.radius = radius

    def calculate_curved_area_cube(length):
        """
        Function to calculate the volume of a cube
        :param length: length of cube
        :return: total volume calculated
        """

        sqaure_area = SurfaceArea.calculate_area_square(length)
        return 4 * sqaure_area

    def calculate_curved_area_cuboid(length, width, height):
        """
        Function to calculate the curved surface area of a cube
        :param length: length of cuboid
        :param width: width of cuboid
        :param height: height of cuboid
        :return: total volume calculated
        """

        return ((2 * height) * (length + width))

    def calculate_curved_areae_cylinder(radius, height):
        """
        Function to calculate the curved surface area of a cylinder
        :param radius: radius of cylinder
        :param height: height of cylinder
        :return: total volume calculated
        """

        return (2 * math.pi) * radius * height

    def calculate_curved_area_cone(radius, length):
        """
        Function to calculate the curved surface area of a cube
        :param radius: radius of cone
        :param height: length ofcone
        :return: total volume calculated
        """

        return math.pi * radius * length

    def calculate_curved_area_sphere(radius):
        """
        Function to calculate the curved surface area of a sphere
        :param radius: radius of sphere
        :return: total volume calculated
        """

        return 4 * math.pi * (radius**2)

    def calculate_curved_area_hemisphere(radius):
        """
        Function to calculate the curved surface area of a hemisphere
        :param radius: radius of hemisphere
        :return: total volume calculated
        """

        return 2 * math.pi * (radius**2)
    
   
class SurfaceArea:
    """
    Calculate the total surface area of shapes
    definitions: 
    Shapes: 
    calculate_area_sqaure
    calculate_area_rectangle
    calculate_area_circle
    calculate_area_triagle
    3D Shapes:
    calculate_area_cube
    calculate_area_cuboid
    calculate_area_cylinder
    calculate_area_cone
    calculate_area_sphere
    calculate_area_hemisphere
    """

    def __init__(self, length, width, height, radius):
        self.length = length
        self.width = width
        self.height = height
        self.radius = radius

    def calculate_area_square(length):
        """
        Function to calculate area of a square given a length
        :param length: int
        :return: total area calculated
        """
        return length ** 2

    def calculate_area_rectangle(width, height):
        """
        Function to calculate the area of a rectangle
        :param width: int width of the rectangle
        :param height: int height of the rectangle
        :return: total area calculated
        """

        return width * height

    def calculate_area_circle(radius):
        """
        Function to calculate the area of a circle
        :param radius: radius of circle
        :return: total area calculated
        """

        return math.pi * (radius ** 2)

    def calculate_area_triangle(width, height):
        """
        Function to calculate the area of a triangle
        :param width: width of triangle
        :param height: height of triangle
        :return: total area calculated
        """
        square_area = SurfaceArea.calculate_area_rectangle(width, height)
        return square_area / 2

    def calculate_area_cube(length):
        """
        Function to calculate the area of a cube
        :param : length of cude
        :return: total area calculated
        """
        sqaure_area = SurfaceArea.calculate_area_square(length)
        return 6 * sqaure_area

    def calculate_area_cuboid(length, width, height):
        """
        Function to calculate the area of a cuboid
        :param length: length of cuboid
        :param width: width of cuboid
        :param height: height of cuboid
        :return: total area calculated
        """
        return 2 * ((length * width) +
                    (width * height) +
                    (height * length))

    def calculate_area_cylinder(height, radius):
        """
        Function to calculate the area of a cylinder
        :param radius: radius of cylinder
        :param height: height of cylinder
        :return: total area cylinder
        """
        return ((2 * math.pi * radius * height) +
                      (2 * math.pi * (radius**2)))

    def calculate_area_cone(length, radius):
        """
        Function to calculate the area of a cone
        :param width: width of cone
        :param height: height of cone
        :return: total area calculated
        """
        return math.pi * radius * (radius + length)

    def calculate_area_sphere(radius):
        """
        Function to calculate the area of a sphere
        :param radius: radius of sphere
        :return: total area calculated
        """
        return 4 * math.pi * (radius**2)

    def calculate_area_hemisphere(radius):
        """
        Function to calculate the area of a hemisphere
        :param radius: radius of hemisphere
        :return: total area calculated
        """
        return 3 * math.pi * radius**2

