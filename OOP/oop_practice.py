class Spell:
    def __init__(self, name, mana_cost, power):
        self.name =  name
        self.mana_cost = mana_cost
        self.power = power

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, num):
        if num < 0:
            raise ValueError
        self._power = num

    @classmethod
    def from_string(cls, string):
        name, mana_cost, power = string.split(':')#напомни что за метод еще есть strip()
        return cls(name, int(mana_cost), int(power))#я скажу честно, подсмотрел из предыдщего задания. Аразве через f строку нельзя прописать это?

    @staticmethod
    def is_high_tier(mana_cost):
        return mana_cost > 50

    def __str__(self):
        return f'Заклинание: {self.name}, Мана{self.mana_cost}, Сила: {self.power}'

    def __call__(self):
        print(f'Заклинание {self.name} успешно применено! Сила атаки: {self.power}')

    def __add__(self, other):
        if isinstance(other, Spell):
            new_name = self.name + other.name
            new_mana_cost = self.mana_cost + other.mana_cost
            new_power = self.power + other.power
            return Spell(new_name, new_mana_cost, new_power)  # Обязательно return!
         raise TypeError("Складывать можно только заклинания!")

    def __eq__(self, other):
        if isinstance(other, Spell):
           # return(max(self.power, other.power))#можно ли так делать, либо делаем так
            return self.power == other.power
        return False

    def __lt__(self, other):
        if isinstance(other, Spell):
            return self.power < other.power #тут я тоже подсмотрел в предыдущий код
        return NotImplemented


    # Тестируем создание и property
s1 = Spell("Огненный шар", 30, 95)
s2 = Spell.from_string("Ледяная стрела:15:50")
s3 = Spell("Исцеление", 40, 70)

print(s1)  # Заклинание: Огненный шар, Мана: 30, Сила: 95

# Тестируем __call__
s2()  # ✨ Заклинание Ледяная стрела успешно применено! Сила атаки: 50

# Тестируем @staticmethod
print(f"Требует ли Огненный шар много маны? {Spell.is_high_tier(s1.mana_cost)}")  # True

# Тестируем комбинацию заклинаний (__add__)
s_mega = s2 + s3
print(s_mega)  # Заклинание: Ледяная стрела + Исцеление, Мана: 55, Сила: 120

# Тестируем сравнение и сортировку по силе
print(f"Ледяная стрела слабее Огненного шара? {s2 < s1}")  # True

spells_list = [s1, s2, s3]
print("\nСортировка заклинаний по силе:")
for spell in sorted(spells_list):
    print(spell)






