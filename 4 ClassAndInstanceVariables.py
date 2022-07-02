# Python3 program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.

class Dog:
    animal = 'dog'

    def __init__(self, breed, color, age):
        self.breed = breed
        self.color = color
        self.age = age


def fn_execution_method():
    rodger = Dog("Pug", "Brown", 10)
    buz = Dog("Bulldog", "Black", 12)

    print("RODGER DETAILS..")
    print('rodger is a', rodger.animal)
    print('breed ', rodger.breed)
    print('color ', rodger.color)
    print('age ', rodger.age)

    print("\nBUZO DETAILS")
    print("buzo is a", buz.animal)
    print("breed", buz.breed)
    print("color", buz.color)
    print("age", buz.age)


if __name__ == "__main__":
    fn_execution_method()
    print("\nAccessing class variable using class name")
    print(Dog.animal)
