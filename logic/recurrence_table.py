from logic.path import Path
from logic.node import Node

class RecurrenceTable():

    def __init__(self, girdsize=5, path=Path("")):
        self.table = dict()
        self.path = path
        for i in range(5):
            for j in range(5):
                row = list()
                for k in range(len(self.path)):
                    row.append((-1, "?"))
                self.table[Node(i, j)] = row

    def __str__(self):
        res = (50*"="+"\n")
        for i in range(len(self.path)):
            res += "For i = {} \n".format(i)
            for j in range(5):
                row = ""
                for k in range(5):
                    row += str(self.table[Node(j, k)][i])
                res+=(row+"\n")
            res += (50*"-" + "\n")
        res += (50*"="+"\n")
        return res

    def __getitem__(self, args):
        node, i = args
        if node in self.table.keys():
            return self.table[node][i]
        else:
            return (-1, "?")

    def __setitem__(self, args, item):
        node, i = args
        if node in self.table.keys():
            self.table[node][i] = item

    def set_starting_point(self, starting_node):
        self.table[starting_node][0] = (0, "f")

    def fill_table(self):
        for i in range(1, len(self.path)):
            self.fill_row(i)

    def fill_row(self, i):
        for dest_node in self.table.keys():
            self.update_node(dest_node, i)

    def update_node(self, node, i):
        if self.path.command(i) in ("udlr"):
            origin_node = node.moveFrom(self.path.command(i))
            self[node, i] = (self[origin_node, i-1][0], self.path.command(i))
        elif self.path.command(i) == "?":
            new_command = self.maximize_command(node, i)
            if new_command:
                self[node, i] = new_command

    def maximize_command(self, node, i):
        up_node = node.moveTo("u")
        down_node = node.moveTo("d")
        left_node = node.moveTo("l")
        right_node = node.moveTo("r")
        if self[up_node, i-1][0] == 0:
            return (0, "d")
        elif self[down_node, i-1][0] == 0:
            return (0,"u")
        elif self[left_node, i-1][0] == 0:
            return (0, "r")
        elif self[right_node, i-1][0] == 0:
            return (0,"l")

    def backtrack(self, cursor, i):
        if self[(cursor, i)][0]==-1:
            return False
        commands = ""
        for j in range(i, 0, -1):
            command = self[(cursor, j)][1]
            commands = command + commands
            cursor = cursor.moveFrom(command)
        return Path(commands)
