import items

class NonPlayableCharacter():
    def _init_(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def _str_(self):
        return self.name

    class Trader(NonPlayableCharacter):
        def _init_(self):
            self.name = "Trader"
            self.gold = 100
            self.inventory = [items.CrustyBread(),
                              items.CrustyBread(),
                              items.CrustyBread(),
                              items.HealingPotion(),
                              dict_items.HealingPotion()]

