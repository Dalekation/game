class Character:
    def __init__(self, strength=0, agility=0, stamina=0, health=0):
        self._strength = strength
        self._agility = agility
        self._stamina = stamina
        # считаем, что и для Монстров и Героев добавляется
        self._health = health + stamina


    def __str__(self):
        return f"\tСила:{self._strength}\n\tЛовкость:{self._agility}\n\tВыносливость:{self._stamina}\n\tЗдоровье:{self._health}"
    
    def __repr__(self):
        return self.__str__()
    
    def get_strength(self):
        return self._strength
    
    def get_agility(self):
        return self._agility
    
    def get_stamina(self):
        return self._stamina
    
    def get_health(self):
        return self._health
    
    def set_health(self, new_health):
        self._health = new_health
