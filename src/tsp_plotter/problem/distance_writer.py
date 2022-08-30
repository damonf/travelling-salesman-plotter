def write_distances(graph, graph_file):
    # Write the graph to file.
    with open(graph_file, "w") as file:
        for row in graph:
            line = ""

            for distance in row:
                line += f"{distance} "

            line.rstrip()
            line += "\n"
            file.write(line)
