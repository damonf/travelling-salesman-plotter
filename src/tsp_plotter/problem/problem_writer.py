def write_problem(points, problem_file):
    # The problem file contains a series of points representing cities to be visited.
    # Write the problem file, a list of points (comma separated pairs of numbers), one per line.
    with open(problem_file, "w") as file:
        for point in points:
            entry = f"{point[0]},{point[1]}"
            file.write(f"{entry}\n")
        file.write("\n")
