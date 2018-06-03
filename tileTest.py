
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass

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
        return """"""

class gallows(MapTile):
    def intro_text(self):
        return """"""
    
class church(MapTile):
    def intro_text(self):
        return """"""
    
class proctorsHouse(MapTile):
    def intro_text(self):
        return """"""
    
class oldRoad(MapTile):
    def intro_text(self):
        return """"""
    
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
