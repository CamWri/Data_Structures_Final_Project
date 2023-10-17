from event_tree_ofAny import *
from species import *


def play_intro():
    print(Fore.BLUE + "There has and will always be good and evil. During prosperity, evil lingers in the shadows of the good. Over time though, this evil unleashes on the world. Today is one of those times with a curse spreading all across the lands corrupting the soul itself. Depending on your actions, you can be the savior of the lands or lead the curse for domination. So with the fate of the lands in your hands, who will you be?" + Fore.RESET)
    #playsound.playsound(root.audio_file)
    player_character_name = input(Fore.RED + Style.BRIGHT + "Enter your character name: " + Style.RESET_ALL).rstrip().capitalize()
    player_char = character(player_character_name, Inventory(10))
    #playsound.playsound(node_intro_1_1_1.audio_file)
    return player_char

def next_node(node, player_char):
    if len(node.children_value) > 0:
        inventory_node = Node("Inventory")
        node.add_child(inventory_node)
        while True:
            print(Fore.BLUE + node.audio_file_text + Fore.RESET)
            for i in range(len(node.children_value)):
                print(f'Action {i}: {node.children_value[i]}', end = "\n")

            next_action_index = int(input(Fore.RED + Style.BRIGHT + "Enter the corresponding number for which one will you do: " + Fore.RESET))
            if node.children_value[next_action_index] == "Inventory":
                print(Fore.YELLOW + "Inventory:")
                print(f"\tGold: {player_char.inventory.gold}")
                for i in player_char.inventory.iteams:
                    print(f'{i.names}')
                else:
                    print("\tYou have no items in your inventory" + Fore.RESET)
                    print()
                node.children_value.remove("Inventory")
                node.children.remove(inventory_node)
            else:
                break
        return node.children[next_action_index]
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
        if node.loot is not None:
            for i in node.loot:
                character.inventory.iteams.append(i.name)
            print(Fore.GREEN + f'Updated Inventory:')
            for i in character.inventory.iteams:
                print(f'\tAdded to your inventory a {i}')
            print(Fore.RESET)
        if node.gold > 0:
            print(Fore.GREEN + f'Update to Gold:')
            print(f"\tYou grabbed {node.gold} pieces of gold")
            character.inventory.gold += node.gold
            print(f"\tNow you have {character.inventory.gold}" + Fore.RESET)

if __name__ == "__main__":
    main()