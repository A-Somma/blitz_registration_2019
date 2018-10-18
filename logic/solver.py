from logic.recurrence_table import RecurrenceTable
def solve(partial_path, starting_node, destination_node):
    r = RecurrenceTable(path=partial_path)
    r.set_starting_point(starting_node)
    r.fill_table()
    print(r)
    return r.backtrack(destination_node, len(partial_path)-1)
    