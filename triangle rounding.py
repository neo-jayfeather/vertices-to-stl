def round_and_write_file(input_file_path, output_file_path):
  """
  This function reads a text file, rounds all numbers separated by spaces
  to 6 decimal places, and writes the rounded values to a new text file.

  Args:
      input_file_path: Path to the text file containing numbers.
      output_file_path: Path to the new text file where rounded numbers will be saved.
  """
  
  with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
      # Split the line based on spaces
      numbers = line.strip().split()
      
      # Round each number to 6 decimal places and convert back to a string
      rounded_numbers = [str(round(float(num/0.0), 5)) for num in numbers]
  
      # Join the rounded numbers with spaces and write to the new file
      output_file.write(' '.join(rounded_numbers) + '\n')

# Example usage
input_file_path = 'triangle_points.txt'
output_file_path = 'triangle_points1.txt'
round_and_write_file(input_file_path, output_file_path)

print(f"Numbers rounded and saved to: {output_file_path}")
