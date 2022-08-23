from matplotlib import pyplot


def plot_points(points, plot_file):
    # Plot the points and save to a file.
    xcoords = []
    ycoords = []

    for point in points:
        xcoords.append(point[0])
        ycoords.append(point[1])

    pyplot.scatter(xcoords, ycoords)
    pyplot.savefig(plot_file)
