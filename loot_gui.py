from hover_text import *

class LOOT_GUI:
    def __init__(self, loot_interface, character, enemy_list):
        self.loot_interface = loot_interface

        self.button_frame = Frame(self.loot_interface)

        self.exit_commit_button = Button(self.button_frame, text="Exit", command=lambda: self.loot_interface.destroy())
        self.exit_commit_button.pack(side=RIGHT)


        self.eqiup_item_button = Button(self.button_frame, text="Loot Checked Items", command=lambda: self.loot(character))
        self.eqiup_item_button.pack(side=LEFT)

        self.button_frame.pack(side=BOTTOM)

        self.checkbuttonvalue_list = []
        self.item_list = []
        self.enemy_list = []

        for enemy in enemy_list:
            self.enemy_frame = Frame(self.loot_interface)
            self.enemy_label = Label(self.enemy_frame, text = f"{enemy.name}")
            self.enemy_label.pack(side=TOP)
            self.checkbutton_list = []
            for item in enemy.inventory.items:
                check_button = IntVar()
                item_check_button = Checkbutton(self.enemy_frame, text = f"{item.name}", variable = check_button, onvalue = 1, offvalue=0, width = len(item.name) + 2)
                CreateToolTip(item_check_button, text=item.examine())
                self.checkbutton_list.append(item_check_button)
                self.checkbuttonvalue_list.append(check_button)
                self.item_list.append(item)
                item_check_button.pack(side=BOTTOM)
            self.enemy_list.append(self.checkbutton_list)
            self.enemy_frame.pack(side=LEFT, anchor="w", padx = 10, pady=10)

    def loot(self, character):
        length = 0
        item_list_num = 0
        for item_list in self.enemy_list:
            for item in item_list:
                if self.checkbuttonvalue_list[length].get() == 1:
                    character.inventory.items.append(self.item_list[length])
                    self.enemy_list[item_list_num][item_list.index(item)].config(state=DISABLED)
                    self.checkbuttonvalue_list[length].set(0)
                length += 1
            item_list_num += 1

