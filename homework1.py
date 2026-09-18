class Task:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.d = False


class TaskManager:
    def __init__(self):
        self.t = []

    def add(self, x):
        self.t.append(x)

    def delete(self, x):
        self.t.remove(x)

    def done(self, x):
        x.d = True

    def show(self):
        for x in self.t:
            if x.d == True:
                s = "виконано"
            else:
                s = "не виеонано"
            print(f"{x.a} | {x.b} | {x.c} | {s}")
