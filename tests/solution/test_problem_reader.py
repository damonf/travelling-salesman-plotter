from unittest.mock import mock_open

import pytest

from tsp_plotter.solution import problem_reader


def test_problem_reader_reads_problem(mocker):
    m = mock_open(read_data="17.7, 2.7\n88.5, 87.6\n9.5, 98.2\n")
    mocker.patch("builtins.open", m)
    problem = problem_reader.read_problem("some_file")

    m.assert_called_once_with("some_file", "r")
    assert problem == [(17.7, 2.7), (88.5, 87.6), (9.5, 98.2)]


def test_problem_reader_throws_when_invalid_line(mocker):
    mocker.patch("builtins.open", mock_open(read_data="17.7, 2.7\naaa\n9.5, 98.2\n"))
    with pytest.raises(ValueError, match="invalid problem file"):
        problem_reader.read_problem("some_file")


def test_problem_reader_throws_when_invalid_number(mocker):
    mocker.patch("builtins.open", mock_open(read_data="17.7, 2.7\na, b\n9.5, 98.2\n"))
    with pytest.raises(ValueError, match="invalid problem file"):
        problem_reader.read_problem("some_file")
