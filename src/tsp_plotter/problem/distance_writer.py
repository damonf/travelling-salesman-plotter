def write_distances(distance_matrix, distance_matrix_file):
    # Write the distance matrix to file.
    with open(distance_matrix_file, "w") as file:
        for row in distance_matrix:
            line = ""

            for distance in row:
                line += f"{distance} "

            line.rstrip()
            line += "\n"
            file.write(line)
