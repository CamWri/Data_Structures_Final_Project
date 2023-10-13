
class Inventory:
    def __init__(self):
        self.gold = 10
        self.iteams = []

    def add_iteam(self, iteam, iteam_value):
        self.iteams.append(iteam)
        self.iteams_value.append(iteam_value)

    def sell_iteam(self, iteam, value):
        pass

    def add_gold(self, gold_ammount):
        self.gold += gold_ammount