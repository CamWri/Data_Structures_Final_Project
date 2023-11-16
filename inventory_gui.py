from hover_text import *

class Inventory_GUI:
    def __init__(self, inventory_interface, character):
        self.inventory_interface = inventory_interface

        label_name = Label(inventory_interface, text=f'{character.name}\'s Inventory')
        label_name.pack()

        frame_top = Frame(inventory_interface)

        frame_weapon = Frame(frame_top)

        label_gold = Label(frame_weapon, text=f'Gold: {character.inventory.gold}')
        label_gold.pack()

        label_weapon1 = Label(frame_weapon, text=f"Weapon 1: {character.weapon1.name}")
        label_weapon1.pack()
        CreateToolTip(label_weapon1, text=f"{character.weapon1.examine()}")

        label_weapon2 = Label(frame_weapon, text=f"Weapon 2: {character.weapon2.name}")
        label_weapon2.pack()
        CreateToolTip(label_weapon2, text=f"{character.weapon2.examine()}")

        label_armor = Label(frame_weapon, text=f"Armor: {character.armor.name}")
        label_armor.pack()
        CreateToolTip(label_armor, text=f"{character.armor.examine()}")

        frame_weapon.pack(side=LEFT, anchor="w", padx=30, pady=5)

        if character.weapon2.type != "Hand Attacks":
            frame_spells = Frame(frame_top)
            for spell in character.weapon2.spells:
                label = Label(frame_spells, text=f'{spell.name}')
                label.pack()
                CreateToolTip(label, text=f"{spell.examine()}")
            frame_spells.pack(side=RIGHT, anchor="e", padx=70, pady=5)

        frame_top.pack(side=TOP, anchor="n")

        frame_inventory = Frame(inventory_interface)




        self.radio_item_set = IntVar()
        self.radio_item_set.set(-1)

        for item_index in range(len(character.inventory.items)):
            if item_index % 9 == 0:
                temp_frame = Frame(frame_inventory, highlightthickness=2, highlightcolor="blue")
            button = Radiobutton(temp_frame, text=f'{character.inventory.items[item_index].name}', width=10, command = lambda:self.equip_item(character.inventory.items[item_index]), variable= self.radio_item_set, value = item_index )
            button.pack(padx = 5)
            CreateToolTip(button, text=f"{character.inventory.items[item_index].examine()}")
            if item_index % 9 == 0:
                temp_frame.pack(side = LEFT)
        if item_index % 9 != 0 and len(character.inventory.items) != 0:
            temp_frame.pack(side=LEFT)

        frame_inventory.pack(side = LEFT, pady= 5)

    def equip_item(self, item):
        pass