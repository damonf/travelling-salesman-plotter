from tsp_plotter.solution import path_plotter


def test_path_plotter_plots_path(mocker):
    mock_plot = mocker.patch("matplotlib.pyplot.plot")
    mock_scatter = mocker.patch("matplotlib.pyplot.scatter")
    mock_savefig = mocker.patch("matplotlib.pyplot.savefig")

    path = [(0, 10), (10, 5), (0, 10)]
    plot_file = "some_file"
    path_plotter.plot_path(path, plot_file)

    args, _ = mock_plot.call_args
    assert args == ([0, 10, 0], [10, 5, 10])

    args, _ = mock_scatter.call_args
    assert args == ([0, 10, 0], [10, 5, 10])

    args, _ = mock_savefig.call_args
    assert args == ("some_file",)
