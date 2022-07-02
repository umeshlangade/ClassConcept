class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hello,", self.name, "this side..!!")


if __name__ == "__main__":
    p = Person("UMESH")
    p.say_hi()
