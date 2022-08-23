from unittest.mock import mock_open

from tsp_plotter.problem import problem_writer


def test_problem_writer_writes_problem(mocker):
    m = mock_open()
    mocker.patch("builtins.open", m)

    points = [(0, 10), (10, 5), (0, 10)]
    problem_file = "some_file"
    problem_writer.write_problem(points, problem_file)

    m.assert_called_once_with("some_file", "w")
    handle = m()

    wc = handle.write.mock_calls
    wc[0].assert_called_with("0,10\n")
    wc[1].assert_called_with("10,5\n")
    wc[2].assert_called_with("0,10\n")
    wc[3].assert_called_with("\n")
