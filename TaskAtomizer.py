


class Atom:
    def Atom():
        self.description = ""


class Task:
    def Task():
        self.description = ""
        self.atoms = Atom():
        self.priority = 0

class Goal:
    def Goal():
        self.description = ""
        self.tasks = Task()
        self.related = []

class User:
    def User():
        self.name = ""
        self.goals = []
