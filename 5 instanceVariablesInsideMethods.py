# Python3 program to show that we can create
# instance variables inside methods

class Dog:

    animal = "Dog"

    def __init__(self, breed):
        # Instance Variable
        self.breed = breed

    def set_color(self, color):
        self.color = color


    def get_color(self):
        return self.color


if __name__ == "__main__":
    rodger = Dog("Pug")
    rodger.set_color("Brown")
    print(rodger.get_color())
