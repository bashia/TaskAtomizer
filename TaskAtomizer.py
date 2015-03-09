


class Atom:
    def Atom():
        self.description = ""

class Task:
    def Task():
        self.description = ""
        self.atoms = Atom():

class Goal:
    def Goal():
        self.description = ""
        self.tasks = Task()
