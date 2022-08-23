import argparse
import os
import sys

from tsp_plotter.solution import solution_plotter
from tsp_plotter.problem import problem_generator
from tsp_plotter.output_files import OutputFiles

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="salesman",
        description="Travelling salesman - problem generator / solution plotter",
    )
    parser.add_argument(
        "-o",
        "--output_dir",
        type=str,
        metavar="DIR",
        default="output",
        dest="output_dir",
        help="output directory",
    )
    subparsers = parser.add_subparsers(
        help="Available commands",
        description="Command help",
        dest="subcommand",
        required=True,
    )

    # Create a problem

    create_parser = subparsers.add_parser(
        "create",
        help="Generate a problem",
    )
    create_parser.add_argument(
        "num_points",
        type=int,
        help="Number of points in the problem",
    )
    create_parser.add_argument(
        "-a",
        "--arc",
        help="Points form an arc",
        action="store_true",
    )

    # Plot a solution

    plot_parser = subparsers.add_parser(
        "plot",
        help="Plot a solution",
    )
    plot_parser.add_argument(
        "solution",
        help="Input file containing the solution path",
    )
    plot_parser.add_argument(
        "problem",
        help="Input file containing the points defining the problem",
    )

    args = parser.parse_args()

    if len(args.output_dir) > 0:
        path = args.output_dir
        if not os.path.exists(path):
            os.makedirs(path)

    print(f"args is {args}")

    output_files = OutputFiles(args.output_dir)

    if args.subcommand == "create":
        problem_generator.generate_problem(
            args.num_points,
            args.arc,
            output_files.problem,
            output_files.problem_image,
            output_files.distance_matrix,
        )

    elif args.subcommand == "plot":
        solution_plotter.plot_solution(
            args.solution, args.problem, output_files.solution_image
        )
    else:
        print(f"unknown command: {args.subcommand}", file=sys.stderr)
