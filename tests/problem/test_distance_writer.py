from unittest.mock import mock_open

from tsp_plotter.problem import distance_writer


def test_distance_writer_writes_distances(mocker):
    m = mock_open()
    mocker.patch("builtins.open", m)

    adjacency_matrix = [[0.0, 1.1, 5.0], [1.1, 0.0, 1.3], [5.0, 1.3, 0.0]]
    distance_file = "some_file"
    distance_writer.write_distances(adjacency_matrix, distance_file)

    m.assert_called_once_with("some_file", "w")
    handle = m()

    wc = handle.write.mock_calls
    wc[0].assert_called_with("0.0 1.1 5.0")
    wc[1].assert_called_with("1.1 0.0 1.3")
    wc[2].assert_called_with("5.0 1.3 0.0")
