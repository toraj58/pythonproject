class Shark():
    def swim(self):
        print("The shark is swimming.")

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")


class Clownfish():
    def swim(self):
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")


shark=Shark()
clown=Clownfish()
shark.skeleton()
clown.skeleton()

# Polymorphism with Class Methods
for fish in (shark,clown):
    fish.swim()

#  Polymorphism with a Function
def classmethod(fish):
    fish.swim_backwards()

classmethod(shark)
classmethod(clown)