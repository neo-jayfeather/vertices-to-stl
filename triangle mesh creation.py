import numpy as np # needed libraries
import trimesh
<<<<<<< Updated upstream
path = 'canon_in_abL.txt'
=======
path = 'sRGB_in_abL.txt'
>>>>>>> Stashed changes
pathName = path.split('\\')[len(path.split('\\'))-1] # complex way to get file name after last \
pathName = path.split('.')[len(path.split('.'))-2] # complex way to remove .txt or ending
num_vertices = 0 
num_coordinates = 0
triangles = []

<<<<<<< Updated upstream
with open('triangle_points1.txt', 'r') as file: # open text file
=======
with open(path, 'r') as file: # open text file
>>>>>>> Stashed changes
    lines = file.readlines()
    num_vertices = len(lines)
    num_coordinates = len(lines[0].rstrip().replace('\t',' ').split(' ')) #i hope this works, will test at home or something
    vertices = [[0.0] * num_coordinates for _ in range(num_vertices)] # define list
    for x in range(num_vertices):
        for y in range(num_coordinates):
            vertices[x][y] = float(lines[x].rstrip().replace('\t',' ').split(' ')[y]) # no pain
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
for i in range(num_vertices):
    triangles.append([3 * i, 3 * i + 1, 3 * i + 2]) # triangle array defenition
    # triangle one uses verticies 0,1,2 etc.

vertices_array = np.array(vertices).reshape(-1, 3) # helpful
mesh = trimesh.Trimesh(vertices=vertices_array, faces=triangles) #mesh creation
<<<<<<< Updated upstream
mesh.export(f'{pathName} output.stl', file_type='stl') # mesh created
=======
with open('sRGB_in_abL_color.txt' ,'r') as file:
    colors = file.readlines()
    num_lines = len(colors)
    num_colors = len(colors[0].rstrip().replace('\t',' ').split(' ')) #i hope this works, will test at home or something
    allColors = [[0.0] * (num_colors + 1) for _ in range(num_lines)] # define list
    for x in range(num_lines):
        for y in range(num_colors):
            allColors[x][y] = float(colors[x].rstrip().replace('\t',' ').split(' ')[y]) # no pain

    for x in range(num_lines):
        allColors[x][3] = 255
        #print(allColors[x])
        mesh.visual.face_colors[x] = allColors[x]
    
mesh.export(f'{pathName} output.glb', file_type='glb') # mesh created
>>>>>>> Stashed changes
print("done") #confirmation
