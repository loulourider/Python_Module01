class Plant:
    def __init__(self, name : str, age : int, height : int):
        self.h = height
        self.n = name
        self.a = age
    def show(self):
        print(f"{self.n}: {self.h} cm, {self.a} days old")
    def age(self):
        self.a += 1
    def grow(self):
        self.h += 1

if __name__ == "__main__":
    x = Plant("Rose", 30, 25)
    for i in range(6):
        x.show()
        x.age()
        x.grow()
    x.show()
