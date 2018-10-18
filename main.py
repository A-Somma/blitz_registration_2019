import logic.solver as solver
from logic.node import Node
from logic.path import Path
from logic.recurrence_table import RecurrenceTable

def main():
    partial_path = Path("dddd????")
    starting_node = Node(x_coordinate=0, y_coordinate=0)
    destination_node = Node(x_coordinate=4, y_coordinate=4)

    complete_path = solver.solve(partial_path, starting_node, destination_node)

    print("Unscrambled path: "+str(complete_path))

if __name__ == "__main__":
    main()