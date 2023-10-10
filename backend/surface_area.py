import math

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