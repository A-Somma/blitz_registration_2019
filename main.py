import src.solver as solver
from src.node import Node

def main():
    partial_path = Path()
    starting_node = Node(x_coordinate=0, y_coordinate=0)
    destination_node = Node(x_coordinate=5, y_coordinate=5)

    complete_path = solver.solve(partial_path, starting_node, destination_node)

    return complete_path

if __name__ == "__main__":
    main()