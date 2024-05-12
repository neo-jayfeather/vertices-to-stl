import numpy as np # needed libraries
import trimesh
import os

path = 'sRGB_in_abL.txt'
pathName = os.path.splitext(path)[0] #gets filename
num_vertices, num_coordinates = 1200,9
custom = True # flag, enable to have custom vertices and coordinates
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
    for x in range(num_vertices):
        for y in range(num_coordinates):
            vertices[x][y] = float(lines[x].rstrip().replace('\t',' ').split(' ')[y]) # no pain
    vertices = np.array(vertices).reshape(-1,3)
    for x in range(len(vertices)):
        a, b, c = 0, 2, 1
        vertices[x] = [vertices[x][a],vertices[x][b],vertices[x][c]]
nCount = 0
for i in range(num_vertices):
    triangles.append([3 * i + 0, 3 * i + 1, 3 * i + 2]) # triangle array defenition
    if(i%200 >= 100 and (i <= 200 or (i > 400 and i <= 600) or (i > 800 and i<= 1000))):
        triangles[i] = [triangles[i][2], triangles[i][1], triangles[i][0]]
    if(i%200 < 100 and ((i >= 200 and i < 400) or (i > 600 and i <= 800) or (i >= 1000 and i <= 1200))):
        triangles[i] = [triangles[i][2], triangles[i][1], triangles[i][0]] #handles bottom
# triangle one uses vertiies 0,1,2 etc.
#complicated triangle flipping lol


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
        allColors[x][3] = 255 #assign alpha
        mesh.visual.face_colors[x] = allColors[x]
        nCount += 1

output_filename = f"{pathName}_output.glb"
available_filename = get_avail_filename(output_filename)
mesh.export(available_filename, file_type='glb') # mesh created
print("done") #confirmation
