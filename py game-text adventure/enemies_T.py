class Enemy:
    def__init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def_str_(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

class GiantSpider(Enemy):
        def_init_(self):
            self.name = "Giant Spider"
            self.hp = 10
            self.damage = 2

class Orge(Enemy):
    def_innit_(self):
        self.name = "Ogre"
        self.hp = 30
        self.damage = 10

class BatColony(Enemy):
    def_innit_(self):
        self.name = "Colony of bats"
        self.hp = 100
        self.damage = 4

class RockMonster(Enemy):
    def_init_(self):
        self.name = "Rock Monster"
        self.hp = 80
        self.damage = 15




