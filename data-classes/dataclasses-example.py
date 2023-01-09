from dataclasses import dataclass, field


@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        self.sort_index = self.age

    def __str__(self) -> str:
        return f"{self.name} | {self.job} | {self.age}"


@dataclass(order=True, frozen=True)
class ReadOnlyPerson:
    """Read Only Person"""
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.strength)


person1 = Person("Geralt", "Witcher", 30)
person2 = Person("Yennnefer", "Sorceress", 25)
person3 = Person("Yennnefer", "Sorceress", 25)


if __name__ == "__main__":
    print(f"The id of person2: {id(person2)}")
    print(f"The id of person3: {id(person3)}")
    print("Print of person1:")
    print(person1)
    print(f"Is person2 == person3? {person2 == person3}")
    print(f"Is person1 > person2? {person1>person2}")
