# A majority of this code was written by Google Gemini was researching solutions

# git clone https://github.com/Nehri/slicing_algorithm.git

# --- Python Packages Needed ---
# pip install pymeshlab # this is a library that deals with processing 3d meshes efficiently
# pip install numpy # this is a library that deals with computation
# pip install torch # this is the library that deals with the machine learning computation
# pip install numpy-stl # this library adds stl functionality to numPy
# pip install stlconverter # this is used to convert between ASCII and Binary STL files
# pip install colorama # this allows color ASCII text in console and is a dependency for the slicing-algorithm project

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
