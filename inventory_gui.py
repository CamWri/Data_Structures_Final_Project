from hover_text import *

class Inventory_GUI:
    def __init__(self, inventory_interface, character):
        self.inventory_interface = inventory_interface

        label_name = Label(inventory_interface, text=f'{character.name}\'s Inventory')
        label_name.pack()

        self.frame_top = Frame(inventory_interface)

        frame_weapon = Frame(self.frame_top)

        label_gold = Label(frame_weapon, text=f'Gold: {character.inventory.gold}')
        label_gold.pack()

        self.label_weapon1 = Label(frame_weapon, text=f"Weapon 1: {character.weapon1.name}")
        self.label_weapon1.pack()
        CreateToolTip(self.label_weapon1, text=f"{character.weapon1.examine()}")

        self.label_weapon2 = Label(frame_weapon, text=f"Weapon 2: {character.weapon2.name}")
        self.label_weapon2.pack()
        CreateToolTip(self.label_weapon2, text=f"{character.weapon2.examine()}")

        self.label_armor = Label(frame_weapon, text=f"Armor: {character.armor.name}")
        self.label_armor.pack()
        CreateToolTip(self.label_armor, text=f"{character.armor.examine()}")

        frame_weapon.pack(side=LEFT, anchor="w", padx=30, pady=5)

        if character.weapon2.type_of_damage == "magical":
            self.frame_spells = Frame(self.frame_top)
            for spell in character.weapon2.spells:
                label = Label(self.frame_spells, text=f'{spell.name}')
                label.pack()
                CreateToolTip(label, text=f"{spell.examine()}")
            self.frame_spells.pack(side=RIGHT, anchor="e", padx=70, pady=5)

        self.frame_top.pack(side=TOP, anchor="n")

        frame_inventory = Frame(inventory_interface)

        #Make a button on the bottom that when click calls equip_item function
        change_item_button = Button(inventory_interface, text = "Equip Clicked Item", command= lambda: self.equip_item(character))
        change_item_button.pack(side=BOTTOM, pady = 10)

        self.radio_item_set = IntVar()
        self.radio_item_set.set(-1)
        self.radio_button_list = []
        if len(character.inventory.items) != 0:
            for item_index in range(len(character.inventory.items)):
                if item_index % 9 == 0:
                    self.temp_frame = Frame(frame_inventory, highlightthickness=2, highlightcolor="blue")
                radiobutton = Radiobutton(self.temp_frame, text=f'{character.inventory.items[item_index].name}', width=len(character.inventory.items[item_index].name), variable= self.radio_item_set, value = item_index)
                radiobutton.pack(padx = 5)
                CreateToolTip(radiobutton, text=f"{character.inventory.items[item_index].examine()}")
                self.radio_button_list.append(radiobutton)
                if item_index % 9 == 0:
                    self.temp_frame.pack(side = LEFT)
            else:
                self.temp_frame.pack(side=LEFT)
        else:
            empty_inventory_label = Label(inventory_interface, text = "You have not other items in your inventory")
            empty_inventory_label.pack(side=TOP, pady= 5)

        frame_inventory.pack(side = LEFT, pady= 5)

    def equip_item(self, character):
        item_to_equip_index = self.radio_item_set.get()
        item = character.inventory.items[item_to_equip_index]

        if item.type == "weapon2":
            if character.weapon2.name == "Kick":
                self.radio_button_list[item_to_equip_index].destroy()
            else:
                self.radio_button_list[item_to_equip_index].config(text = f"{character.weapon2.name}", width = len(character.weapon2.name))
                CreateToolTip(self.radio_button_list[item_to_equip_index], text=f"{character.weapon2.examine()}")
            if character.weapon2.type_of_damage == "magical":
                self.frame_spells.destroy()
            if item.type_of_damage == "magical":
                self.frame_spells = Frame(self.frame_top)
                for spell in item.spells:
                    label = Label(self.frame_spells, text=f'{spell.name}')
                    label.pack()
                    CreateToolTip(label, text=f"{spell.examine()}")
                self.frame_spells.pack(side=RIGHT, anchor="e", padx=70, pady=5)
            character.inventory.items[item_to_equip_index] = character.weapon2
            character.weapon2 = item
            self.label_weapon2.config(text=f"Weapon 2: {item.name}")
            CreateToolTip(self.label_weapon2, text=f"{item.examine()}")
        elif item.type == "weapon1":
            if character.weapon1.name == "Punch":
                self.radio_button_list[item_to_equip_index].destroy()
            else:
                self.radio_button_list[item_to_equip_index].config(text=f"{character.weapon1.name}", width=len(character.weapon2.name))
                CreateToolTip(self.radio_button_list[item_to_equip_index], text=f"{character.weapon1.examine()}")
            character.inventory.items[item_to_equip_index] = character.weapon1
            character.weapon1 = item
            self.label_weapon1.config(text=f"Weapon 1: {item.name}")
            CreateToolTip(self.label_weapon1, text=f"{item.examine()}")
        elif item.type == "armor":
            self.radio_button_list[item_to_equip_index].config(text=f"{character.armor.name}",width=len(character.armor.name))
            CreateToolTip(self.radio_button_list[item_to_equip_index], text=f"{character.armor.examine()}")
            character.inventory.items[item_to_equip_index] = character.armor
            character.armor = item
            self.label_armor.config(text=f"Armor: {item.name}")
            CreateToolTip(self.label_armor, text=f"{item.examine()}")

