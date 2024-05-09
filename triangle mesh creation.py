import numpy as np # needed libraries
import trimesh
num_vertices = 0 # text file size (will probably automate later)
num_coordinates = 0
triangles = []



with open('triangle_points1.txt', 'r') as file: # open text file
    lines = file.readlines()
    num_vertices = len(lines)
    num_coordinates = len(lines[0].rstrip().replace('\t',' ').split(' ')) #i hope this works, will test at home or something
    vertices = [[0.0] * num_coordinates for _ in range(num_vertices)] # define list
    for x in range(num_vertices):
        for y in range(num_coordinates):
            #vertices[x][y] = float(lines[x].split(' ')[y]) #pain
            vertices[x][y] = float(lines[x].rstrip().replace('\t',' ').split(' ')[y]) # no pain

for i in range(num_vertices):
    triangles.append([3 * i, 3 * i + 1, 3 * i + 2]) # triangle array defenition
    # triangle one uses verticies 0,1,2 etc.

vertices_array = np.array(vertices).reshape(-1, 3) # helpful
mesh = trimesh.Trimesh(vertices=vertices_array, faces=triangles) #mesh creation
mesh.export('output.stl', file_type='stl') # mesh created
print("done") #confirmation