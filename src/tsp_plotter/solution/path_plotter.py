from matplotlib import pyplot


def plot_path(vertices, plot_file):
    # Plot the vertices, and save to file.
    xcoords = []
    ycoords = []

    for point in vertices:
        xcoords.append(point[0])
        ycoords.append(point[1])

    pyplot.plot(xcoords, ycoords)
    pyplot.scatter(xcoords, ycoords)

    pyplot.savefig(plot_file)
