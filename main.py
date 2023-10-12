from event_tree_ofAny import *
from species import *
import assemblyai as aai

aai.settings.api_key = f"303f86dbeeec4bb9a444259da3a61a0d"


#Introduction of how the governence guards shows up to take money for the protection of your townhome. You and your family are outside farming.
#The collectors talk about a rumor of unkown disease that has been speading to the main city with no ideas of how it spreads.
#(There can be an action here where you get the money or someother person gets the money), this is where the tree starts
#If you go, you grab the money then you hear a noise, and it is one of the gaurds spazzing out, continue on
#if some other family member goes, you see the gaurd spazzing, and phoming from the mouth, continue on

def create_playable_char():
    player_character_name = input(Fore.RED + Style.BRIGHT + "Enter your character name: " + Style.RESET_ALL).rstrip().capitalize()
    #player_char = character(player_character_name, 0, 0, 0, 0, 0, 0, 0)
    #player_char.character_attributes(player_char)
    #print('\n\n\n')
    #player_char.species_sheet(player_char, player_character_name)
    #print('\n')
    #return player_char
    return player_character_name

def create_non_playable_char(name, list):
    player_char = character(name, list[0], list[1], list[2], list[3], list[4], list[5], list[6])
    return player_char


def play_intro():
    transcriber = aai.Transcriber()
    #print(Fore.BLUE + transcriber.transcribe(root.audio_file).text + Fore.RESET)
    print(Fore.BLUE + "There has and will always be good and evil. During prosperity, evil lingers in the shadows of the good. Over time though, this evil unleashes on the world. Today is one of those times with a curse spreading all across the lands corrupting the soul itself. Depending on your actions, you can be the savior of the lands or lead the curse for domination. So with the fate of the lands in your hands, who will you be?" + Fore.RESET)
    #playsound.playsound(root.audio_file)
    player_character = create_playable_char()
    print(Fore.BLUE + "Your story begins on a blistering hot summer day. You and your family are farming to sustain your destitute life. In the distance, you hear guards approaching and talking about the public\'s worries over the increasing derangement of people. When the guards get to your hut, they ask for the monthly commission for being part of the city. Everyone knows people in this area can't pay it and get other needs but if you don\'t, you will be ostracized. Your father tells you to go get the money." + Fore.RESET)
    #playsound.playsound(node_intro_1_1_1.audio_file)
    return player_character

def next_node(node):
    if len(node.children_value) > 0:
        for i in range(len(node.children_value)):
            print(f'Action {i}: {node.children_value[i]}', end = "\n")
        next_action_index = int(input(Fore.RED + Style.BRIGHT + "Enter the corresponding number for which one will you do: " + Fore.RESET))
        return node.children[next_action_index]
    else:
        print("Done")
        return None

def play(node):
    pass

def main():
    character = play_intro()
    node  = node_intro_1_1_1

    while True:
        node = next_node(node)
        if node is None:
            break
        print(Fore.BLUE + node.audio_file_text + Fore.RESET)

if __name__ == "__main__":
    main()