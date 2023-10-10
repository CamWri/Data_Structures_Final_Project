attribute_explanation = {
    "athleticism": "Athleticism accounts for your physical characteristics of your species. The more points you put in, the more physically gifted your species is.",
    "intelligence" : "Intelligence accounts for how smart your species is with the ability to innovate, come up with new ideas, and learn and use old ideas. The more points you put in, the more brilliant and quick-witted your species is. Don't be too smart for your own good.",
    "communication" : "Communication accounts for how coherient your species is with communication and their ability to communicate their ideas effectivly. The more points you put in, the more persuasive and stronger communication your species has.",
    "resilience" : "Resilience accounts for how adaptibale and resistant your species is. The more points you put in, the more you can survive and adapt to new situations and harsh enviorments.",
    "population" : "Population accounts for how many of your species exist on this planet. The more points you put in, the more your species reproduces and the higher the initial population. Hope you have the resources",
    "health" : "This is the amount of health you and your species have. The more you put in, the more health you have when dealing with enemies and eviormental struggles.",
    "reputation": "Reputation accounts for how your species is viewed. The more points you put in, the more other species are willing to help or hurt you, depending on the other species."
    }



class character():
    def __init__(self, name, athleticism, intelligence, communication, resilience, population, health, reputation):
        self.name = name
        self.athleticism = athleticism
        self.intelligence = intelligence
        self.communication = communication
        self.resilience = resilience
        self.population = population
        self.health = health
        self.reputation = reputation

    def establish_attributes(self, attribute):

        attribute_value = -1

        while (attribute_value <= -1 or attribute_value > 10):
            try:
                attribute_value = int(input(f'Please input the {attribute} of your species: '))
                if attribute_value == 0:
                    print('\t' + attribute_explanation[attribute] + '\n')
                    attribute_value = int(input(f'Please input the {attribute} of your species: '))
            except ValueError:
                print("Please only input numbers when inputing your attributes\n")
                attribute_value = -1

        return attribute_value

    def species_sheet(self, character, char_name):
        print(f'Character Name: {char_name}')
        print(f'Athleticism: {character.athleticism}')
        print(f'Intelligence: {character.intelligence}')
        print(f'Communication: {character.communication}')
        print(f'Resilience: {character.resilience}')
        print(f'Population: {character.population}')
        print(f'Health: {character.health}')
        print(f'Reputation: {character.reputation}')

    def get_attributes_asList(self):
        list = []
        list.append(self.reputation)
        list.append(self.population)
        list.append(self.resilience)
        list.append(self.intelligence)
        list.append(self.communication)
        list.append(self.health)
        list.append(self.athleticism)
        return list

    def establish_dialouge_options(self):
        pass



