class Subject:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


class Observer:
    def update(self, message):
        print(f"Наглядач {self.id} отримав: {message}")


if __name__ == "__main__":
    subject = Subject()

    observer1 = Observer()
    observer1.id = 1
    subject.register(observer1)

    observer2 = Observer()
    observer2.id = 2
    subject.register(observer2)

    subject.notify("Привіт від Суб'єкта!")

    subject.unregister(observer1)
    subject.notify("Папа від суб'єкта!")
