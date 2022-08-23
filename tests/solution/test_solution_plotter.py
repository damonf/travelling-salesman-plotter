from tsp_plotter.solution import solution_plotter

import pytest


def test_solution_plotter_creates_path():
    indices = [0, 1, 2, 0]
    vertices = [(0, 10), (10, 10), (20, 0)]
    path = solution_plotter.create_path(indices, vertices)

    assert path == [(0, 10), (10, 10), (20, 0), (0, 10)]


def test_solution_plotter_throws_when_index_out_of_range():
    indices = [0, 1, 9]
    vertices = [(0, 10), (10, 10), (20, 0)]

    with pytest.raises(IndexError, match="9"):
        solution_plotter.create_path(indices, vertices)
