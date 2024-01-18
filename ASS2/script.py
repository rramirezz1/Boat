def duplicate_quads(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith('f'):
                vertices = line.split()[1:]
                if len(vertices) == 4:  # Check if it's a quad
                    vertex1, vertex2, vertex3, vertex4 = vertices
                    face1 = f'f {vertex1} {vertex2} {vertex3}\n'
                    face2 = f'f {vertex1} {vertex3} {vertex4}\n'
                    outfile.write(face1)
                    outfile.write(face2)
                else:
                    outfile.write(line)
            else:
                outfile.write(line)

if __name__ == "__main__":
    input_file = "Boat.obj"
    output_file = "Boat2.obj"
    duplicate_quads(input_file, output_file)