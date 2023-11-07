from hover_text import *
class Combat_GUI:
    def __init__(self, combat_interface, character, enemy_list):
        self.combat_interface = combat_interface

        self.frame_allCharacters = Frame(self.combat_interface)

        self.frame_characters = Frame(self.frame_allCharacters)

        self.player_label = self.display_char(self.frame_characters, character)
        CreateToolTip(self.player_label, text=f"Health: {character.health}")


        self.frame_characters.pack(side=TOP)

        self.attack_commit_button = Button(combat_interface, text="Attack", command=lambda: self.attack(character, enemy_list))
        self.attack_commit_button.pack(side=BOTTOM, pady=5)

        self.frame_users_choice = Frame(combat_interface)

        self.frame_enemies = Frame(self.frame_allCharacters)

        self.frame_target_enemy = Frame(self.frame_users_choice)
        self.label_enemy = Label(self.frame_target_enemy, text="Enemies to Target")
        self.label_enemy.pack(side=TOP)

        self.radio_enemy_set = IntVar()
        self.radio_enemy_set.set(0)

        self.enemy_total = 0
        self.total_health = 0
        self.enemy_label_list = []
        self.radio_enemy_label_list = []


        for enemy in enemy_list:
            self.enemy_total += 1
            self.frame_single_enemy = Frame(self.frame_enemies)
            self.enemy_number_label = Label(self.frame_single_enemy, text=f"Enemy {self.enemy_total}:")
            self.enemy_number_label.pack(side=LEFT)
            self.enemy_label = self.display_char(self.frame_single_enemy, enemy)
            weakness = ", ".join(enemy.weakness)
            CreateToolTip(self.enemy_label, text=f"Health {enemy.health}\nDistance: {enemy.distance_from_player}\nWeakness: {weakness}")
            self.enemy_label_list.append(self.enemy_label)
            self.frame_single_enemy.pack(side=TOP)

            self.enemy_radio_button = Radiobutton(self.frame_target_enemy, text=f"{enemy.name}", variable=self.radio_enemy_set, value=self.enemy_total, width=20)
            self.enemy_radio_button.pack(side=TOP)
            CreateToolTip(self.enemy_radio_button, text=f"Health: {enemy.health}\nDistance: {enemy.distance_from_player}\nWeakness: {weakness}")
            self.radio_enemy_label_list.append(self.enemy_radio_button)
            self.total_health += enemy.health

        self.frame_enemies.pack(side=TOP)
        self.frame_target_enemy.pack(side=RIGHT, anchor="e", padx=40)

        self.frame_allCharacters.pack(side=TOP)

        self.frame_attacks = Frame(self.frame_users_choice)

        self.attacks_label = Label(self.frame_attacks, width=15, text="Possible Attacks")
        self.attacks_label.pack(side=TOP)

        self.radio_attack_set = IntVar()
        self.radio_attack_set.set(0)

        self.button_value_attack = 0

        self.button_value_attack += 1
        self.weapon1_radio_button = Radiobutton(self.frame_attacks, text=f"{character.weapon1.name}", variable=self.radio_attack_set, value= 1, width=20)
        self.weapon1_radio_button.pack(side=TOP)
        CreateToolTip(self.weapon1_radio_button,text=f"{character.weapon1.examine()}")

        if character.weapon2.type_of_damage == "magical":
            self.button_value_attack = 3
            for spell_index in range(len(character.weapon2.spells)):
                self.spell_radio_button = Radiobutton(self.frame_attacks, text=f"Cast {character.weapon2.spells[spell_index].name}", variable= self.radio_attack_set, value= self.button_value_attack, width=20)
                self.spell_radio_button.pack(side=TOP)
                self.button_value_attack += 1
                CreateToolTip(self.spell_radio_button, text=f"{character.weapon2.spells[spell_index].examine()}")

        else:
            self.weapon2_radio_button = Radiobutton(self.frame_attacks, text=f"{character.weapon2.name}", variable= self.radio_attack_set, value= 2, width=20)
            self.weapon2_radio_button.pack(side=TOP)
            CreateToolTip(self.weapon2_radio_button, text=f"{character.weapon2.examine()}")

        self.frame_attacks.pack(side=LEFT, anchor="w", padx=40)

        self.frame_users_choice.pack(side=BOTTOM)

    def attack(self, character, enemy_list):
        if self.radio_attack_set.get() == 0 or self.radio_enemy_set.get() == 0:
            self.radio_attack_set.set(1)
            self.radio_enemy_set.set(1)
        elif self.total_health == 0:
            pass
        else:
            character_attack_index = self.radio_attack_set.get()
            enemy_attacked_index = self.radio_enemy_set.get() - 1

            weakness = ", ".join(enemy_list[enemy_attacked_index].weakness)

            #rework attack for spells, swords etc in their respective classes, add healing and defensive spells
            if character_attack_index == 1:
                enemy_list[enemy_attacked_index].health = enemy_list[enemy_attacked_index].health - character.weapon1.damage
                if enemy_list[enemy_attacked_index].health < 0:
                    enemy_list[enemy_attacked_index].health = 0
                CreateToolTip(self.enemy_label_list[enemy_attacked_index], text=f"Health: {enemy_list[enemy_attacked_index].health}\nDistance: {enemy_list[enemy_attacked_index].distance_from_player}\nWeakness: {weakness}")
                CreateToolTip(self.radio_enemy_label_list[enemy_attacked_index], text=f"Health: {enemy_list[enemy_attacked_index].health}\nDistance: {enemy_list[enemy_attacked_index].distance_from_player}\nWeakness: {weakness}")
                self.total_health -= character.weapon1.damage
                if self.total_health < 0:
                    self.total_health = 0
            elif character_attack_index == 2:
                enemy_list[enemy_attacked_index].health = enemy_list[enemy_attacked_index].health - character.weapon2.damage
                if enemy_list[enemy_attacked_index].health < 0:
                    enemy_list[enemy_attacked_index].health = 0
                CreateToolTip(self.enemy_label_list[enemy_attacked_index], text=f"Health: {enemy_list[enemy_attacked_index].health}\nDistance: {enemy_list[enemy_attacked_index].distance_from_player}\nWeakness: {weakness}")
                CreateToolTip(self.radio_enemy_label_list[enemy_attacked_index], text=f"Health: {enemy_list[enemy_attacked_index].health}\nDistance: {enemy_list[enemy_attacked_index].distance_from_player}\nWeakness: {weakness}")
                self.total_health -= character.weapon2.damage
                if self.total_health < 0:
                    self.total_health = 0
            else:
                enemy_list[enemy_attacked_index].health = enemy_list[enemy_attacked_index].health - character.weapon2.spells[character_attack_index-3]
                if enemy_list[enemy_attacked_index].health < 0:
                    enemy_list[enemy_attacked_index].health = 0
                CreateToolTip(self.enemy_label_list[enemy_attacked_index], text=f"Health: {enemy_list[enemy_attacked_index].health}\nDistance: {enemy_list[enemy_attacked_index].distance_from_player}\nWeakness: {weakness}")
                CreateToolTip(self.radio_enemy_label_list[enemy_attacked_index], text=f"Health: {enemy_list[enemy_attacked_index].health}\nDistance: {enemy_list[enemy_attacked_index].distance_from_player}\nWeakness: {weakness}")
                self.total_health -= character.weapon2.spells[character_attack_index-3]
                if self.total_health < 0:
                    self.total_health = 0


            if self.total_health == 0:
                self.label_final_text = Label(self.combat_interface, text = "You Have Won the Fight")
                self.label_final_text.pack(side= BOTTOM, pady = 20)
                self.combat_interface.after(3000, lambda: self.label_final_text.destroy())
                self.combat_interface.after(3000, lambda: self.frame_allCharacters.destroy())
                self.combat_interface.after(3000, lambda: self.frame_users_choice.destroy())
                self.combat_interface.after(3000, lambda: self.frame_users_choice.destroy())
                self.combat_interface.after(3000, lambda: self.attack_commit_button.destroy())
                self.loot(character, enemy_list)
            elif character.health == 0:
                self.label_final_text = Label(self.combat_interface, text = "You Have Lost the Fight, Exit When Ready On the Top Left")
                self.label_final_text.pack(side=BOTTOM, pady=20)
                self.combat_interface.overrideredirect(False)


            self.radio_attack_set.set(0)
            self.radio_enemy_set.set(0)

        # get the index of the enemy from the variable enemies, then use create tool tip

    def display_char(self, window, character):
        self.character_label = Label(window, text=f"{character.name}")
        self.character_label.pack(side=LEFT)
        self.character_weapon_label1 = Label(window, text=f"{character.weapon1.name}")
        self.character_weapon_label1.pack(side=LEFT)
        CreateToolTip(self.character_weapon_label1, text=character.weapon1.examine())
        self.character_weapon_labe2 = Label(window, text=f"{character.weapon2.name}")
        self.character_weapon_labe2.pack(side=LEFT)
        CreateToolTip(self.character_weapon_labe2, text=character.weapon2.examine())
        self.character_armor = Label(window, text=f"{character.armor.name}")
        self.character_armor.pack(side=LEFT)
        CreateToolTip(self.character_armor, text=character.armor.examine())
        return self.character_label

    def loot(self, character, enemy_list):
        pass




