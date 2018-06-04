import items
import world


class Player:
    def __init__(self):
        self.inventory = [items.Dagger(),
                          items.CrustyBread()]
        self.x = world.start_tile_location[0]      
        self.y = world.start_tile_location[1]       
        self.hp = 100
        self.gold = 5
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print('* ' + str(item))
        print("Gold: {}".format(self.gold))

    def heal(self):
        consumables = [item for item in self.inventory
                       if isinstance(item, items.Consumable)]
        if not consumables:
            print("You don't have any items to heal you!")
            return

        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal: ")
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.")

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)

    def dialogue(self):
        d = world.tile_at(self.x, self.y)
        d.check_if_dialogue(self)
        
    def dialogueChurch(self):
        print("Well how do you fare?")
        answer = input()
        print("Well that's nice to hear. What are you wondering about his here village?")
        while True:
            print(" - What is it (1)\n - Is there anywhere else I should explore? (2)\n  - Who are you? (3)\n - Quit(q)")
            user_input = input()
            if user_input in ['Q', 'q']:
                print("fare thee well!")
                return
            elif user_input in ['1']:
                print("This is our puritan village, here in Salem Massachussetts. It was founded in 1626, as a place for our ancestors to escape "
                      "religious persecution. ")
            elif user_input in ['2']:
                print("Yeah, up the road over there there's a new colony being formed. The kids are really taking an interest in it, but the adults are shunning away from it. ")
            elif user_input in ['3']:
                print("I'm Abigail Williams. ")            
                
            else:
                print("Invalid choice!")        
    def dialogueBen(self):
        print("Well how do you fare?")
        print("It's a pleasure to meet you, brave traveler. What can I tell you about our wonderful village?")
        while True:
            print(" - Where are we? (1)\n - Who are you? (2)\n - What do you believe in? (3)\n - What is clockwork religion? (4) \n - Quit(q)")
            user_input = input()
            if user_input in ['Q', 'q']:
                print("fare thee well!")
                return
            elif user_input in ['1']:
                print("We're in Philadelphia, Pennsylvania. This is a place of great thinking, and there are many great minds here planning for the end of the current revolutionary war.  ")
            elif user_input in ['2']:
                print("Why, I'm Ben Franklin. I'm a postmaster, scientist and inventor, among other things.  ")
            elif user_input in ['3']:
                print("We're deists, believing in the prolific use of rational and logical thought in order to understand the natural world. We believe that god can be found in the natural world, "
                      "and that people should have free will and independence. We believe that the separation of church and state is essential, along with the fact that humans are inherently good. ")            
            elif user_input in ['4']:
                print("Clockwork religion is the belief that god created the earth and then left us to our own devices. As such, it is important for humans to be independent so that we can decide our own fate. ")
            else:
                print("Invalid choice!") 
                
                
    def dialogueIrving(self):
        print("Well how do you do")
        
        while True:
            print(" - Where are we? (1)\n - Who are you? (2)\n - What do you believe in? (3)\n - How did you view literature? (4) \n - Quit(q)")
            user_input = input()
            if user_input in ['Q', 'q']:
                print("farewell")
                return
            elif user_input in ['1']:
                print("We're in Romanticism, a reflection of the more innovative and creative side of people.")
            elif user_input in ['2']:
                print("I'm Washington Irving, an American short story writer and essayist. I'm originally from New York, but I'm out here for a break from the city. ")
            elif user_input in ['3']:
                print("We're believers in Romanticism, an idealogy that focuses on the emotional and imaginitive side of people. We belive our ancesters were too boring with their"
                      "rationalistic ways, and always making decisions just because they made sense. The only real way to live is to be emotional and optimistic, so that you make "
                      "the decisions you want to, not the ones you think are more rational. We get plenty of new ideas and perspectives from immigrants, and believe that the mingling of"
                      "races is beneficial to all. ")            
            elif user_input in ['4']:
                print("We viewed literature as an escape from reality. We belived in the importance of the imagination, and literature allows people to express that. We also viewed the "
                      "frontier as a supreme opportunity, as it gave people the ability to express their true selves. We view the world as mysterious, and believe that it is impossible to know"
                      "everything. We believe that everyone deserves equal opportunity and education, which can come from literature. ")
            else:
                print("Invalid choice!")      
                
                
    def dialogueTwain(self):
        print("Well how do you do")
        
        while True:
            print(" - Where are we? (1)\n - Who are you? (2)\n - What do you believe in? (3)\n - Why was this way of thinking created? (4) \n - Quit(q)")
            user_input = input()
            if user_input in ['Q', 'q']:
                print("farewell")
                return
            elif user_input in ['1']:
                print("This is realism, an accurate reflection of reality. We believe in pragmatism, and that the morality of the individual is essential. The equality commonly found in "
                      "democratic systems is also incredible important, along with human's ability to control our own destinies. ")
            elif user_input in ['2']:
                print("I'm Mark Twain, but my real name is Samuel Clemens. I'm an American writer and publisher, most famous for some of my novels, which include the Adventures of Huckleberry Finn and the "
                      "Adventures of Tom Sawyer. ")
            elif user_input in ['3']:
                print("We believe that everything should be shown as it is. We got to this way of thinking because our ancestors did everything based on emotion, instead of logical "
                      "thought. We focus on different things than our ancestors, such as the plight of the new urban poor population and people's ordinary lives. We think that portraying"
                      "the human struggle in print is essential to life. Each person should have an equal voice, and should be independent to make their own decisions. ")            
            elif user_input in ['4']:
                print("We started thinking this way as the result of many failed revolutions in the 1840s. We thought that showing worldwide events and conditions in a harsh light would "
                      "help humans understand more about the world. ")
            else:
                print("Invalid choice!")        
        
    def dialogueFitzgerald(self):
        print("Well how do you do")
        
        while True:
            print(" - Where is this? (1)\n - What do you do? (2)\n - What are your beliefs? (3)\n - Why was this way of thinking created? (4) \n - Quit(q)")
            user_input = input()
            if user_input in ['Q', 'q']:
                print("Farewell, old sport")
                return
            elif user_input in ['1']:
                print("This is West egg, or rather, the western part of Long Island in New York. New York was the center of the Jazz age, which is something I took a big part in. ")
            elif user_input in ['2']:
                print("I'm a writer. I've written books such as The Great Gatsby, which wasn't really recognized in my time but became widely regarded as one of the bests works of "
                      "American literature after my death. ")
            elif user_input in ['3']:
                print("Disillusionment is an important part of life, as well as the importance of the individual. Modernists feel an anxiety regarding the past, and reflect ideas of "
                      "the breakdown of cultural norms as well as collectivism vs individualism in texts. ")            
            elif user_input in ['4']:
                print("Modernism was formed as a reaction to cultural relativism, as we believe that there should be only one reality. Past generations believed that people made their own "
                      "meaning in the world, but we believe that there is a single, objective reality that encompasses all humans. ")
            else:
                print("I'm not sure what you said, old sport")          