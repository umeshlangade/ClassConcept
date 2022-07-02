class Addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("first number ", self.first)
        print("second number ", self.second)
        print("addition of two number is", self.answer)

    def calculate(self):
        self.answer = self.first + self.second

    # Deleting calling destructor
    def __del__(self):
        print("destructor called, Addition is deleted.")


if __name__ == "__main__":
    obj = Addition(100, 200)
    obj.calculate()
    obj.display()
    # calling destructor
    del obj
