
class Node():

    def __init__(self, x_coordinate=0, y_coordinate=0):
        self.x=x_coordinate
        self.y=y_coordinate

    def __str__(self):
        return str((self.x, self.y))

    def __eq__(self, node):
        return (self.x == node.x and self.y == node.y)

    def __hash__(self):
        coordinate = str(self.x)+str(self.y)
        return hash(coordinate)

    def moveTo(self, command):
        if command == "u":
            return Node(self.x - 1, self.y)
        if command == "d":
            return Node(self.x + 1, self.y)
        if command == "r":
            return Node(self.x, self.y + 1)
        if command == "l":
            return Node(self.x, self.y - 1)

    def moveFrom(self, command):
        if command == "u":
            return Node(self.x + 1, self.y)
        if command == "d":
            return Node(self.x - 1, self.y)
        if command == "r":
            return Node(self.x, self.y - 1)
        if command == "l":
            return Node(self.x, self.y + 1)
