# git clone https://github.com/Nehri/slicing_algorithm.git

# pip install pymeshlab
# pip install numpy
# pip install torch
# pip install numpy-stl
# pip install stlconverter
# pip install colorama

import pymeshlab

# --- Code to convert the OBJ file to STL file ---
ms = pymeshlab.MeshSet()

# Load the OBJ file
ms.load_new_mesh('/content/shap-e/mesh_0.obj')

# Save as STL
ms.save_current_mesh('mesh.stl')

# --- Convert Binary STL File to ASCII STL File ---
# python3 -m stlconverter /content/shap-e/mesh.stl stla

# --- Slicing STL Mesh with User Provided Parameters: 0.25 is layer height and 0 is infill percentage ---
# python3 /content/slicing_algorithm/slicing.py /content/shap-e/mesh-converted-ASCII.stl 0.25 0
