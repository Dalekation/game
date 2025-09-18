class Weapon:
    global available_weapons 
    available_weapons = ["Меч", "Дубина", "Кинжал","Топор","Копье","Легендарный Меч"]
    def __init__(self, name):
        self._name = name

        # Здесь можно положить просмотр конфига
        weapons_damage = {
            "Меч": 3,
            "Дубина": 3,
            "Кинжал": 2,
            "Топор": 4,
            "Копье": 3,
            "Легендарный Меч": 10
        }

        # Здесь можно положить просмотр конфига
        weapons_type = {
            "Меч": "Рубящий",
            "Дубина": "Дробящий",
            "Кинжал": "Колющий",
            "Топор": "Рубящий",
            "Копье": "Колющий",
            "Легендарный Меч": "Рубящий"
        }

        self._damage = weapons_damage[name]
        self._damage_type = weapons_type[name]

    

    def get_damage_type(self):
        return self._damage_type

    def get_damage(self):
        return self._damage

    def get_name(self):
        return self._name
    
    def __str__(self):
        return f"{self._name} (Урон: {self._damage}, Тип урона: {self._damage_type})"
    
    def __repr__(self):
        return self.__str__()
