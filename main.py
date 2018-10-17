import logic.solver as solver
from logic.node import Node
from logic.path import Path
from logic.recurrence_table import RecurrenceTable

def main():
    partial_path = Path("llll")
    starting_node = Node(x_coordinate=0, y_coordinate=0)
    destination_node = Node(x_coordinate=5, y_coordinate=5)

    complete_path = solver.solve(partial_path, starting_node, destination_node)

    r = RecurrenceTable(path=Path("??????"))
    r.set_starting_point(Node(0,0))
    r.fill_table()
    print(r)
    return complete_path

if __name__ == "__main__":
    main()