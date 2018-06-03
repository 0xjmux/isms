
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass
###VARIABLE DECLARATION FOR CUSTOM OUTCOMES
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
        return """Oops. You've run into a dead end. Looks like there's nowhere to go here. """

class gallows(MapTile):
    def intro_text(self):
        visited_gallows = True
        return """As you walk out of the outskirts of the village, you approach a set of gallows. There are 3 bodies hanging, with no one around 
        to tell of what they did to deserve this. You can smell rotting flesh, and look ahead in horror as their carcasses slowly spin around in the wind. """
    
class church(MapTile):
    def intro_text(self):
        return """You now stand in front of the villages church. It's the tallest building in the village, and is adorned by a white cross at the top. You can hear 
        the bell ringing, and it appears it is time for the village to awake and church to start. """
    
class proctorsHouse(MapTile):
    def intro_text(self):
        if visited_gallows == True:
            return """You turn to a well built wooden house. When you ask a passerby who it belongs to, they quietly whisper 'John Proctor', and then quickly 
        scurry away. You interpret that he might have been one of the hanged """
        else:
            return """You turn to a well built wooden house. When you ask a passerby who it belongs to, they quietly whisper 'John Proctor', and then quickly 
        scurry away. You think he probably isn't very well respected in the village. """
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

_world = {}     #is this needed?

start_tile_location = None          #some bullshit I added to make this spaghetti code work
world_map = []

 
def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('world/map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t')) # Assumes all rows contain the same number of tabs
    for y in range(len(rows)):
        row = []
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '') # Windows users may need to replace '\r\n'
            print(tile_name)
            if tile_name == 'StartingRoom':
                global start_tile_location
                start_tile_location = (x, y)
            row.append(tile_name if tile_name else None)
        world_map.append(row)

load_tiles()
