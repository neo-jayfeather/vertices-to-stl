import numpy as np
import trimesh

def check_color_data(file_path):
    # Load the 3MF file
    mesh = trimesh.load(file_path)

    # Check if vertex colors are present
    has_vertex_colors = hasattr(mesh.visual, 'vertex_colors')
    if has_vertex_colors:
        print(f"Vertex colors found in {file_path}")
    else:
        print(f"No vertex colors in {file_path}")

    # Check if texture maps are present
    has_texture_maps = hasattr(mesh.visual, 'uv')
    if has_texture_maps:
        print(f"Texture maps found in {file_path}")
    else:
        print(f"No texture maps in {file_path}")

# Paths to your 3MF files (replace with actual file paths)
black_3mf_path = 'black.3mf'
red_3mf_path = 'red.3mf'

# Check color data for both files
check_color_data(black_3mf_path)
check_color_data(red_3mf_path)
