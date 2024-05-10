import trimesh
import numpy as np

# Create a mesh
mesh = trimesh.creation.icosphere()

# Set the face colors
face_colors = np.random.rand(mesh.faces.shape[0], 3) * 255

# Save the mesh as a 3MF file
mesh.export("mesh.3mf", face_colors=face_colors)
