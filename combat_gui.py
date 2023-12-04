from loot_gui import *
from time import *

class Combat_GUI:
    def __init__(self, combat_interface, character, enemy_list):
        self.combat_interface = combat_interface

        self.frame_allCharacters = Frame(self.combat_interface)

        self.frame_characters = Frame(self.frame_allCharacters)

        self.player_label = self.display_char(self.frame_characters, character)
        CreateToolTip(self.player_label, text=f"Health: {character.examine()}")


        self.frame_characters.pack(side=TOP)

        self.frame_button = Frame(self.combat_interface)

        self.attack_commit_button = Button(self.frame_button, text="Do Actions", command=lambda: self.attack(character, enemy_list))
        self.attack_commit_button.pack(side=LEFT, anchor="e", padx = 10)

        self.exit_commit_button = Button(self.frame_button, text="Exit", command=lambda:  self.combat_interface.destroy())
        self.exit_commit_button.pack(side=RIGHT, anchor="w", padx = 10)

        self.frame_button.pack(side=BOTTOM, pady=5)

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
        self.enemy_frame = []
        self.enemy_attack_list = []

        self.total_health = 0

        self.enemy_attack_frame = Frame(self.combat_interface)

        self.character_attack_label = Label(self.enemy_attack_frame, text=f"")
        self.character_attack_label.pack(side=TOP)
        self.enemy_attack_list.append(self.character_attack_label)

        for enemy in enemy_list:
            self.enemy_total += 1
            self.frame_single_enemy = Frame(self.frame_enemies)
            self.enemy_number_label = Label(self.frame_single_enemy, text=f"Enemy {self.enemy_total}:")
            self.enemy_number_label.pack(side=LEFT)
            self.enemy_label = self.display_char(self.frame_single_enemy, enemy)
            CreateToolTip(self.enemy_label, text=f"{enemy.examine()}")
            self.enemy_label_list.append(self.enemy_label)
            self.frame_single_enemy.pack(side=TOP)

            self.total_health += enemy.health

            self.enemy_radio_button = Radiobutton(self.frame_target_enemy, text=f"{enemy.name}", variable=self.radio_enemy_set, value=self.enemy_total, width=len(enemy.name))
            self.enemy_radio_button.pack(side=TOP)
            CreateToolTip(self.enemy_radio_button, text=f"{enemy.examine()}")
            self.radio_enemy_label_list.append(self.enemy_radio_button)

            self.enemy_frame.append(self.frame_single_enemy)

            self.enemy_attack_label = Label(self.enemy_attack_frame, text = f"")
            self.enemy_attack_label.pack(side = TOP)
            self.enemy_attack_list.append(self.enemy_attack_label)

        self.frame_enemies.pack(side=TOP)
        self.frame_target_enemy.pack(side=RIGHT, anchor="e", padx=45)

        self.frame_allCharacters.pack(side=TOP)

        self.frame_attacks = Frame(self.frame_users_choice)

        self.attacks_label = Label(self.frame_attacks, width=17, text="Possible Attacks")
        self.attacks_label.pack(side=TOP)

        self.radio_attack_set = IntVar()
        self.radio_attack_set.set(0)

        self.button_value_attack = 0
        self.button_value_attack += 1
        self.weapon1_radio_button = Radiobutton(self.frame_attacks, text=f"{character.weapon1.name}", variable=self.radio_attack_set, value= 1, width=len(character.weapon1.name) + 4)
        self.weapon1_radio_button.pack(side=TOP)
        CreateToolTip(self.weapon1_radio_button,text=f"{character.weapon1.examine()}")

        if character.weapon2.type_of_damage == "magical":
            self.button_value_attack = 3
            for spell_index in range(len(character.weapon2.spells)):
                self.spell_radio_button = Radiobutton(self.frame_attacks, text=f"{character.weapon2.spells[spell_index].name}", variable= self.radio_attack_set, value= self.button_value_attack, width=len(character.weapon2.spells[spell_index].name) + 4)
                self.spell_radio_button.pack(side=TOP)
                self.button_value_attack += 1
                CreateToolTip(self.spell_radio_button, text=f"{character.weapon2.spells[spell_index].examine()}")
        elif character.weapon2.type_of_damage is None:
            pass
        else:
            self.button_value_attack = 2
            self.weapon2_radio_button = Radiobutton(self.frame_attacks, text=f"{character.weapon2.name}", variable= self.radio_attack_set, value= self.button_value_attack, width=len(character.weapon2.name) + 4)
            self.weapon2_radio_button.pack(side=TOP)
            CreateToolTip(self.weapon2_radio_button, text=f"{character.weapon2.examine()}")

        self.frame_attacks.pack(side=LEFT, anchor="w", padx = 45)

        self.frame_users_choice.pack(side=BOTTOM)

        self.movement_number = DoubleVar()

        self.movement_scale = Scale(self.combat_interface, variable = self.movement_number, from_ = -character.movement_distance, to = character.movement_distance, orient=HORIZONTAL, sliderlength= 20, width = 5)
        self.movement_scale.pack(side = BOTTOM)

        self.movement_label = Label(self.combat_interface, text = "Movement")
        self.movement_label.pack(side = BOTTOM)

        self.label_final_text = Label(self.combat_interface, text=f"You move first and then attack")
        self.label_final_text.pack(side=BOTTOM)

        self.enemy_attack_frame.pack(side = TOP, pady = 15)


    def attack(self, character, enemy_list):
        character_attack_index = self.radio_attack_set.get()
        enemy_attacked_index = self.radio_enemy_set.get() - 1

        self.label_final_text.config(text = "")

        self.move_forward = True

        for enemy in enemy_list:
            if enemy.distance_from_player > self.movement_number.get():
                enemy.distance_from_player -= self.movement_number.get()
            else:
                enemy.distance_from_player = 1
                self.move_forward = False

        if character_attack_index == 1:
            if character.weapon1.range >= enemy_list[enemy_attacked_index].distance_from_player:
                self.attack_enemy(enemy_attacked_index, enemy_list, character, character.weapon1)
                self.combat_interface.after(2000, lambda: self.enemy_attack(enemy_list, character))
            else:
                self.label_final_text.config(text= f"The enemy is out of range to attack with {character.weapon1.name}")
        elif character_attack_index == 2:
            if character.weapon2.range >= enemy_list[enemy_attacked_index].distance_from_player:
                self.attack_enemy(enemy_attacked_index, enemy_list, character, character.weapon2)
                self.combat_interface.after(2000, lambda: self.enemy_attack(enemy_list, character))
            self.label_final_text.config(text=f"The enemy is out of range to attack with {character.weapon2.name}")
        elif character_attack_index == 0:
            if self.move_forward:
                self.character_attack_label.config(text=f"You do not attack with any weapon but moved {self.movement_number.get()}")
            else:
                self.character_attack_label.config(text=f"You attempt to move forward but an enemy is in your way")

            self.combat_interface.after(2000, lambda: self.enemy_attack(enemy_list, character))
        else:
            self.attack_enemy(enemy_attacked_index, enemy_list, character, character.weapon2.spells[character_attack_index-3])
            self.combat_interface.after(2000, lambda: self.enemy_attack(enemy_list, character))

        CreateToolTip(self.enemy_label_list[enemy_attacked_index],text=f"{enemy_list[enemy_attacked_index].examine()}")
        CreateToolTip(self.radio_enemy_label_list[enemy_attacked_index],text=f"{enemy_list[enemy_attacked_index].examine()}")

        if enemy_list[enemy_attacked_index].health == 0:
            self.enemy_frame[enemy_attacked_index].destroy()
            self.radio_enemy_label_list[enemy_attacked_index].destroy()
            character.inventory.gold += enemy_list[enemy_attacked_index].inventory.gold

        if self.total_health == 0:
            self.label_final_text.config(text="You Have Won the Fight")
            self.label_final_text.pack(side= BOTTOM, pady = 20)
            self.combat_interface.after(2000, lambda: self.label_final_text.destroy())
            self.combat_interface.after(1, lambda: self.frame_allCharacters.destroy())
            self.combat_interface.after(1, lambda: self.frame_users_choice.destroy())
            self.combat_interface.after(1, lambda: self.attack_commit_button.destroy())
            self.combat_interface.after(1, lambda: self.exit_commit_button.destroy())
            self.combat_interface.after(1, lambda: self.enemy_attack_frame.destroy())
            self.combat_interface.after(1, lambda: self.movement_scale.destroy())
            self.combat_interface.after(1, lambda: self.movement_label.destroy())
            self.combat_interface.after(2050, lambda: LOOT_GUI(self.combat_interface, character, enemy_list))
        elif character.health == 0:
            self.label_final_text.config(text="You Have Lost the Fight")
            self.label_final_text.pack(side=BOTTOM, pady=20)
            self.combat_interface.after(3000, lambda: self.combat_interface.destroy())

        self.radio_attack_set.set(0)
        self.radio_enemy_set.set(0)
        self.movement_number.set(0)


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

    def attack_enemy(self, enemy_attacked_index, enemy_list, character, weapon):
        damage = weapon.damage - (enemy_list[enemy_attacked_index].armor.armor_value * 0.5)

        if weapon.elemental in enemy_list[enemy_attacked_index].weakness:
            damage += (weapon.elemental_damage * 0.5)
        else:
            damage += weapon.elemental_damage

        if weapon.elemental in enemy_list[enemy_attacked_index].weakness:
            damage += (weapon.elemental_damage * 0.5)
        else:
            damage += weapon.elemental_damage


        if enemy_list[enemy_attacked_index].weapon2.type_of_damage is None:
            damage -= (enemy_list[enemy_attacked_index].weapon2.damage_mitigation * 0.5)

        if damage < 1:
            damage = 1

        enemy_list[enemy_attacked_index].health = enemy_list[enemy_attacked_index].health - damage
        if enemy_list[enemy_attacked_index].health < 0:
            self.total_health -= enemy_list[enemy_attacked_index].health + damage
            enemy_list[enemy_attacked_index].health = 0
        else:
            self.total_health -= damage

        CreateToolTip(self.enemy_label_list[enemy_attacked_index], text=f"{enemy_list[enemy_attacked_index].examine()}")
        CreateToolTip(self.radio_enemy_label_list[enemy_attacked_index],text=f"{enemy_list[enemy_attacked_index].examine()}")

        if self.move_forward:
            self.enemy_attack_list[0].config(text = f"{character.name} did {damage} damage to {enemy_list[enemy_attacked_index].name}. {enemy_list[enemy_attacked_index].name} has {enemy_list[enemy_attacked_index].health} health left.\nYou moved {self.movement_number.get()}")
        else:
            self.enemy_attack_list[0].config(text = f"{character.name} did {damage} damage to {enemy_list[enemy_attacked_index].name}. {enemy_list[enemy_attacked_index].name} has {enemy_list[enemy_attacked_index].health} health left.\nYou attempt to move forward but an enemey blocks you")



    def enemy_attack(self, enemy_list, character):
        for enemy in enemy_list:
            if enemy.health > 0:
                if enemy.weapon1.range >= enemy.distance_from_player:
                    enemy_damage = enemy.weapon1.damage - (character.armor.armor_value * 0.5)
                    if character.weapon2.type_of_damage is None:
                        enemy_damage -= (character.weapon2.damage_mitigation * 0.5)


                    if enemy.weapon1.type in character.weakness:
                        enemy_damage *= 1.5

                    if enemy_damage < 1:
                        enemy_damage = 1

                    character.health -= enemy_damage
                    self.enemy_attack_list[enemy_list.index(enemy) + 1].config(text=f"{enemy.name} did {enemy_damage} damage to {character.name} by using {enemy.weapon1.name}. \n{character.name} has {character.health} health left.")
                elif enemy.weapon2.range >= enemy.distance_from_player:
                    enemy_damage = enemy.weapon2.damage - (character.armor.armor_value * 0.5)
                    if character.weapon2.type_of_damage is None:
                        enemy_damage -= (character.weapon2.damage_mitigation * 0.5)

                    if enemy.weapon2.type in character.weakness:
                        enemy_damage *= 1.5

                    if enemy_damage < 1:
                        enemy_damage = 1

                    character.health -= enemy_damage
                    self.enemy_attack_list[enemy_list.index(enemy) + 1].config(text=f"{enemy.name} did {enemy_damage} damage to {character.name} by using {enemy.weapon2.name}. \n{character.name} has {character.health} health left.")
                elif enemy.weapon2.type_of_damage == "magical":
                    most_effective_spell = enemy.weapon2.spells[0]
                    current_damage = enemy.weapon2.spells[0].damage
                    for spell in enemy.weapon2.spells:
                        if spell.elemental in character.weakness:
                            most_effective_spell = spell
                            current_damage = spell.damage * 1.5
                    enemy_damage = current_damage - (character.armor.armor_value * 0.5)
                    if character.weapon2.type_of_damage is None:
                        enemy_damage -= (character.weapon2.damage_mitigation * 0.5)
                    if enemy_damage < 1:
                        enemy_damage = 1

                    if enemy.weapon2.type in character.weakness:
                        enemy_damage *= 1.5

                    character.health -= enemy_damage
                    self.enemy_attack_list[enemy_list.index(enemy) + 1].config(text=f"{enemy.name} did {enemy_damage} damage to {character.name} by using {most_effective_spell.name}. \n{character.name} has {character.health} health left.")
                else:
                    enemy.distance_from_player -= enemy.movement_distance
                    self.enemy_attack_list[enemy_list.index(enemy) + 1].config(text=f"{enemy.name} moved closer to {character.name} by {enemy.movement_distance}")
                CreateToolTip(self.player_label, text=f"Health: {character.health}")

                CreateToolTip(self.enemy_label_list[enemy_list.index(enemy)],text=f"{enemy_list[enemy_list.index(enemy)].examine()}")
                CreateToolTip(self.radio_enemy_label_list[enemy_list.index(enemy)],text=f"{enemy_list[enemy_list.index(enemy)].examine()}")

                if character.health <= 0:
                    character.health = 0
                    break
