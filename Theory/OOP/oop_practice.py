class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self._hp = hp
        self.power = power
        print(f'Создание {self.name}, {self._hp}, {self.power}')

    def __del__(self):
        print(f'Удаление {self.name}')

    def attack(self):
        return f'{self.name} наносит удар силой {self.power}!'

    @classmethod
    def create_default(cls, name, hp = 100, power = 10):
        return cls(name, hp, power)

    @staticmethod
    def is_alive(hp):
        return hp >0


    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0
            print('Персонаж мертв')
        else:
            self._hp = value


    def __str__(self):
        return f"Имя: {self.name}, HP: {self.hp}, Сила: {self.power}" #не понял как тут сработает проперти

    def __repr__(self):
        return f 'Character('{self.name}')'

    
