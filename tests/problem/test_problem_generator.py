from tsp_plotter.problem import problem_generator


def test_problem_generator_creates_problem():
    num_points = 10
    arc = False
    points = problem_generator.create_problem(num_points, arc)

    assert len(points) == 10


def test_problem_generator_creates_problem_arc():
    num_points = 10
    arc = True
    points = problem_generator.create_problem(num_points, arc)

    assert len(points) == 10


def test_problem_generator_creates_distance_matrix():
    points = [(0.0, 0.0), (0.0, 3.0), (4.0, 0.0)]

    distance_matrix = problem_generator.create_distance_matrix(points)

    assert len(distance_matrix) == 3
    assert distance_matrix[0] == [0.0, 3.0, 4.0]
    assert distance_matrix[1] == [3.0, 0.0, 5.0]
    assert distance_matrix[2] == [4.0, 5.0, 0.0]
