class  Weapon:
    def_init_(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def_str_(self):
        return self.name

class Rock(Weapon):
    def _init_(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5
        self.value = 1

class Dagger(Weapon):
    def_init_(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust."\
                            "Somewhat more dangerous than a rock."
        self.damage = 10
        self.value = 20

class RustySword(Weapon):
    def _init_(self):
        self.name = "Rusty sword"
        self.description = "This sword is showing its age,"\
                            "but still has some fight in it."
        self.damage = 20
        self.value = 100

class Consumable:
    def _init_(self):
        raise "{} (+{}HP)".format(self.name, self.healing_value)

class CrustyBread(Consumable):
    def _init_(self):
        self.name = "Crusty Bread"
        self.healing_value = 10
        self.value = 12

class HealingPotion(Consumable):
    def _init_(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60

