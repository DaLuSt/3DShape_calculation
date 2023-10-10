import tkinter as tk
from tkinter import messagebox
import math

class ShapeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Shape Calculator")
        self.root.geometry("400x300")  # Set the size of the main window

        self.label = tk.Label(root, text="Select a 3D shape:")
        self.label.pack()

        self.shape_var = tk.StringVar()
        self.shape_var.set("Cube")

        self.shape_menu = tk.OptionMenu(root, self.shape_var, "Cube", "Cuboid", "Cylinder", "Cone", "Sphere", "Hemisphere")
        self.shape_menu.pack()

        self.calculate_button = tk.Button(root, text="Calculate", command=self.open_input_window)
        self.calculate_button.pack()

    def open_input_window(self):
        shape = self.shape_var.get()
        inputs = self.get_inputs(shape)
        if inputs is not None:
            input_window = tk.Toplevel(self.root)
            input_window.title(f"Enter Dimensions for {shape}")
            input_window.geometry("300x200")  # Set the size of the input window

            self.create_input_fields(input_window, shape, inputs)

            calculate_button = tk.Button(input_window, text="Calculate", command=lambda: self.calculate(shape, inputs))
            calculate_button.pack()

    def create_input_fields(self, window, shape, inputs):
        input_frame = tk.Frame(window)
        input_frame.pack()

        for i, label in enumerate(shape_labels[shape]):
            lbl = tk.Label(input_frame, text=label)
            lbl.grid(row=i, column=0, sticky="w")
            entry = tk.Entry(input_frame)
            entry.insert(0, str(inputs[i]))
            entry.grid(row=i, column=1)

    def calculate(self, shape, inputs):
        if shape == "Cube":
            self.calculate_cube(*inputs)
        elif shape == "Cuboid":
            self.calculate_cuboid(*inputs)
        elif shape == "Cylinder":
            self.calculate_cylinder(*inputs)
        elif shape == "Cone":
            self.calculate_cone(*inputs)
        elif shape == "Sphere":
            self.calculate_sphere(*inputs)
        elif shape == "Hemisphere":
            self.calculate_hemisphere(*inputs)

    def show_result(self, title, result):
        messagebox.showinfo(title, result)

    def get_inputs(self, shape):
        input_frame = self.root.winfo_children()[1].winfo_children()[1]
        inputs = []
        for entry_widget in input_frame.winfo_children():
            if isinstance(entry_widget, tk.Entry):
                input_value = entry_widget.get()
                try:
                    input_value = float(input_value)
                    inputs.append(input_value)
                except ValueError:
                    messagebox.showerror("Input Error", "Please enter valid numbers for all dimensions.")
                    return None
        return tuple(inputs)


    def calculate_cube(self, length):
        volume = length ** 3
        self.show_result("Cube Volume", f"Volume of Cube: {volume}")

    def calculate_cuboid(self, length, width, height):
        volume = length * width * height
        self.show_result("Cuboid Volume", f"Volume of Cuboid: {volume}")

    def calculate_cylinder(self, radius, height):
        volume = math.pi * (radius ** 2) * height
        self.show_result("Cylinder Volume", f"Volume of Cylinder: {volume}")

    def calculate_cone(self, radius, height):
        volume = (1/3) * math.pi * (radius ** 2) * height
        self.show_result("Cone Volume", f"Volume of Cone: {volume}")

    def calculate_sphere(self, radius):
        volume = (4/3) * math.pi * (radius ** 3)
        self.show_result("Sphere Volume", f"Volume of Sphere: {volume}")

    def calculate_hemisphere(self, radius):
        volume = (2/3) * math.pi * (radius ** 3)
        self.show_result("Hemisphere Volume", f"Volume of Hemisphere: {volume}")

shape_labels = {
    "Cube": ["Length"],
    "Cuboid": ["Length", "Width", "Height"],
    "Cylinder": ["Radius", "Height"],
    "Cone": ["Radius", "Height"],
    "Sphere": ["Radius"],
    "Hemisphere": ["Radius"],
}

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeCalculatorApp(root)
    root.mainloop()
