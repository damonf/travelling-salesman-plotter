from tsp_plotter.problem import points_plotter


def test_points_plotter_plots_path(mocker):
    mock_scatter = mocker.patch("matplotlib.pyplot.scatter")
    mock_savefig = mocker.patch("matplotlib.pyplot.savefig")

    points = [(0, 10), (10, 5), (0, 10)]
    plot_file = "some_file"
    points_plotter.plot_points(points, plot_file)

    args, _ = mock_scatter.call_args
    assert args == ([0, 10, 0], [10, 5, 10])

    args, _ = mock_savefig.call_args
    assert args == ("some_file",)
