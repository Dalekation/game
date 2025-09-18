from random import randint
import time
from hero import Hero, get_number, available_classes
from monster import Monster, available_monsters


def fight(hero, enemy):
    agility_total = hero.get_agility() + enemy.get_agility()

    move = 1
    cur_hero_health = hero.get_health()
    cur_enemy_health = enemy.get_health()
    while True:
        print(f"\nХод {move} героя:")
        priority = randint(1, agility_total)

        # Атака промахнулась
        if priority <= enemy.get_agility():
            print(f"Герой промахнулся.")
        else:
            # Атакует герой монстра
            base_damage = hero.get_weapon().get_damage() + hero.get_strength()
            base_damage += enemy.get_damage_changes_defence(hero.get_weapon(), hero, move)
            base_damage += hero.get_damage_changes_attack(enemy, move)

            if base_damage > 0:
                print(f"Нанесено {base_damage} урона монстру!")
                cur_enemy_health -= base_damage
                if cur_enemy_health <= 0:
                    print(f"Монстр побежден!")
                    return 1
            else:
                print(f"Урон монстру не был нанесен.")
        time.sleep(3)
        print(f"\nХод {move} монстра:")
        priority = randint(1, agility_total)

        # Атака промахнулась
        if priority <= hero.get_agility():
            print(f"Монстр промахнулся.")
        else:
            # Атакует монстр героя
            # Считаем, что для монстров и для героев добавляется
            base_damage = enemy.get_damage() + enemy.get_strength()
            base_damage += enemy.get_damage_changes_attack(hero.get_weapon(), hero, move)
            base_damage += hero.get_damage_changes_defence(enemy, move)

            if base_damage > 0:
                print(f"Нанесено {base_damage} урона герою!")
                cur_hero_health -= base_damage
                if cur_hero_health <= 0:
                    print(f"Герой побежден!")
                    return -1
            else:
                print(f"Урон герою не был нанесен.")

        move += 1

        print(f"Осталось здоровья:\n\tМонстр - {cur_enemy_health}\n\tГерой - {cur_hero_health}")
        # чтобы не слишком быстро появлялись строки
        time.sleep(3)

def start_game():
    print("Выберите класс, с которого вы начнете")
    for i, el in enumerate(available_classes):
        print(f"{i + 1}) {el}.")

    res = get_number(1, len(available_classes))
    for i, el in enumerate(available_classes):
        if i + 1 == res:
            hero = Hero(el)
            print("Герой создан.\n")
            print(hero)
            time.sleep(3)

    turn = 1
    while True:
        enemy = Monster(available_monsters[randint(0, len(available_monsters) - 1)])
        print("\nНачинается бой против\n")
        print(enemy)
        time.sleep(3)
        # print('\nВаш герой\n')
        # print(hero)
        # time.sleep(3)
        res = fight(hero, enemy)

        if res == 1:
            hero.change_weapon(enemy.get_prize_for_winning())
            if hero.get_current_level() < 3:
                hero.level_up()
        else:
            print("Увы, вы проиграли!")
            break
        
        if turn <= 5:
            turn += 1
        else:
            print("\nПоздравляем! Вы закончили игру!")
            break

    
start_game()