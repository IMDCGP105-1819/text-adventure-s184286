import enemies
import npc
import random

class MapTile:
    def_init_(self,x,y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self,player):
        pass

    class StartTile(MapTile):
        def intro_text(self):
            return """
            You find yourself in a cave with a flickering torch on the wall.
            You can make out four paths, each equally as dark and foreboding.
            """

    class EnemyTile(MapTile):
        def _init_(self,x,y):
            r = random.random()
            if r < 0.50:
                self.enemy = enemies.GiantSpider()
                self.alive_text = "A giant spider jumps down from "\
                                   "its web in fromt of you!"
                self.dead_text = "The corpse of a dead spider " \
                                   "rots on the ground."
                elif r < 0.80:
                    self.enemy = enemies.Ogre()
                    self.alive_text = "An ogre is blocking your path!"
                    slef.dead_text ="A dead orge reminds you of your triumph."
                elif r < 0.95:
                    self.enemy = enemies.batColony()
                    self.alive_text = ""
                    self.dead_text = ""

                 super().__init__(x,y)

                 def intro_text(self):


