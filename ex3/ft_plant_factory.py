class Plant:
    def __init__(self, name : str, age : int, height : float):
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
    rose = Plant("Rose", 30, 25.0)
    oak = Plant("Oak", 365, 200.0)
    cactus = Plant("Cactus", 90, 5.0)
    sunflower = Plant("Sunflower", 45, 15.0)
    fern = Plant("Fern", 120, 15.0)
    plantes = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")
    for i in plantes:
        i.show()
    