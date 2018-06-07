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
washingtonSpeech = False
marxSpeech = False

class startTile(MapTile):
    def intro_text(self):
        return """
        You find yourself on the edge of the Atlantic ocean. To the south, you can see a small village, with what seem to be pilgrims. 
        """

class puritanVillage(MapTile):
    def intro_text(self):
        return """As you approach the village, it turns out that these settlers are puritans, not pilgrims. They appear to be approaching the tallest building in the village, which appears to be a church. """

class deadEnd(MapTile):
    def intro_text(self):
        return """Oops! You seem to have ended up in a dead end. It looks like there's no way out other than the way you came in. """""

class gallows(MapTile):
    def intro_text(self):
        global visited_gallows
        visited_gallows = True
        return """You approach the end of the puritan village, and see some newly erected gallows. There's 3 figures hanging off of it, and another one covered in heavy bricks. You wonder what crimes these people committed to end up this way, as their bodies slowly spin in the breeze. """
    
class church(MapTile):
    def intro_text(self):
        return """The tallest building in the village is the church, and it's at the very end of the town. The bell is ringing, and the church seems to be just getting out. People pour out, dressed in very traditional clothes. A teenage girl approaches you. """
    
class proctorsHouse(MapTile):
    def intro_text(self):
        
        output = """You approach a very traditional looking house, made completely out of logs. It's well built, and has a tall chimney that sticks up out of the roof. """
        
        if visited_gallows:
            output += "You wonder if this was the house of one of the men who were hung in the gallows."
            
        return output
    
class oldRoad(MapTile):
    def intro_text(self):
        return """You turn away from the church, and down an old road. It's made of dirt, and isn't very well worn. It looks like you're one of the first people to use it, but it seems like the children from the puritan village play near it, as there are plenty of tiny footprints. """

    
class deism(MapTile):
    def intro_text(self):
        return """As you come to the end of the old road, you come into a newer looking village. It's laid out very rationally, with a town square and houses, but there isn't a church to be seen. This is quite a depart from the last village. A little further along you see an older man waiting. """
    
class benFranklin(MapTile):
    def intro_text(self):
        return """Upon much suprise, you find that that older man was Ben Franklin. He looks like he wants to talk to you. """
    
class WashingtonSpeech(MapTile):
    def intro_text(self):
        global washingtonSpeech
        if washingtonSpeech == False:
            washingtonSpeech = True
            return "As you walk past Ben Franklin, you can see George Washington standing upon a wooden stage, in the center of the town. He's in the middle of giving a battle speech to his soldiers, and as you stand at the back of the crowd you catch the last few words. He's saying something about the need for rationalism and independence, along with the necessity of the need of separation of church and state. The soldiers walk to the east, towards what you assume is the battlefield. "
        else:
            return """This appears to be an empty ampitheater. You can hear some gunshots to the east, piercing through the summer's breeze. """
    
class Battlefield(MapTile):
    def intro_text(self):
        return """As you enter this battlefield, you see Washington's army taking a stand against the redcoats. Both sides are firing against each other, and to avoid getting hit you crouch behind a cart filled to the brim with hay. """
    
class oldForest(MapTile):
    def intro_text(self):
        return "As you walk away from the deist town, you enter a looming forest. As you trek through it turns to night, and you feel the piercing gaze of eyes glaring at you from every corner, but you can't see anything when you look. Eventually, a strange figure with a pumpkin for a head runs out of the trees in from of you, dragging the body of some poor soul. You carry on, ever wary of what is ahead. "    
    
class romanticism(MapTile):
    def intro_text(self):
        return """You finally come to a small gap in the trees. A small cottage lies ahead of you, with a thatched roof and a middle-aged man watering some plants. You approach him, and he turns to you as if to tell you something. """
    
class romanticismHouse(MapTile):
    def intro_text(self):
        return """Inside the house, there is fancy design, and the walls are adorned with bricks. There are bright white curtains, and an intricate fireplace, all surrounded by wooden furniture. """
    
class sideExit(MapTile):
    def intro_text(self):
        return """You exit through the side door of the house, and start walking on the only other path out of the small break in the woods. It's dawn, and the sunrise through the trees gives a warm 
        aesthetic."""
    
class RealismTown(MapTile):
    def intro_text(self):
        return "As you apporach the next village, you notice that it is realistically depicted, and significantly more advanced, with streetlights, and other facilities. Everything is realistically portrayed, exactly as it is seen. There's a small cafe to your south, with a dim streetlight and some light chatter carrying away from the patrons there. "    
    
class smallCafe(MapTile):
    def intro_text(self):
        return """As you enter the cafe, a tall well dressed main who you recognize as Mark Twain, or rather Samuel Clemens, greets you as you enter. """
    
