class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name


class Weapon1(Weapon):
    def __init__(self):
        self.name = "Weapon1"
        self.description = "......."
        self.damage = 5


class Weapon2(Weapon):
    def __init__(self):
        self.name = "Weapon2"
        self.description = "....... " \
                           "......."
        self.damage = 10


class Weapon3(Weapon):
    def __init__(self):
        self.name = "Weapon3"
        self.description = "......... " \
                           "........"
        self.damage = 20
