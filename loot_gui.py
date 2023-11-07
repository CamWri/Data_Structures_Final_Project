from hover_text import *

class LOOT_GUI:
    def __init__(self, loot_interface, character, enemy_list):
        self.loot_interface = loot_interface

        self.eqiup_item_button = Button(self.loot_interface, text="Equip Checked Items") #command=lambda: self.attack(character, enemy_list)
        self.eqiup_item_button.pack(side=BOTTOM)

        self.item_value = 0

        self.checkbutton_list = []

        for enemy in enemy_list:
            self.enemy_frame = Frame(self.loot_interface)
            self.enemy_label = Label(self.enemy_frame, text = f"{enemy.name}")
            self.enemy_label.pack(side=LEFT)
            self.enemy_inventory_frame = Frame(self.enemy_frame)
            self.gold_value = IntVar()
            self.gold_check_button = Checkbutton(self.enemy_inventory_frame, text=f"{enemy.inventory.gold} gold", variable=self.gold_value ,onvalue=1, offvalue=0, width= 8)
            self.checkbutton_list.append(self.gold_check_button)
            self.gold_check_button.pack()
            for item in enemy.inventory.items:
                check_button = IntVar()
                item_check_button = Checkbutton(self.enemy_inventory_frame, text = f"{item.name}", variable = check_button, onvalue = 1, offvalue=0, width = len(item.name) + 2)
                self.checkbutton_list.append(item_check_button)
                item_check_button.pack()
            self.enemy_inventory_frame.pack(pady=10)
            self.enemy_frame.pack(side=TOP)

