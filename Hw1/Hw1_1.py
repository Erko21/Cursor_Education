class Animals():
    def __init__(self, anymal_type, name, age):
        self.anymal_type = anymal_type
        self.name = name
        self.age = age

    def my_animal(self):
        print(f"I have a {self.anymal_type} which is called {self.name.title()} and it is {self.age} years old!")

class Dog(Animals):
    def voice(self):
        print(f"My {self.anymal_type} can bark really loud)")

class Fly(Animals):
    def __init__(self,anymal_type, name , age , wing_size):
        super().__init__(anymal_type, name , age)
        self.anymal_type = anymal_type
        self.name = name
        self.age = age
        self.wing_size = wing_size

    def wings(self):
        print(f"My {self.anymal_type} can fly very height and it has {self.wing_size} santimeters wings!")

class Restoration(Animals):
    def wizzard_repair(self):
        print(f"My {self.anymal_type} can repair its legs only in one day!Can u imagine that?")

class Frog(Animals):
    def __init__(self, anymal_type, name, age, full_length, body_length):
        super().__init__(anymal_type, name, age)
        self.full_length = full_length
        self.body_length = body_length

    def legs_length(self):
        length = self.full_length - self.body_length
        print(f"My {self.anymal_type} has {length} santimeters legs!")

class Counting_legs(Animals):
    def __init__(self, anymal_type, name, age, legs):
        super().__init__(anymal_type, name, age)
        self.legs = legs
    def leg(self):
        if self.legs == 4:
            print(f"My {self.anymal_type} can run really fast!")
        elif self.legs == 2 :
            print(f"My {self.anymal_type} can fly really hight!")
        else: print(f"My {self.anymal_type} have {self.legs} legs")

m_anymal = Animals('dog', 'petty', 16)
m_anymal.my_animal()

dog = Dog('dog', 'petty', 10)
dog.my_animal()
dog.voice()

fly = Fly('bird', 'carol', 4, 30)
fly.my_animal()
fly.wings()

wizzard = Restoration('wizzard', 'blow', 1)
wizzard.my_animal()
wizzard.wizzard_repair()

frog = Frog('frog', 'carol', 1, 25, 19)
frog.my_animal()
frog.legs_length()

legs = Counting_legs('bird', 'piko', 3, 4)
legs.my_animal()
legs.leg()