# 3D Shape Calculations
* * *
A module with functions for the calculation of volume, Curved surface are and Total surface area of 3D shapes


## Description
* * *
Volume: Calculate the volume for 3D shapes
    calculate_volume_cube
    calculate_volume_cuboid
    calculate_volume_cylinder
    calculate_volume_cone
    calculate_volume_sphere
    calculate_volume_hemisphere
CurvedSurfaceArea: Calculate the curved surface area for 3D shapes
    calculate_curved_area_cube
    calculate_curved_area_cuboid
    calculate_curved_area_cylinder
    calculate_curved_area_cone
    calculate_curved_area_sphere
    calculate_curved_area_hemisphere
SurfaceArea: Calculate the total surface area of shapes and 3D shapes
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

## Installation
* * *

### Single install
The easiest way to install all the required packages is via conda. How to install conda on your system can be found [here](https://docs.anaconda.com/anaconda/install/index.html).

To create a new environment which contains all the required packages plus the right version run the following code:

```bash
  conda env create -f environment.yml
```

This will create a new environment named `mosquito_env` which can be used to run this repository.

> NOTE: the environment.yml is located in the install/ directory [here](install/environment.yml).

### Multiple installs
An other option is to install each package seperately, either with conda or pip.

conda:
```bash
  conda install <PACKAGE>=<VERSION>
```

pip
```bash
  pip install <PACKAGE>==<VERSION>
```

> NOTE: make sure to use the correct versions, which are listed [here](#packages).

## Getting started
* * *
How to run the code?


## Requirements
* * *
| Software                          | Version  |
| --------------------------------- | :------: |
| [Python](https://www.python.org/) | `3.9.7`  |    


## Packages
* * *
| Package                                                        | Version  |
| ---------------------------------------------------------------| :------: |
| [math](https://docs.python.org/3/library/math.html)            | `3.10.2` |


## License
* * * 
This project contains a MIT [license](./LICENSE.md)


## References
* * *

Formulas for calculations: https://www.omnicalculator.com/math/area#sector-area-formula
