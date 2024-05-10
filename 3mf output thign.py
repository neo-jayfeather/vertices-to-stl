import numpy as np
import trimesh

# Create a simple mesh (you can replace this with your own mesh)
vertices = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
faces = np.array([[0, 1, 2]])
mesh = trimesh.Trimesh(vertices=vertices, faces=faces)

# Generate random RGB colors for each face
num_faces = len(mesh.faces)
random_colors = np.random.rand(num_faces, 3)  # Random values between 0 and 1

# Create a ColorVisuals object
color_visuals = trimesh.visual.color.ColorVisuals(mesh=mesh, face_colors=random_colors)

# Access the face colors
print(color_visuals.face_colors)

# Set the ColorVisuals object as the mesh's visual properties
mesh.visual = color_visuals

# Save the mesh as an STL file
mesh.export('output.3mf', file_type='3mf')
