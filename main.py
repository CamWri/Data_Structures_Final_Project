from event_tree_ofAny import *

def create_char():
    player_character_name = input("Enter your character name: ").rstrip().capitalize()
    player_char = character(player_character_name, 0, 0, 0, 0, 0, 0, 0)
    character_attributes(player_char)
    print('\n\n\n')
    player_char.species_sheet(player_char, player_character_name)
    print('\n')
    return player_char

def attribute(species, attriubte, number, points_left):
    print(f'Attribute {number} out of 7:\t', end = "")
    species.attriubte = species.establish_attributes(attriubte)
    points_left = points_left - species.attriubte
    print(f'\t\tPoints Remaining:{points_left}\n', end = "")

    return species.attriubte, points_left


def character_attributes(player_species):
    print("\nYou will have a total of 40 points over 7 categories going from 1 - 10. For any of these, press '0' for information on this attribute.")
    print("Your attributes are Athleticism, Intelligence, Communication, Resilience, Population, Health and Reputation")

    attributes_total = True

    while attributes_total:
        points_left = 40
        player_species.athleticism, points_left = attribute(player_species, "athleticism", 1, points_left)
        player_species.intelligence, points_left = attribute(player_species, "intelligence", 2, points_left)
        player_species.communication, points_left = attribute(player_species, "communication", 3, points_left)
        player_species.resilience, points_left = attribute(player_species, "resilience", 4, points_left)
        player_species.population, points_left = attribute(player_species, "population", 5, points_left)
        player_species.health, points_left = attribute(player_species, "health", 6, points_left)
        player_species.reputation, points_left = attribute(player_species, "reputation", 7, points_left)

        if points_left == 0:
            break
        else:
            print("\nPlease enter the attribute values that have a sum of 40 going from 1 - 10 where 0 is for information on the attribute")



def intro():
    #Introduction of how the governence shows up to take money for the protection of your townhome. You and your family are outside farming.
    #The collectors talk about a rumor of unkown disease that has been speading to the main city with no ideas of how it spreads
    #(There can be an action here where you get the money or someother person gets the money), this is where the tree starts
    #If you go, you grab the money then you hear a noise, and it is one of the gaurds spazzing out, continue on
    #if some other family member goes, you see the gaurd spazzing, and phoming from the mouth, continue on

    pass


def main():

    create_narration("With good in life, there also comes the evil."
            "So, even in the most prosperous of times, evil still exists. Sometimes it is just harder to see."
            "Evil lingers, grows, and evolves during prosperity, eventually overtaking the good."
            "Today is one of those times with a curse spreading all across the lands,  corrupting life itself."
            "The once living things are accursed with rage, anger, and vengeance with no mental power or free will."
            "Some say its an act of a higher deity, others say its from the mountains."
            "Some even say it was created by the living, but no one knows for sure."
            "Depending on your actions, you can be the savior of the lands, or lead the curse for domination."
            "So, with the fate of the lands in your hands, who will you be?",
                     "intro")


    players_character = create_char()




if __name__ == "__main__":
    main()