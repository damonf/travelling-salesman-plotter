def read_problem(problem_file):
    # The problem file contains a series of points representing cities to be visited.
    # Read the problem file, a list of points (comma separated pairs of numbers), one per line
    # and return them as a list of tuples.
    problem = []

    with open(problem_file, "r") as file:
        for line in file:
            line = line.strip()

            parts = line.split(",")

            if len(parts) != 2:
                raise ValueError(f"invalid problem file, line: {line}")

            try:
                problem.append((float(parts[0]), float(parts[1])))
            except ValueError as error:
                raise ValueError(f"invalid problem file, line: {line}.  {error}")

    return problem
