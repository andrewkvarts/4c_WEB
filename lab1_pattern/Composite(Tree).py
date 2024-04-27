class Component:
    def __init__(self, name):
        self.name = name
    def add(self, component):
        raise NotImplementedError()
    def remove(self, component):
        raise NotImplementedError()
    def operation(self):
        raise NotImplementedError()

class Leaf(Component):
    def __init__(self, name):
        super().__init__(name)
    def add(self, component):
        raise NotImplementedError("Leaf cannot have children")
    def remove(self, component):
        raise NotImplementedError("Leaf cannot have children")
    def operation(self):
        print(f"{self.name} виконується")


class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = []
    def add(self, component):
        self.children.append(component)
    def remove(self, component):
        self.children.remove(component)
    def operation(self):
        for child in self.children:
            child.operation()


if __name__ == "__main__":
    root = Composite("Root")
    leaf1 = Leaf("Leaf 1")
    leaf2 = Leaf("Leaf 2")
    composite1 = Composite("Composite 1")

    composite1.add(leaf3 := Leaf("Leaf 3"))
    composite1.add(leaf4 := Leaf("Leaf 4"))

    root.add(leaf1)
    root.add(leaf2)
    root.add(composite1)

    root.operation()
