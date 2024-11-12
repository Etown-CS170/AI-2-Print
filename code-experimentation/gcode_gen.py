# TODO: Find parameters for bed size, numb of walls/perimeter, bed temp, extruder temp, print speed etc.

import trimesh

# Load the OBJ file
mesh = trimesh.load_mesh("mesh.obj")

# Slice the model (simplified)
layers = []
for z in range(0, int(mesh.bounds[1][2]), 0.2):  # Slice at 0.2mm intervals
    layer = mesh.section(plane_origin=[0, 0, z], plane_normal=[0, 0, 1])
    if layer is not None:
        layers.append(layer)

# Generate G-code (simplified)
gcode = []
gcode.append("G28")  # Home the printer
gcode.append("G90")  # Absolute positioning

for layer in layers:
    for path in layer.paths:
        gcode.append(f"G0 X{path.vertices[0][0]} Y{path.vertices[0][1]}")  # Move to start
        for vertex in path.vertices:
            gcode.append(f"G1 X{vertex[0]} Y{vertex[1]} E1")  # Linear move with extrusion
        gcode.append("G92 E0")  # Reset extruder position

# Save G-code to file
with open("mesh.gcode", "w") as f:
    f.write("\n".join(gcode))