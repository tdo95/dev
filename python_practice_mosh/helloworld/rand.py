import random

for i in range(3):
    print(random.random())
    print(random.randint(20,40))

# pick random member from a list
members = ['hon', 'hoe', 'hee', 'hoo']
print(random.choice(members))

class Dice:
    def __init__(self, lower, upper):
        self.upper = upper
        self.lower = lower
        self.values = (0, 0)
    def roll(self):
        self.set_random()
        return self.values
    def set_random(self):
        self.values = (random.randint(self.lower, self.upper), random.randint(self.lower, self.upper))

die = Dice(2,20)
print(die.roll())