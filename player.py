import items
import world


class Player:
    def __init__(self):
        self.inventory = [items.Rock(),
                          items.Dagger(),
                          items.CrustyBread()]
        self.x = world.start_tile_location[0]      ###THIS SHIT IS CAUSING SOME FUCKING PROBLEMS FIX IT DUMBASS
        self.y = world.start_tile_location[1]       #so, it's a tuple. The numbers are indicies, and somehow it's reading it as a null
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