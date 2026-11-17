class Plant:
    def __init__(self, name : str, height : float,  age : int):
        self.set_height(height)
        self._height = 0
        self._age = 0
        self.name = name 
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
    def get_height(self):
        return self._height
    def get_age(self):
        return self._age


if __name__ == "__main__":
    print("=== Création valide ===")
    rose = Plant("Rose", 25.0, 30)
    print(f"{rose.name}: {rose.get_height()}cm, {rose.get_age()} days old")

    print("\n=== Modifications valides ===")
    rose.set_height(40.0)
    rose.set_age(35)
    print(f"{rose.name}: {rose.get_height()}cm, {rose.get_age()} days old")

    print("\n=== Modifications invalides ===")
    rose.set_height(-10)
    rose.set_age(-5)
    print(f"{rose.name}: {rose.get_height()}cm, {rose.get_age()} days old")

    print("\n=== Constructeur avec valeurs invalides ===")
    bad = Plant("Cactus", -5.0, -20)
    print(f"{bad.name}: {bad.get_height()}cm, {bad.get_age()} days old")