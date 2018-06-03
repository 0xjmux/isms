import enemies
import npc
import random

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass
    
    def dialogue(self):
        pass
    
        

###BOOL DEFINITIONS
visited_gallows = False


class startTile(MapTile):
    def intro_text(self):
        return """
        You find yourself on the edge of the atlantic ocean. To the south, you can see a small village, with what seem to be pilgrims. 
        """

class puritanVillage(MapTile):
    def intro_text(self):
        return """As you approach the village, it turns out that these settlers are puritans, not pilgrims. 
        They appear to be approaching the tallest building in the village, which appears to be a church. """

class deadEnd(MapTile):
    def intro_text(self):
        return """Oops! You seem to have ended up in a dead end. It looks like there's no way out other than the way you came in. """""

class gallows(MapTile):
    def intro_text(self):
        visited_gallows = True
        return """You approach the end of the puritan village, and see some newly erected gallows. There's 3 figures hanging off of it, and another one 
        covered in heavy bricks. You wonder what crimes these people committed to end up this way, as their bodies slowly spin in the breeze. """
    
class church(MapTile):
    def intro_text(self):
        return """The tallest building in the village is the church, and it's at the very end of the town. The bell is ringing, and the church seems to be just getting out. 
        People pour out, dressed in very traditional clothes. """
    ###################################ADD DIALOG FUNCTION
class proctorsHouse(MapTile):
    def intro_text(self):
        
        output = """You approach a very traditional looking house, made completely out of logs. It's well built, and has a tall chimney that sticks up out of the roof. """
        
        if visited_gallows:
            output += "You wonder if this was the house of one of the men who were hung in the gallows."
            
        return output
    
class oldRoad(MapTile):
    def intro_text(self):
        return """You turn away from the church, and down an old road. It's made of dirt, and isn't very well worn. It looks like you're one of the first people to use it, 
        but it seems like the children from the puritan village play near it, as there are plenty of tiny footprints. """

    
class deism(MapTile):
    def intro_text(self):
        return """"""
    
class benFranklin(MapTile):
    def intro_text(self):
        return """"""
    
class WashingtonSpeech(MapTile):
    def intro_text(self):
        return """"""
    
class Battlefield(MapTile):
    def intro_text(self):
        return """"""
    
class oldForest(MapTile):
    def intro_text(self):
        return """"""    
    
class romanticism(MapTile):
    def intro_text(self):
        return """"""
    
class romanticismHouse(MapTile):
    def intro_text(self):
        return """"""
    
class sideExit(MapTile):
    def intro_text(self):
        return """"""
    
class deadEnd(MapTile):
    def intro_text(self):
        return """"""
    
class RealismTown(MapTile):
    def intro_text(self):
        return """"""    
    
class smallCafe(MapTile):
    def intro_text(self):
        return """"""
    
class modernism(MapTile):
    def intro_text(self):
        return """"""
    
class MarxRally(MapTile):
    def intro_text(self):
        return """"""
    
class westEgg(MapTile):
    def intro_text(self):
        return """"""
    
    
class multiplePerspectives(MapTile):
    def intro_text(self):
        return """"""
    
class HarlemRenaissance(MapTile):
    def intro_text(self):
        return """"""
    
class gatsby(MapTile):
    def intro_text(self):
        return """"""
    
class trainStation(MapTile):
    def intro_text(self):
        return """"""
    
class zeitgeist(MapTile):
    def intro_text(self):
        return """"""
    
class existence(MapTile):
    def intro_text(self):
        return """"""    

class museum(MapTile):
    def intro_text(self):
        return """"""
    
class carousel(MapTile):
    def intro_text(self):
        return """"""
    
class A21(MapTile):
    def intro_text(self):
        return """"""
    
  
#class EnemyTile(MapTile):
    #def __init__(self, x, y):
        #r = random.random()
        #if r < 0.50:
            #self.enemy = enemies.GiantSpider()
            #self.alive_text = "A giant spider jumps down from " \
                              #"its web in front of you!"
            #self.dead_text = "The corpse of a dead spider " \
                             #"rots on the ground."
        #elif r < 0.80:
            #self.enemy = enemies.Ogre()
            #self.alive_text = "An ogre is blocking your path!"
            #self.dead_text = "A dead ogre reminds you of your triumph."
        #elif r < 0.95:
            #self.enemy = enemies.BatColony()
            #self.alive_text = "You hear a squeaking noise growing louder" \
                              #"...suddenly you are lost in s swarm of bats!"
            #self.dead_text = "Dozens of dead bats are scattered on the ground."
        #else:
            #self.enemy = enemies.RockMonster()
            #self.alive_text = "You've disturbed a rock monster " \
                              #"from his slumber!"
            #self.dead_text = "Defeated, the monster has reverted " \
                             #"into an ordinary rock."

        #super().__init__(x, y)

    #def intro_text(self):
        #text = self.alive_text if self.enemy.is_alive() else self.dead_text
        #return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".
                  format(self.enemy.damage, player.hp))


