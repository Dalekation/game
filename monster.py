from character import Character
from weapon import Weapon

class Monster(Character):
    global available_monsters
    available_monsters = ["Гоблин", "Скелет", "Слайм", "Призрак", "Голем", "Дракон"]
    global prize_for_monster
    prize_for_monster = {
        "Гоблин": "Кинжал", 
        "Скелет": "Дубина",
        "Слайм": "Копье", 
        "Призрак": "Меч", 
        "Голем": "Топор", 
        "Дракон": "Легендарный Меч"
    }
    def __init__(self, character_type):
        monsters = {
            "Гоблин":{
                "health": 5,
                "damage": 2,
                "strength": 1,
                "agility": 1,
                "stamina": 1
            },
            "Скелет":{
                "health": 10,
                "damage": 2,
                "strength": 2,
                "agility": 2,
                "stamina": 1
            },
            "Слайм":{
                "health": 8,
                "damage": 1,
                "strength": 3,
                "agility": 1,
                "stamina": 2
            },
            "Призрак":{
                "health": 6,
                "damage": 3,
                "strength": 1,
                "agility": 3,
                "stamina": 1
            },
            "Голем":{
                "health": 10,
                "damage": 1,
                "strength": 3,
                "agility": 1,
                "stamina": 3
            },
            "Дракон":{
                "health": 20,
                "damage": 4,
                "strength": 3,
                "agility": 3,
                "stamina": 3
            }

        }
        self._damage = monsters[character_type]["damage"]
        self._character_type = character_type

        super().__init__(
            strength=monsters[character_type]["strength"], 
            agility=monsters[character_type]["agility"], 
            stamina=monsters[character_type]["stamina"], 
            health=monsters[character_type]["health"]
        )

    def __str__(self):
        return "Монстр:\n" + super().__str__() + f"\n\tУрон: {self._damage}" + f"\nКласс:\n\t{self._character_type}"
    
    def __repr__(self):
        return self.__str__()


    

    def get_prize_for_winning(self):
        return Weapon(prize_for_monster[self._character_type])

    def get_damage_changes_defence(self, weapon, hero, move):
        if self._character_type == 'Скелет':
            if weapon.get_damage_type() == 'Дробящий':
                return weapon.get_damage()
        elif self._character_type == 'Слайм':
            if weapon.get_damage_type() == 'Рубящий':
                return -weapon.get_damage()
        
        elif self._character_type == 'Голем':
            return -self.get_stamina()
        
        return 0

    def get_damage_changes_attack(self, weapon, hero, move):
        
        if self._character_type == 'Призрак':
            if self.get_agility() > hero.get_agility():
                return 1
        elif self._character_type == 'Дракон':
            if move % 3 == 0:
                return 3
            
        return 0


    def get_damage(self):
        return self._damage
