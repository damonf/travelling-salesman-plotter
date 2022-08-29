def write_distances(adjacency_matrix, adjacency_matrix_file):
    # Write the adjacency matrix to file.
    with open(adjacency_matrix_file, "w") as file:
        for row in adjacency_matrix:
            line = ""

            for distance in row:
                line += f"{distance} "

            line.rstrip()
            line += "\n"
            file.write(line)
