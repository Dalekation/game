from character import Character
from weapon import Weapon
from random import randint


def get_number(left, right):
    res = input()
    while not res.isdigit() or int(res) < left or int(res) > right:
        print(f"Неверный формат ввода или число вне диапазона. Введите число от {left} до {right}.")
        res = input()
    
    return int(res)

class Hero(Character):
    global available_classes
    available_classes = ["Разбойник", "Воин", "Варвар"]
    def __init__(self, character_type):
        # Здесь можно положить просмотр конфига
        class_health = {
            "Разбойник":4,
            "Воин":5,
            "Варвар":6
        }
        # Здесь можно положить просмотр конфига
        class_weapon = {
            "Разбойник":"Кинжал",
            "Воин": "Меч",
            "Варвар": "Дубина"
        }

        if character_type not in class_health:
            raise ValueError("Неверный тип персонажа (класс героя)")
        super().__init__(strength=randint(1, 3), agility=randint(1, 3), stamina=randint(1, 3), health=class_health[character_type])

        self._weapon = Weapon(class_weapon[character_type])
        self._character_type = [(character_type, 1)]


    def __str__(self):
        return "Герой:\n" + super().__str__() + "\nКлассы:\n" + '\n'.join(map(lambda x: "\t" + x[0] + f" (уровень {x[1]})", self._character_type))
    def __repr__(self):
        return self.__str__()
    
    def get_current_level(self):
        total_res = 0
        for el in self._character_type:
            total_res += el[1]
        
        return total_res
    
    def get_weapon(self):
        return self._weapon
    
    def get_damage_changes_attack(self, monster, move):
        final_res = 0
        for char_type in self._character_type:
            if char_type[0] == 'Разбойник':
                if char_type[1] >= 1:
                    if self.get_agility() > monster.get_agility():
                        final_res += 1
                if char_type[1] >= 3:
                    final_res += move - 1
            elif char_type[0] == 'Воин':
                if char_type[1] >= 1:
                    if move == 1:
                        final_res += self._weapon.get_damage()
            elif char_type[0] == 'Варвар':
                if char_type[1] >= 1:
                    if move <= 3:
                        final_res += 2
                    else:
                        final_res -= 1

        return final_res
    
    def get_damage_changes_defence(self, monster, move):
        final_res = 0
        for char_type in self._character_type:
            if char_type[0] == 'Воин':
                if char_type[1] >= 2:
                    if self.get_strength() > monster.get_strength():
                        final_res -= 3
            elif char_type[0] == 'Варвар':
                if char_type[1] >= 2:
                    final_res -= self.get_stamina()

        return final_res
    
    def update_class(self, class_name):
        if self.get_current_level() >= 3:
            raise ValueError("Нельзя увеличить уровень выше 3-го")
        
        if len(self._character_type) == 0:
            raise ValueError("Нельзя увеличить уровень без класса")
        
        found = False
        for i in range(len(self._character_type)):
            if self._character_type[i][0] == class_name:
                if class_name == 'Разбойник':
                    if self._character_type[i][1] == 1:
                        self._agility += 1
                elif class_name == 'Воин':
                    if self._character_type[i][1] == 2:
                        self._strength += 1
                elif class_name == 'Варвар':
                    if self._character_type[i][1] == 2:
                        self._stamina += 1
                
                self._character_type[i] = (class_name, self._character_type[i][1] + 1)
                
                found = True 

                break

        if not found:
            raise ValueError("Класс не найден")
        
    def add_new_class(self, class_name):
        # добавить проверку что нет класса и что сумма уровней ниже 3
        if self.get_current_level() >= 3:
            raise ValueError("Нельзя увеличить уровень выше 3-го")
        for i in range(len(self._character_type)):
            if self._character_type[i][0] == class_name:
                raise ValueError("Нельзя добавить класс повторно")
        
        self._character_type.append((class_name, 1))


    def change_weapon(self, new_weapon):
        print("Вы можете поменять оружие")
        print(f"Ваше текущее оружие {self._weapon}")
        print(f"Вы можете его поменять на {new_weapon}")
        print("Поменять? (0 - нет, 1 - да)")

        res = get_number(0, 1)

        if res == 0:
            print("Вы успешно оставили текущее оружие")
        elif res == 1:
            self._weapon = new_weapon
            print("Вы успешно поменяли оружие")


    def level_up(self):
        print("Вы можете повысить уровень или дополнительно получить новый класс")
        print("Выберите действие")
        available_classes = ["Разбойник", "Воин", "Варвар"]

        for i, el in enumerate(available_classes):
            found = False
            for character in self._character_type:
                if el == character[0]:
                    print(f"{i + 1}) {el} повысить до {character[1] + 1} уровня.")
                    found = True
            
            if not found:
                print(f"{i + 1}) Добавить класс {el} 1 уровня.")

        print("Введите только номер пункта")

        res = get_number(1, len(available_classes))

        for i, el in enumerate(available_classes):
            if i + 1 == int(res):
                found = False
                for character in self._character_type:
                    if el == character[0]:
                        self.update_class(el)
                        self.set_health(self.get_health() + self.get_stamina())
                        found = True
                        print(f"Увеличили уровень у {el}")
                
                if not found:
                    self.add_new_class(el)
                    print(f"Добавили класс {el}")

                break    
