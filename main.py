from event_tree_ofAny import *
from species import *
from time import *


def play_intro():
    print(Fore.BLUE + "There has and will always be good and evil. During prosperity, evil lingers in the shadows of the good. Over time though, this evil unleashes on the world. Today is one of those times with a curse spreading all across the lands corrupting the soul itself. Depending on your actions, you can be the savior of the lands or lead the curse for domination. So with the fate of the lands in your hands, who will you be?" + Fore.RESET)
    #playsound.playsound(root.audio_file)
    player_character_name = input(Fore.RED + Style.BRIGHT + f"Enter your character name: " + Style.RESET_ALL).rstrip().capitalize()
    player_char = character(player_character_name, Inventory(10), health= 30)
    print(Fore.RED + Style.BRIGHT + f"Your characters health is {player_char.health}"+ Fore.RESET)
    #sleep(1.5)
    #playsound.playsound(node_intro_1_1_1.audio_file)
    return player_char

def inventory_check(character, node, inventory_node):
    print(Fore.YELLOW + "Inventory:")
    print(f"\tGold: {character.inventory.gold}")
    print(f"\tWeapon 1: {character.weapon1}")
    print(f"\tWeapon 2: {character.weapon2}")
    print(f"\tArmor: {character.armor}")
    for i in character.inventory.iteams:
        print(f'{i.names}')
    else:
        print("\tYou have no items in your inventory" + Fore.RESET)
        print()
    node.children_value.remove("Inventory")
    node.children.remove(inventory_node)

def add_iteam(character, node):
    for i in node.loot:
        character.inventory.iteams.append(i)
        print(Fore.CYAN + f'You grabbed and added to your inventory a {i.name}' + Fore.GREEN)
        inspect = input(f"Would you like to inspect {i.name}(Y/N):").lower().rstrip()
        if inspect == "y" or inspect == "yes":
            print(Fore.YELLOW)
            i.examine()
            print(Fore.GREEN)
        if i.type == "weapon1" or i.type == "weapon2" or i.type == "armor":
            equip = input(f"Would you like to equip {i.name}(Y/N):").lower().rstrip()
            if equip == "y" or equip =="yes":
                if i.type == "weapon1":
                    character.weapon1 = i
                elif i.type == "weapon2":
                    character.weapon2 = i
                elif i.type == "armor":
                    character.armor = i
            print(Fore.RESET)

def next_node(node, character):
    if len(node.children_value) > 0:
        inventory_node = Node("Inventory")
        node.add_child(inventory_node)
        while True:
            print(Fore.BLUE + node.audio_file_text + Fore.RESET)
            for i in range(len(node.children_value)):
                #sleep(1)
                print(f'Action {i}: {node.children_value[i]}', end = "\n")


            next_action_index = int(input(Fore.RED + Style.BRIGHT + "Enter the corresponding number for which one will you do: " + Fore.RESET))
            if node.children_value[next_action_index] == "Inventory":
                inventory_check(character, node, inventory_node)
            else:
                break
        return node.children[next_action_index]
    elif node.gold > 0:
        print(Fore.CYAN + f"\tYou grabbed and add to your inventory {node.gold} pieces of gold")
        character.inventory.gold += node.gold
        print(Fore.YELLOW + f"\tNow you have {character.inventory.gold}" + Fore.RESET)
    else:
        print("Done")
        return None

def main():
    character = play_intro()
    node  = node_intro_1_1_1

    while True:
        node = next_node(node, character)
        if node is None:
            break
        if node.loot is not None or node.gold > 0:
            add_iteam(character, node)

            #Go through each iteam recieved from the enviorment and compare it with existing iteam, ask if you want to equip it

if __name__ == "__main__":
    main()