class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
        
        """


#class FindGoldTile(MapTile):
    #def __init__(self, x, y):
        #self.gold = random.randint(1, 50)
        #self.gold_claimed = False
        #super().__init__(x, y)

    #def modify_player(self, player):
        #if not self.gold_claimed:
            #self.gold_claimed = True
            #player.gold = player.gold + self.gold
            #print("+{} gold added.".format(self.gold))

    #def intro_text(self):
        #if self.gold_claimed:
            #return """
            #Another unremarkable part of the cave. You must forge onwards.
            #"""
        #else:
            #return """
            #Someone dropped some gold. You pick it up.
            #"""


#class TraderTile(MapTile):
    #def __init__(self, x, y):
        #self.trader = npc.Trader()
        #super().__init__(x, y)

    #def check_if_trade(self, player):
        #while True:
            #print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            #user_input = input()
            #if user_input in ['Q', 'q']:
                #return
            #elif user_input in ['B', 'b']:
                #print("Here's whats available to buy: ")
                #self.trade(buyer=player, seller=self.trader)
            #elif user_input in ['S', 's']:
                #print("Here's whats available to sell: ")
                #self.trade(buyer=self.trader, seller=player)
            #else:
                #print("Invalid choice!")

    #def trade(self, buyer, seller):
        #for i, item in enumerate(seller.inventory, 1):
            #print("{}. {} - {} Gold".format(i, item.name, item.value))
        #while True:
            #user_input = input("Choose an item or press Q to exit: ")
            #if user_input in ['Q', 'q']:
                #return
            #else:
                #try:
                    #choice = int(user_input)
                    #to_swap = seller.inventory[choice - 1]
                    #self.swap(seller, buyer, to_swap)
                #except ValueError:
                    #print("Invalid choice!")

    #def swap(self, seller, buyer, item):
        #if item.value > buyer.gold:
            #print("That's too expensive")
            #return
        #seller.inventory.remove(item)
        #buyer.inventory.append(item)
        #seller.gold = seller.gold + item.value
        #buyer.gold = buyer.gold - item.value
        #print("Trade complete!")

    #def intro_text(self):
        #return """
        #A frail not-quite-human, not-quite-creature squats in the corner
        #clinking his gold coins together. He looks willing to trade.
        #"""


start_tile_location = None          #some bullshit I added to make this spaghetti code (not) work
world_map = []
<<<<<<< HEAD
string_to_class_map = {}
 
=======

string_to_class_map = {"startTile": startTile,
                       "puritanVillage": puritanVillage}
>>>>>>> 6d36196a9d02d5f4f302e29b00085e78768b7091
 
def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('world/map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t')) # Assumes all rows contain the same number of tabs
    for y in range(len(rows)):
        row = []
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '') # Windows may need to replace '\r\n'
            #print(tile_name)    #for when I'm having problems with this stupid ass function
            if tile_name == 'startTile':
                global start_tile_location
                start_tile_location = (x, y) 
                #print(start_tile_location)
            row.append(string_to_class_map[tile_name](x, y) if tile_name else None)
        world_map.append(row)



#world_dsl = """
#|EN|EN|VT|EN|EN|
#|EN|  |  |  |EN|
#|EN|FG|EN|  |TT|
#|TT|  |ST|FG|EN|
#|FG|  |EN|  |FG|
#"""


#def is_dsl_valid(dsl):
    #if dsl.count("|ST|") != 1:
        #return False
    #if dsl.count("|VT|") == 0:
        #return False
    #lines = dsl.splitlines()
    #lines = [l for l in lines if l]
    #pipe_counts = [line.count("|") for line in lines]
    #for count in pipe_counts:
        #if count != pipe_counts[0]:
            #return False

    #return True

#tile_type_dict = {"VT": VictoryTile,
                  #"EN": EnemyTile,
                  #"ST": StartTile,
                  #"FG": FindGoldTile,
                  #"TT": TraderTile,
                  #"  ": None}


#def parse_world_dsl():
    #if not is_dsl_valid(world_dsl):
        #raise SyntaxError("DSL is invalid!")

    #dsl_lines = world_dsl.splitlines()
    #dsl_lines = [x for x in dsl_lines if x]

    #for y, dsl_row in enumerate(dsl_lines):
        #row = []
        #dsl_cells = dsl_row.split("|")
        #dsl_cells = [c for c in dsl_cells if c]
        #for x, dsl_cell in enumerate(dsl_cells):
            #tile_type = tile_type_dict[dsl_cell]
            #if tile_type == StartTile:
                #global start_tile_location
                #start_tile_location = x, y
            #row.append(tile_type(x, y) if tile_type else None)

        #world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None

#def tile_exists(x, y):
    #"""Returns the tile at the given coordinates or None if there is no tile.
    #:param x: the x-coordinate in the worldspace
    #:param y: the y-coordinate in the worldspace
    #:return: the tile at the given coordinates or None if there is no tile
    #"""
    #return _world.get((x, y))
