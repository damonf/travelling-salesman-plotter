def read_solution(solution_file):
    # The solution file contains indices into the problem array, describing a path
    # that is the solution.
    # Read the solution file, a list of positive integers, one per line
    # and return them as a list.
    solution = []

    with open(solution_file, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            try:
                solution.append(int(line))
            except ValueError as error:
                raise ValueError(f"invalid solution file, line: {line}.  {error}")

    return solution
