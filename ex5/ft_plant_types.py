class Plant:
    def __init__(self, name : str, height : float,  age : int):
        self._height = 0
        self._age = 0
        self.name = name
        self.set_height(height)
        self.set_age(age)
    def set_age(self, age):
        if age < 0:
            print("Error, age can't be negative")
        else:
            self._age = age
    def set_height(self, height):
        if height < 0:
            print("Error, height can't be negative")
        else:
            self._height = height
    def show(self):
        print(f"{self.name}: {self._height}cm, {self._age} days old")
    def get_height(self):
        return self._height
    def get_age(self):
        return self._age
    def age(self):
        self._age += 1
    def grow(self):
        self._height += 1

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)  
        self.color = color
        self.bloomed = False
    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed == True:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")
    def bloom(self):
        self.bloomed = True
class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")
    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide.")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")
    def age(self):
        super().age()
        self.nutritional_value += 1


if __name__ == "__main__":
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()