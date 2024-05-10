import trimesh
import numpy as np

# Create vertices for a cube
vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])

# Define faces (indices of vertices)
faces = np.array([
    [0, 1, 2],
    [0, 2, 3],
    [4, 5, 6],
    [4, 6, 7],
    [0, 1, 5],  # Top face
    [1, 2, 6],  # Top face
    [2, 3, 7],  # Top face
    [3, 0, 4]   # Top face
])

# Create a mesh
mesh = trimesh.Trimesh(vertices=vertices, faces=faces)

# Create a color array (RGB values)
face_colors = np.array([
    [255, 0, 0],   # Red
    [0, 255, 0],   # Green
    [0, 0, 255],   # Blue
    [255, 255, 0], # Yellow
    [255, 0, 255], # Magenta (top face)
    [0, 255, 255], # Cyan (top face)
    [255, 255, 255], # White (top face)
    [128, 128, 128]  # Gray (top face)
])

# Assign colors to faces
mesh.visual.face_colors = face_colors

# Visualize the colored mesh
mesh.show()

mesh.export('my_cube.3mf',file_type = '3mf')
