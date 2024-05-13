import numpy as np  # Importing numpy for numerical operations
import trimesh  # Importing trimesh for creating and manipulating 3D meshes
import os  # Importing os for interacting with the operating system

# Path to the input file
path = 'sRGB_in_abL.txt'
# Extracting the filename from the path
pathName = os.path.splitext(path)[0]

# Number of vertices and coordinates
num_vertices, num_coordinates = 1200,9

# Flag to enable custom vertices and coordinates
custom = True

# List to store the triangles
triangles = []

# Function to generate a unique filename
def get_avail_filename(base):
    # Splitting the base into filename and extension
    filename, ext = os.path.splitext(base)
    count = 1
    # Loop to check if a file with the given name exists
    while os.path.exists(base):
        # If it does, append a count to the filename
        base = f"{filename}({count}){ext}"
        count += 1
    # Return the unique filename
    return base

# Function to calculate the normal of a triangle
def get_normal (vertices):
    
    # Extracting the vertices of the triangle
    vec1 = np.array([vertices[3]-vertices[0],vertices[4]-vertices[1],vertices[5]-vertices[2]]);
    vec2 = np.array([vertices[6]-vertices[0],vertices[7]-vertices[1],vertices[8]-vertices[2]]);
    
    # Calculating the normal of the triangle
    normal = np.cross(vec1, vec2)

    # Normalizing the normal
    normal = normal / np.linalg.norm(normal)

    # Returning the normal   
    return normal

# Function to calculate the direction of a triangle from Lab=(50,0,0)
def get_direction (tri1):    
    # Calculating the direction of the triangle
    #   the Lab has been reordered as aLb, so its coordinates are (0,50,0)
    direction = tri1 - np.array([0,50,0])
    # Normalizing the direction
    direction = direction / np.linalg.norm(direction)
    # Returning the direction
    return direction        

# Function to decide whether two vectors are in the same direction
def same_direction (vec1, vec2):
    # Calculating the dot product of the two vectors
    dot_product = np.dot(vec1, vec2)
    # If the dot product is greater than 0, the vectors are in the same direction
    return dot_product > 0

# Opening the input file
with open(path, 'r') as file:
    # Reading all lines into a list
    lines = file.readlines()
    # If custom flag is not set, determine the number of vertices and coordinates from the file
    if(not custom):
        num_vertices = len(lines)
        num_coordinates = len(lines[0].rstrip().replace('\t',' ').split(' '))
    # Defining a 2D list to store the vertices
    vertices = [[0.0] * num_coordinates for _ in range(num_vertices)]
    # Loop to read the vertices from the lines
    for x in range(num_vertices):
        for y in range(num_coordinates):
            vertices[x][y] = float(lines[x].rstrip().replace('\t',' ').split(' ')[y])
    # Reshaping the vertices into a numpy array
    vertices = np.array(vertices).reshape(-1,3)
    # Reordering the vertices
    for x in range(len(vertices)):
        a, b, c = 0, 2, 1
        vertices[x] = [vertices[x][a],vertices[x][b],vertices[x][c]]

# Counter for the number of triangles
nCount = 0

# Loop to generate the triangles
for i in range(num_vertices):
    # Each triangle is defined by three vertices
    triangles.append([3 * i + 0, 3 * i + 1, 3 * i + 2])

    vertice_x9 = np.array(vertices[3*i:3*i+3]).reshape(-1)
    if ~same_direction(get_normal(vertice_x9),get_direction(vertices[3*i])):
        triangles[i] = [triangles[i][2], triangles[i][1], triangles[i][0]]

    # # Flipping the order of vertices in some triangles based on certain conditions
    # if(i%200 >= 100 and (i <= 200 or (i > 400 and i <= 600) or (i > 800 and i<= 1000))):
    #     triangles[i] = [triangles[i][2], triangles[i][1], triangles[i][0]]
    # if(i%200 < 100 and ((i >= 200 and i < 400) or (i > 600 and i <= 800) or (i >= 1000 and i <= 1200))):
    #     triangles[i] = [triangles[i][2], triangles[i][1], triangles[i][0]]

# Creating a trimesh object with the vertices and triangles
mesh = trimesh.Trimesh(vertices=vertices, faces=triangles)

# Opening the file with the colors
with open('sRGB_in_abL_color.txt' ,'r') as file:
    # Reading all lines into a list
    colors = file.readlines()
    # Determining the number of lines and colors
    num_lines = len(colors)
    num_colors = len(colors[0].rstrip().replace('\t',' ').split(' '))
    # Defining a 2D list to store the colors
    allColors = [[0.0] * (num_colors + 1) for _ in range(num_lines)]
    # Loop to read the colors from the lines
    for x in range(num_lines):
        for y in range(num_colors):
            allColors[x][y] = float(colors[x].rstrip().replace('\t',' ').split(' ')[y])
    # Assigning an alpha value of 255 to each color
    for x in range(num_lines):
        allColors[x][3] = 255
        # Assigning the colors to the faces of the mesh
        mesh.visual.face_colors[x] = allColors[x]
        nCount += 1

# Generating the filename for the output file
output_filename = f"{pathName}_output.glb"
# Ensuring the filename is unique
available_filename = get_avail_filename(output_filename)
# Exporting the mesh to a .glb file
mesh.export(available_filename, file_type='glb')

# Printing a confirmation message
print("done")