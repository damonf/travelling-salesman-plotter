from . import problem_reader, solution_reader, path_plotter


def plot_solution(solution_file, problem_file, solution_image_file):
    # Plot the solution graphically and save to a .png file.

    solution = solution_reader.read_solution(solution_file)
    problem = problem_reader.read_problem(problem_file)
    solution_path = create_path(solution, problem)
    path_plotter.plot_path(solution_path, solution_image_file)


def create_path(indices, vertices):
    # Given a list of indices
    # and a list of vertices
    # return the list of vertices corresponding to the indices.
    result = []

    v_len = len(vertices)

    for idx in indices:
        if idx > v_len or idx < 0:
            raise IndexError(f"points has no entry for {idx}")
        result.append(vertices[idx])

    return result
