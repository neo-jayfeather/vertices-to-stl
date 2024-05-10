import numpy as np
import trimesh

# Create a 1x1x1 cube mesh
extents = [1.0, 1.0, 1.0]
cube_mesh = trimesh.creation.box(extents)

# Generate 6 random colors (RGB triplets)
num_colors = 6
random_colors = np.random.randint(0, 256, size=(num_colors, 4))

# Assign random colors to each face
for i, facet in enumerate(cube_mesh.facets):
<<<<<<< Updated upstream
=======
    print(random_colors)
>>>>>>> Stashed changes
    cube_mesh.visual.face_colors[facet] = random_colors[i]

# Export the cube mesh to a GLB file (binary GLTF)
output_path = "colored_cube.glb"
cube_mesh.export(output_path, file_type="glb")

print(f"Colored cube exported to {output_path}")
