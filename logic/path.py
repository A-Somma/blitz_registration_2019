

class Path():

    def __init__(self, commands):
        self.commands = ["f"]
        for command in commands:
            self.commands.append(command)

    def __getitem__(self, i):
        return self.commands[i]

    def __len__(self):
        return len(self.commands)

    def command(self, i):
        return self[i]
