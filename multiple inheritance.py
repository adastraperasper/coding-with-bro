# multiple inheritence

class Prey:

    def flee(self):
        print("This animal is running")

class Predator:

    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass


class Fish(Prey,Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()


fish.flee()
fish.hunt()

