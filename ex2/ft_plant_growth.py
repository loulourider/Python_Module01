class Plant:
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float = 0.8) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.age_days} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.age_days += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    start_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {day} ===")
        rose.show()
    print(f"Growth this week: {round(rose.height - start_height, 1)}cm")
