from event_tree_ofAny import *
from species import *
from combat_gui import *
from inventory_gui import *
from time import *
from tkinter import*

def play_intro():
    print(Fore.BLUE + "There has and will always be good and evil. During prosperity, evil lingers in the shadows of the good. Over time though, this evil unleashes on the world. Today is one of those times with a curse spreading all across the lands corrupting the soul itself. Depending on your actions, you can be the savior of the lands or lead the curse for domination. So with the fate of the lands in your hands, who will you be?" + Fore.RESET)
    player_character_name = input(Fore.RED + Style.BRIGHT + f"Enter your character name: " + Style.RESET_ALL).rstrip().capitalize()
    player_char = character(player_character_name, Inventory(10), health= 30)
    print(Fore.RED + Style.BRIGHT + f"Your characters health is {player_char.health}"+ Fore.RESET)
    return player_char

def update_inventory(character):
    inventory_interface = Tk()

    inventory_interface.geometry("500x350")

    inventory_interface.resizable(False, False)

    Inventory_GUI(inventory_interface, character)

    inventory_interface.mainloop()


def inventory_check(character, node, inventory_node):
    update_inventory(character)
    node.children.remove(inventory_node)
    for i in range(len(node.children)):
        print(f'Action {i}: {node.children[i].value}', end="\n")

    next_action_index = int(input(Fore.RED + Style.BRIGHT + "Enter the corresponding number for which one will you do: " + Fore.RESET))
    return next_action_index

def add_iteam(character, node):
    print()
    for i in node.loot:
        print(Fore.CYAN + f'You grabbed and added to your inventory a {i.name}' + Fore.GREEN)
        if i.type == "weapon1" and character.weapon1 is punch:
            print(Fore.MAGENTA + f"You automatically equip the {i.name} due to not having anything equipped" + Fore.RESET)
            character.weapon1 = i
        elif i.type == "weapon2" and character.weapon2 is kick:
            print(Fore.MAGENTA + f"You automatically equip the {i.name} due to not having anything equipped"+ Fore.RESET)
            character.weapon2 = i
        elif i.type == "armor" and character.armor is Clothes:
            print(Fore.MAGENTA + f"You automatically equip the {i.name} due to not having anything equipped" + Fore.RESET)
            character.armor = i
        else:
            character.inventory.items.append(i)
        print(Fore.RESET)

def next_node(node, character):
    if len(node.children) > 0:
        if len(node.enemies) == 0:
            inventory_node = Node("Inventory")
            node.add_child(inventory_node)
            if node.gold > 0:
                print(Fore.CYAN + f"\nYou grabbed and add to your inventory {node.gold} pieces of gold")
                character.inventory.gold += node.gold
                print(Fore.YELLOW + f"Now you have {character.inventory.gold} pieces of gold\n" + Fore.RESET)
            if node.loot is not None:
                add_iteam(character, node)
                update_inventory(character)
            print(Fore.BLUE + node.audio_file_text + Fore.RESET)
            for i in range(len(node.children)):
                print(f'Action {i}: {node.children[i].value}', end = "\n")

            next_action_index = int(input(Fore.RED + Style.BRIGHT + "Enter the corresponding number for which one will you do: " + Fore.RESET))
            if node.children[next_action_index].value == "Inventory":
                next_action_index = inventory_check(character, node, inventory_node)
            return node.children[next_action_index]
        else:
            print(Fore.BLUE + node.audio_file_text + Fore.RESET)
            sleep(3)

            combat(character, node.enemies)
            total_enemy_health = 0
            for enemy in node.enemies:
                total_enemy_health += enemy.health

            if character.health == 0:
                next_action_index = 1
                character.health = 30 + 5
            elif total_enemy_health == 0:
                next_action_index = 0
            else:
                next_action_index = 2

            return node.children[next_action_index]
    else:
        return None

def combat(character, enemy_list):
    combat_interface = Tk()

    combat_interface.geometry("500x400")

    combat_interface.resizable(False, False)

    Combat_GUI(combat_interface, character, enemy_list)

    combat_interface.mainloop()


def main():
    character = play_intro()
    node = node_1_1_1

    while True:
        node = next_node(node, character)
        if node is None:
            print("Done")
            break
if __name__ == "__main__":
    main()
