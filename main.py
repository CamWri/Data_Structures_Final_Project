from event_tree_ofAny import *
from species import *
from time import *
from hover_text import *


def play_intro():
    print(Fore.BLUE + "There has and will always be good and evil. During prosperity, evil lingers in the shadows of the good. Over time though, this evil unleashes on the world. Today is one of those times with a curse spreading all across the lands corrupting the soul itself. Depending on your actions, you can be the savior of the lands or lead the curse for domination. So with the fate of the lands in your hands, who will you be?" + Fore.RESET)
    player_character_name = input(Fore.RED + Style.BRIGHT + f"Enter your character name: " + Style.RESET_ALL).rstrip().capitalize()
    player_char = character(player_character_name, Inventory(10), health= 30)
    print(Fore.RED + Style.BRIGHT + f"Your characters health is {player_char.health}"+ Fore.RESET)
    return player_char

def update_inventory(character):
    root = Tk()

    root.geometry("500x350")

    from_equipment = Frame(root)

    label_name = Label(from_equipment, text=f'{character.name}\'s Inventory')
    label_name.pack()

    label_gold = Label(from_equipment, text=f'Gold: {character.inventory.gold}')
    label_gold.pack()

    frame_weapon = Frame(from_equipment)
    label_weapon1 = Label(frame_weapon, text=f"Weapon 1: {character.weapon1.name}")
    label_weapon1.pack()
    CreateToolTip(label_weapon1, text=f"{character.weapon1.examine()}")

    label_weapon2 = Label(frame_weapon, text=f"Weapon 2: {character.weapon2.name}")
    label_weapon2.pack()
    CreateToolTip(label_weapon2, text=f"{character.weapon2.examine()}")
    frame_weapon.pack()

    label_armor = Label(from_equipment, text=f"Armor: {character.armor.name}")
    label_armor.pack()
    CreateToolTip(label_armor, text=f"{character.armor.examine()}")

    from_equipment.pack(anchor="w", padx=10, pady=10)

    if character.weapon2.type_of_damage == "magical":
        frame_spells = Frame(root)
        for spell in character.weapon2.spells:
            label = Label(frame_spells, text=f'{spell.name}')
            label.pack()
            CreateToolTip(label, text=f"{spell.examine()}")
        frame_spells.pack(anchor="e", padx=10, pady=10)

    frame_inventory = Frame(root)

    for item_index in range(len(character.inventory.items)):
        label = Label(frame_inventory, text=f'{character.inventory.items[item_index].name}')
        label.pack()
        CreateToolTip(label, text=f"{character.inventory.items[item_index].examine()}")
        if character.inventory.items[item_index].type == "weapon2":
            for spell in character.inventory.items[item_index].spells:
                label = Label(frame_inventory, text=f'{spell.name} at index {item_index}')
                label.pack()
                CreateToolTip(label, text=f"{spell.examine()}")

    frame_inventory.pack(side = LEFT)

    frame_change_equipment = Frame(root)

    label_equip_item = Label(frame_change_equipment, text = "Input the index of the item you want to equip", font=("Helvetic bold", 10))
    label_equip_item.pack(side = LEFT)

    input_equip_item = Entry(frame_change_equipment, width = 10)
    input_equip_item.pack(side = RIGHT, pady=5)

    frame_change_equipment.pack(side= BOTTOM, padx= 50)
    root.mainloop()


def inventory_check(character, node, inventory_node):
    update_inventory(character)
    node.children.remove(inventory_node)
    print(Fore.BLUE + node.audio_file_text + Fore.RESET)

    for i in range(len(node.children)):
        print(f'Action {i}: {node.children[i].value}', end="\n")

    next_action_index = int(input(Fore.RED + Style.BRIGHT + "Enter the corresponding number for which one will you do: " + Fore.RESET))
    return next_action_index

def add_iteam(character, node):
    print()
    for i in node.loot:
        print(Fore.CYAN + f'You grabbed and added to your inventory a {i.name}' + Fore.GREEN)
        if i.type == "weapon1" and character.weapon1 is fist:
            print(Fore.MAGENTA + f"You automatically equip the {i.name} due to not having anything equipped" + Fore.RESET)
            character.weapon1 = i
        elif i.type == "weapon2" and character.weapon2 is fist:
            print(Fore.MAGENTA + f"You automatically equip the {i.name} due to not having anything equipped"+ Fore.RESET)
            character.weapon2 = i
        elif i.type == "armor" and character.armor is Clothes:
            print(Fore.MAGENTA + f"You automatically equip the {i.name} due to not having anything equipped" + Fore.RESET)
            character.armor = i
        else:
            character.inventory.items.append(i)
        print(Fore.RESET)
        update_inventory(character)

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
            print(Fore.BLUE + node.audio_file_text + Fore.RESET)
            for i in range(len(node.children)):
                print(f'Action {i}: {node.children[i].value}', end = "\n")
                #sleep(1)

            next_action_index = int(input(Fore.RED + Style.BRIGHT + "Enter the corresponding number for which one will you do: " + Fore.RESET))
            if node.children[next_action_index].value == "Inventory":
                next_action_index = inventory_check(character, node, inventory_node)
            return node.children[next_action_index]
        else:
            print("Fight sequence")
            #for the next node, node.children[0] if you beat the guard, index node.children[1] if you loose to the guard
            next_action_index = combat(character, node.enemies)
            next_node = node.children[next_action_index]

            print(Fore.BLUE + next_node.audio_file_text + Fore.RESET)
            for i in range(len(next_node.children)):
                print(f'Action {i}: {next_node.children[i].value}', end="\n")
            next_action_index = int(input(Fore.RED + Style.BRIGHT + "Enter the corresponding number for which one will you do: " + Fore.RESET))
            return next_node.children[next_action_index]
    else:
        print("Done")
        return None

def combat(player, enemey):
    print("-------Battle-------")
    combined_enemey_health = 0
    for i in enemey:
        combined_enemey_health += i.health
        i.char_sheet()

    turn = 1
    while True:
        
        if player.health == 0:
            return 1
        elif combined_enemey_health == 0:
            return 0




def main():
    character = play_intro()
    node  = node_1_1_1

    while True:
        node = next_node(node, character)
        if node is None:
            break
if __name__ == "__main__":
    main()
