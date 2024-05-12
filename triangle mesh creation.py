import numpy as np # needed libraries
import trimesh
import os

path = 'sRGB_in_abL.txt'
pathName = os.path.splitext(path)[0] #gets filename
num_vertices, num_coordinates = 0,0
custom = False # flag, enable to have custom vertices and coordinates
triangles = []

def get_avail_filename(base):
    filename, ext = os.path.splitext(base)
    count = 1
    while os.path.exists(base):
        base = f"{filename}({count}){ext}"
        count += 1
    return base

with open(path, 'r') as file: # open text file
    lines = file.readlines()
    if(not custom):
        num_vertices = len(lines)
        num_coordinates = len(lines[0].rstrip().replace('\t',' ').split(' ')) #i hope this works, will test at home or something
    vertices = [[0.0] * num_coordinates for _ in range(num_vertices)] # define list
    #lines = np.array(lines).reshape(1,-1)
    '''for x in range(num_vertices):
        for y in range(num_coordinates):
            vertices[x][y] = float(lines[x].rstrip().replace('\t',' ').split(' ')[y]) # no pain
        temp = vertices[x]
        #vertices[x] = [temp[1],temp[0],temp[2],temp[4],temp[3],temp[5],temp[7],temp[6],temp[8]]  # Swap (0, 1)
        #vertices[x] = [temp[2],temp[1],temp[0],temp[5],temp[4],temp[3],temp[8],temp[7],temp[6]]
        vertices[x] = [temp[0], temp[2], temp[1], temp[3], temp[5], temp[4], temp[6], temp[8], temp[7]]
        #dumb solution to dumb problem, but it works
    '''
    
    for x in range(num_vertices):
        for y in range(num_coordinates):
            vertices[x][y] = float(lines[x].rstrip().replace('\t',' ').split(' ')[y]) # no pain
    vertices = np.array(vertices).reshape(-1,3)
    for x in range(len(vertices)):
        a, b, c = 0, 2, 1
        vertices[x] = [vertices[x][a],vertices[x][b],vertices[x][c]]
for i in range(num_vertices):
    triangles.append([3 * i + 0, 3 * i + 1, 3 * i + 2]) # triangle array defenition
    # triangle one uses vertiies 0,1,2 etc.

#vertices_array = np.array(vertices).reshape(-1, 3) # helpful
mesh = trimesh.Trimesh(vertices=vertices, faces=triangles) #mesh creation
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

output_filename = f"{pathName}_output.glb"
available_filename = get_avail_filename(output_filename)
mesh.export(available_filename, file_type='glb') # mesh created
print("done") #confirmation
