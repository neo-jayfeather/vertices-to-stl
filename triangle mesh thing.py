import numpy as np
import trimesh

# Initialize vertices as a list of empty sublists
num_vertices = 1200
num_coordinates = 9
vertices = [[0.0] * num_coordinates for _ in range(num_vertices)]

# Assign values to vertices[x][y] (assuming your data is correctly read from the file)
with open('triangle_points1.txt', 'r') as file:
    lines = file.readlines()
    for x in range(num_vertices):
        for y in range(num_coordinates):
            vertices[x][y] = float(lines[x].split(' ')[y])
# Create a list of triangle indices
triangles = []
for i in range(num_vertices):
    triangles.append([3 * i, 3 * i + 1, 3 * i + 2])

# Convert vertices to a NumPy array
vertices_array = np.array(vertices).reshape(-1, 3)
print(vertices[0])

# Create a Trimesh object
mesh = trimesh.Trimesh(vertices=vertices_array, faces=triangles)

# Save the mesh as an STL file
mesh.export('output.stl', file_type='stl')
print("done")
