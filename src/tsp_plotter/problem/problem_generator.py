import random
import math

from . import distance_writer, points_plotter, problem_writer


def generate_problem(num_points, arc, problem_file, problem_image_file, graph_file):
    # Generate a problem.
    # Output files:
    # Problem file; a list of points, one per line.
    # Graph file; an adjacency matrix of distances between the points
    # The problem plotted visually
    problem = create_problem(num_points, arc)
    problem_writer.write_problem(problem, problem_file)
    points_plotter.plot_points(problem, problem_image_file)
    dists = create_graph(problem)
    distance_writer.write_distances(dists, graph_file)


def create_problem(num_points, arc):
    # Create the points representing cities to be visited.
    # The points are a list of tuples.
    # If arc is True, the points will be aligned along an arc.
    if num_points < 2:
        raise ValueError("num_points must be > 1")

    points = []

    if arc:
        # plot a semi-circle
        step = 100.0 / (num_points - 1)
        xp = 0.0
        while xp < 100.0 or math.isclose(xp, 100.0):
            yp = 0.04 * (xp - 50.0) ** 2
            points.append((round(xp, 4), round(yp, 4)))
            xp += step
    else:
        # plot random points
        for idx in range(0, num_points):
            xp = round(random.uniform(0, 100), 4)
            yp = round(random.uniform(0, 100), 4)

            points.append((xp, yp))

    return points


def create_graph(points):
    # Creates an adjacency matrix for the distances between the points.
    # The matrix has in position (i, j) the distance between point i and j.
    dists = []

    for p1 in points:

        row = []

        for p2 in points:
            dist = calc_dist(p1, p2)
            row.append(dist)

        dists.append(row)

    return dists


def calc_dist(p1, p2):
    dist = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
    return round(dist, 4)
