class Dog:
    # default constructor
    def __init__(self):
        self.name = "UMESH LANGADE"

    # method for printing data members
    def print_name(self):
        print(self.name)


if __name__ == "__main__":
    objDog = Dog()
    objDog.print_name()