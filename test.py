class RockBand:
    def __init__(self, name: str, members: list) -> None:
        self.name = name
        self.members = members

    def add_new_member(self, new_member: str) -> None:
        if new_member not in self.members:
            self.members.append(new_member)
        else:
            print(f"{new_member} is already in the band!")

    def __add__(self, other: "RockBand") -> "RockBand":
        new_name = f"{self.name} {other.name} United"
        new_members = self.members = list(set(self.members + other.members))
        return RockBand(new_name, new_members)


the_beatles = RockBand(
    "The Beatles",
    ["John Lennon", "Paul McCartney", "George Harrison"]
)

the_beatles.add_new_member("Ringo Starr")
the_beatles.add_new_member("John Lennon")  # John Lennon already
# in the band

first_band = RockBand("First", ["Ivan", "Sergey"])
second_band = RockBand("Second", ["Sergey", "Max"])
united = first_band + second_band
print(united.name, united.members)  # "First Second United" ["Ivan",
# "Sergey", "Max"]
