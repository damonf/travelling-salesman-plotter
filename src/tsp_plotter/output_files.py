import os


class OutputFiles:
    def __init__(self, output_dir):

        self.problem = os.path.join(output_dir, "problem.txt")
        self.problem_image = os.path.join(output_dir, "problem.png")
        self.adjacency_matrix = os.path.join(output_dir, "adjacency_matrix.txt")
        self.solution_image = os.path.join(output_dir, "solution.png")
