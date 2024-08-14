class Man:
    def __init__(self, name) -> None:
        self.name = name
        print("Init")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("bye" + self.name)

m = Man("john")
m.hello()
m.goodbye()