class modernism(MapTile):
    def intro_text(self):
        return "As you walk out of the cafe, you stroll through the rest of the town, and eventually make your way to the outskirts. You venture out onto the road again, but this time it's well paved and is brightly lit byb streetlamps. As you stroll along, you make your way into the next town. The buildings in this town are futuristic, with intricate design and tall, shiny exteriors. "
    
class MarxRally(MapTile):   #no values, anti-traditionalism, people make their own meaning
    def intro_text(self):
        global marxSpeech
        if marxSpeech == False:
            marxSpeech = True
            return "As you walk into the town, a bearded man is excitedly lecturing to a crowd. As you approach, you recognize him as Karl Marx. Again, you only catch the end of the speech, but you hear him lecture that humans have no intrinsic values, and anti-traditionalism is important. He tells the crowd that people make their own meaning, and it is important to band together in order to overcome life's challenges. As the speech ends, Marx retreats into the back of the stage. People disperse, and you eventually find yourself in an empty town center. "
        else:
            return """You find yourself in an almost empty town center. It looks futuristic, and it appears that there was a speech here a while ago. """
    
class westEgg(MapTile):   #“So we beat on, boats against the current, borne back ceaselessly into the past.” - reflection on pointlessness of life, how we’ll never win, but we keep on trying. 

    def intro_text(self):
        return """As you beat on through the city, against waves of traffic, you find yourself on Long Island, near a place called West Egg. You meet a handsome man, who introduces himself as F. Scott Fitzgerald."""
    
    
class multiplePerspectives(MapTile):  #single story can be told from multiple perspectives
    def intro_text(self):
        return """As you walk around the town, you notice that different buildings and artworks look very different from varying perspectives. You wonder if it was designed this way, or it just worked out well."""
    
class HarlemRenaissance(MapTile):  #jazz age, black art
    def intro_text(self):
        return """As you explore the city, you stumble into a jazz club. There are black artists playing jazz, and there are plenty of interesting paintings up on the walls. People are writing poetry at the tables. This area of New York seems to be a mecca for African-American culture. """
    
class gatsby(MapTile):
    def intro_text(self):
        return """As you walk out of the jazz club, a Golden Rolls Royce darts past you, weaving through traffic with 3 passengers in the back. """
    
class trainStation(MapTile):
    def intro_text(self):
        return """As you exit the area of Long Island, you saunter over to the train station and catch a train into Manhattan. """
    
class zeitgeist(MapTile):
    def intro_text(self):
        return "As you pass through the station and out into the streets, you notice a much more modern world. Cars have replaced horse drawn carriages, and people are dressed very different. The spirit of the times has shifted, and people appear much less happy than they did before. Wars and the great depression have had a great effect on the general mood of the people, especially on the artists of the time. "
    
class existence(MapTile):
    def intro_text(self):
        return """You keep walking through the town, and end up just to the west of the natural history museum. """    

class museum(MapTile):
    def intro_text(self):
        return """As you walk inside, a 17 year old with a red hunting cap along with a 10 year old girl following in tow greets you. """
    
class carousel(MapTile):
    def intro_text(self):
        return """You see Holden and his sister walk off to a carousel in the distance, where Holden sits on the bench to contemplate something. As you're standing there, a portal opens to your south. """
    
class A21(MapTile):
    def modify_player(self, player):
        player.victory = True    
    def intro_text(self):
        return """As you walk through the portal, you find yourself in a classroom. There's a large painting on one wall, and a teacher with some interesting, yet strangely familiar tattoos greets you as you enter. 
        Congratulations! You've gained knowledge!"""
    
start_tile_location = None         
world_map = []


string_to_class_map = {"startTile": startTile,
                       "puritanVillage": puritanVillage,
                       "deadEnd":deadEnd,
                       "gallows":gallows,
                       "church":church,
                       "proctorsHouse":proctorsHouse,
                       "oldRoad":oldRoad,
                       "deism":deism,
                       "benFranklin":benFranklin,
                       "oldForest":oldForest,
                       "WashingtonSpeech":WashingtonSpeech,
                       "Battlefield":Battlefield,
                       "romanticism":romanticism,
                       "romanticismHouse":romanticismHouse,
                       "sideExit":sideExit,
                       "RealismTown":RealismTown,
                       "smallCafe":smallCafe,
                       "modernism":modernism,
                       "MarxRally":MarxRally,
                       "westEgg":westEgg,
                       "multiplePerspectives":multiplePerspectives,
                       "HarlemRenaissance":HarlemRenaissance,
                       "gatsby":gatsby,
                       "trainStation":trainStation,
                       "zeitgeist":zeitgeist,
                       "existence":existence,
                       "museum":museum,
                       "carousel":carousel,
                       "A21":A21
                       }

 
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
            if tile_name == 'startTile':
                global start_tile_location
                start_tile_location = (x, y) 
            row.append(string_to_class_map[tile_name](x, y) if tile_name else None)
        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
