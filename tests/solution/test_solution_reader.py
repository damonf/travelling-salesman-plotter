from unittest.mock import mock_open

import pytest

from tsp_plotter.solution import solution_reader


def test_solution_reader_reads_solution(mocker):
    m = mock_open(read_data="10\n20\n30\n")
    mocker.patch("builtins.open", m)
    solution = solution_reader.read_solution("some_file")

    m.assert_called_once_with("some_file", "r")
    assert solution == [10, 20, 30]


def test_solution_reader_throws_when_invalid(mocker):
    mocker.patch("builtins.open", mock_open(read_data="10\nabc\n30\n"))
    with pytest.raises(ValueError, match="invalid solution file"):
        solution_reader.read_solution("some_file")
