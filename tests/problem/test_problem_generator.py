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


def test_problem_generator_creates_graph():
    points = [(0.0, 0.0), (0.0, 3.0), (4.0, 0.0)]

    graph = problem_generator.create_graph(points)

    assert len(graph) == 3
    assert graph[0] == [0.0, 3.0, 4.0]
    assert graph[1] == [3.0, 0.0, 5.0]
    assert graph[2] == [4.0, 5.0, 0.0]
