### Problem generator and Solution Plotter for the [Travelling Salesman](https://github.com/damonf/travelling_salesman) project.

![ci-tests](https://github.com/damonf/travelling-salesman-plotter/actions/workflows/ci-tests.yml/badge.svg)

## Sample Usage

```bash
# Generate a problem (an arc with 10 points):
poetry run python ./src/tsp_plotter/main.py create -a 10

# Plot a solution to a problem:
poetry run python ./src/tsp_plotter/main.py plot solution.txt problem.txt

```

## License

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)

