class Plant:
    def __init__(self, name, age, height):
        self.height = height
        self.name = name
        self.age = age
    def show(self):
        print(f"{self.name}: {self.height} cm, {self.age} days old")

if __name__ == "__main__":
    x = Plant("Rose", 30, 25)
    y = Plant("Sunflower", 45, 80)
    z = Plant("Cactus", 120, 15)

    x.show()
    y.show()
    z.show()