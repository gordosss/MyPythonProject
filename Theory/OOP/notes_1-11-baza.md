Урок 1: Классы и атрибуты
class Point:
    color = "red"
    circle = 2
где Point — название класса, пишется с заглавной буквы.
В себе может содержать атрибуты (переменные или свойства класса).

Класс может иметь описание, например
class Point:
    'Класс для представления координат точек на плоскости'

У класса есть переменная __doc__, пример
Point.__doc__, которая выведет
'Класс для представления координат точек на плоскости'

Поменять свойство - Point.color = 'black'
Прочитать свойство - Point.color

Увидеть все атрибуты класса - Point.__dict__

Существуют экземпляры класса, например
a = Point() - где 'a', экземпляр класса Point
b = Point() - 'b' - экземляр класса Point

Обьекты a и b - экземпляры класса Point. Свойства a и b берут атрибуты из класса Point

ПОМЕНЯТЬ АТРИБУТ
Можно поменять в экземпляре атрибут, пример:
a.color = 'green'
Так мы меняем локальный атрибут color в 'a', так можно и добавить 

ДОБАВЛЕНИЕ АТРИБУТА
Также можно добавить атрибут в классе, например
Point.type_pt = 'disk'
или то же самое можно сделать с помощью команды
setattr(Point, 'prop', 1)
Если данный атрибут уже есть в классе, то он поменяет значение 

ПРОВЕРКА НА СУЩЕСТВОВАНИЕ АТРИБУТА
Если указать несуществующий атрибут класса, то код выдаст ошибку.
Чтобы этого не допустить, можно воспользоваться функцией - getattr
например
getattr(Point, 'a', False)
Если атрибута нет - выдаст False
Если атрибут есть - вернет значение атрибута

УДАЛЕНИЕ АТРИБУТА
Также можно удалять атрибуты из класса
1 способ - 
del Point.prop
Если удалять несуществующий аругмент с помощью этой команды, выдаст ошибку
Чтобы проверить существует аргумент или нет, можно использовать функцию
hasattr(Point, 'prop') - выдаст False если не существует, True - если существует
2 способ - 
delattr(Point, 'circle')
Удалять можно те атрибуты, которые присутствуют в классе

ЭКЗЕМПЛЯРЫ
Если удалить аргумент из экземпляра, например
del a.color, то код выдаст ошибку при условии, что в экземпляре нет такого аргумента, т.е., в классе аргумент есть, а в экземлпляре нет



_________________
Урок 2 Методы классов. Параметр self
Методы = действия - использовать глаголы
Свойства - существительное

class Point:
    color = 'red'
    circle = 2
Допиши конспект как понял

_______________
Урок 3 Методы: Инициализатор __init__ и финализатор __del__
__init__(self) - инициализатор обьекта класса, вызывается сразу после создания экземлпяра класса
__del__(self) - финализатор класса, вызывается перед удалением экземпляра класса

Пример ___init__:
def __init(self, x, y):
    self.x = x
    self.y = y
pt = Point(1, 2)*если аргументов не будет, возникнет ошибка
print(pt.__dict__)
Такая программа вызовет(как я понял, инициализирует) x и y, с значениями 1 и 2
{'x': 1, 'y': 2}

Пример __del__:
def __init(self, x, y):
    self.x = x
    self.y = y
def __del__(self):
    print('Удаление экземпляра:' + str(self))
такая программа удалит экземпляр,

 Урок 4 Метод __new__
class Point:
    def __new__(cls, *args, **kwargs):
        print('вызоа __new__ для' + str(cls))
    def __init__(self, x = 0, y = 0):
        print('вызов __init__ для' + str(self))
        self.x = x
        self.y = y

В методе __new__ обязательным параметром является __cls__, который ссылается на ТЕКУЩИЙ КЛАСС, в нашем случае на класс Point
В методу __init__ обязательным параметром является __self__, ссылается на создаваемый ЭКЗЕМПЛЯР КЛАССА

__new__ должен возвращать адрес обьекта  
 *args, **kwargs - обязательные аргументы __new__, в целом, общий вид функции __new__ нужно прописывать так:
 def __new__(cls, *args, **kwargs):

 Паттерн Singleton
 Суть паттерна -  в программе должен существовать только один экземпляр класса
Пример:
 class DataBase:

    _instance = None - ссылка на атрибут класса

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance

    def __del__(self):
        DataBase._instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connecr(self):
        print(f'соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('закрытие соединения с БД')

    def read(self):
        return 'Данные из БД'

    def write(self, data):
        print(f'запись в БД {data}')


____________________________
Урок 5 Методы класса (classmethod) и статические методы (staticmethod)

@classmethod - методы класса
@staticmethod - статические методы класса

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100
    @classmethod
    def validate(cls, arg): - здесь cls - ссылка на текущий класс Vector
            return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y

v = Vector(1, 2)
print(vector.validate(5)) - выведет True
res = Vector.get_coord(v)
print(res)

/ Метод validate работает только с атрибутами класса Vector, но не может обращаться к локальным атрибутам экземпляра класса. 
/Отличие от обычного в том, что в обычном присутствует парамтер self, и если вызывать его, то обязательно нужно в нем передать ссылку на экземпляр класса.
/то есть в 'res = Vector.get_coord(v)' ты в скобках передаешь ссылку в виде v - которая ссылается прямо на Vector. А в 'print(vector.validate(5))' только параметр.

Правильно будет ссылаться не на название класса, а на ссылки (параметры), такие как cls или self
Пример:
class Vector:
    MIN_COORD = 0
    MAX_COORD = 100
    @classmethod
    def validate(cls(ВОТ ЭТОТ ПАРАМЕТР), arg): - здесь cls - ссылка на текущий класс Vector
            return cls(ЭТОТ ПАРАМЕТР).MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self(ЭТОТ ПАРАМЕТР).validate(x) and self(ТО ЖЕ).validate(y):
        self.x = x 
        self.y = y

    def get_coord(self):
        return self.x, self.y

/@staticmethod - определяет методы которые не миеют доступа ни к атрибутам класса, ни к аатрибутам его экземпляров. Создается независимая функция
 
 Пример
@staticmethod
def norm2(x. y):
    return x*x + y*y 

Итог
Vector
MIN_COORD = 0
MAX_COORD = 100

@classmethod
def validate(cls, arg):...
- этот метод работает только с атрибутами класса(в нашем случае MIN_COORD и MAX_COORD). Ссылкой является cls. Работать с экземпляром класса напрямую не получится, т.к нет ссылки на соответствующий экземпляр


def __init__(self, x, y):... -
def get_coord(self):...
-эти два метода вызываются из экземпляров класса, и работают с атрибутом через self и также с атрибутами класса Vector. 

@staaticmethod
def norm2(x, y):...
- соверешнно независимая функция, не обращается ни к атрибутам к класса, ни тем более к локальнеым атрибута класса. `




_______________________________
Урок 6 Механизм инкапсуляции. Режим доступа public, private, protected. Сеттеры и геттеры

 class Point:
    def __init__(self,  = 0, y = 0):
        self.x = x
        self.y = y
pt = Point(1, 2)
print(pt.x, pt.y)
Данный код выведет 1 2, обращаемся к классу через pt

Существуют ограничения доступа:
attribute (без одного или двухподчеркиваний вначале) - публичное св-во - public
_attribute (с одним подчеркиванием) - режим доступа protected (служит для обращения внутри класса и во всех его дочерних классах)
__attribute (с двумя подчеркиваниями) - режим доступа private (служит для обращения только внутри класса)

 class Point:
    def __init__(self,  = 0, y = 0):
        self._x = x
        self._y = y
pt = Point(1, 2)
print(pt._x, pt._y)
Данный код выведет 1 2, т.к., protected - лишь визуально предупреждает программиста, чтобы переменная не использовалась


 class Point:
    def __init__(self,  = 0, y = 0):
        self.__x = x
        self.__y = y
pt = Point(1, 2)
print(pt.__x, pt.__y)
Данный код выведет ошибку



 class Point:
    def __init__(self,  = 0, y = 0):
        self.__x = x
        self.__y = y
    def set_coord(self, x, y):
        self.__x = x
        self.__y = y

pt = Point(1, 2)
pt.set_coord(10. 20)
Даннй код не выведет ошибки, т.к., внутри класса мы можем обращаться, но извне доступа нет

Добавим в код get_coord

 class Point:
    def __init__(self,  = 0, y = 0):
        self.__x = x
        self.__y = y
    def set_coord(self, x, y):
        self.__x = x
        self.__y = y
        def get_coord(self):
            return self.__x, self.__y
    
pt = Point(1, 2)
pt.set_coord(10. 20)
print(pt.get_coord)
этот код также вернет значения (return)


get_coord - геттер - метод инкапсуляции
set_coord - сеттер - метод инкапсуляции

 @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0
            print('Персонаж мёртв')
        else:
            self._hp = value

также эти методы могут использоваться для проверки, т.е., if 'условие', то уже "какое то действие"

также приватныы могут быть методы, к примеру
def __check_value(self):

В коде
 class Point:
    def __init__(self,  = 0, y = 0):
        self.__x = x
        self.__y = y

    @classmethod
    def _check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
    def get_coord(self):
        return self.__x, self.__y
    
pt = Point(1, 2)
pt.set_coord(10. 20)
print(pt.get_coord)


Также можно использовать более сильный приват режим. Делается это при помощи acessify - библиотека

from accessify import private, protected

@classmethod
def __check_value


________________________________________

Урок 7 Методы **__setattr__**, **__getattribute_-**, __getattr__**, **__delattr__

class Point:
MAX_COORD = 100
MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def set_bound(self, left):
        self.MIN_COORD = left

    def __getattribute__(self,item):
        print('__getattribute__')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print('__setattr__')
        object.__setattr__(self, key, value)


    def __getattr__(self, item):
        print('__getattr__:' + item)

    def __delattr__(self, item):
        print('__delattr__:' + item)
        object.__delattr__(self, item)

Здесь MAX_COORD и MIN_COORD - являются св-ми класса (2 св-ва)
def - методы класа (2 метода)
Все это является атрибутами класса (4 атрибута)

Все атрибуты остаются класса - являются общими для всех его экземпляров. Из экземпляров класса можно обращаться к св-ам класса

*напоминание. Лучше обращаться к св-ву не через явное обращение, т.е. не Point.MIC_COORD,  а через ссылку, т.е.,self.MIN_COORD

 Чтобы поменять  значение св-ва, к примеру
 def set_bound(self, left):
 self.MIN_COORD = LEFT
 #здесь значение поменяется не в классе,а внутри нашего метода, то есть мы создали новое локальное св-во, а прежнее св-во классса Point осталось без изменений. 
 Чтобы поменять в методе значение св-ва класса, в нашем случае класса Point, правильнее было бы:
@classsmethod
def_set_bound(self, left):
    cls.MIN_COORD = left
т.е., взять классметод и обратиться через cls, а не через self

object - добавил к методам, чтобы методы отработали корректно. object - класс, от которого неявно наследуются все классы в пайтон

__getattribute__(self, item) - self(ссылка на экземпляр класса), item(Атрибут, к которому идет обращение)
Метод автоматически вызывается, когда идет считывание атрибута через экземпляр класса
def __getattribute__(self, item):
    if item = 'x'"
        raise ValueError('Доступ запрещен")
    else:
        return object.__getattribute__(self, item)

К примеру
pt1 = Point(1,2)
a = pt1.x - где а, атрибут через экземпляр класса
Должен возвращать значение атрибута, необходимо использовать метод через return, если return убрать то программа выведет None. ПО умолчанию без return возвращает None


__setattr__(self, key, value): - key - имя атрибута, value - значение которое присваивается атрибуту
Метод автоматически вызывается когда идет присвоение какому либо атрибуту определенного значения
def __setattr__(self, key, value):
    if key = 'z':
        raise AttributeError('недопустиме имя атрибута')
    else:
        object.__setattr__(self, key, value) 

__getattr__(self, item)
Метод автоматически вызывается каждый раз когда идет обращение к несуществующему атрибуту экземпляра класса
def __getattr__(self, item):
    print('getattr__: + item)
    выведет название несуществующего обьекта
или можно такЖ
def __getattr___(self, item):
    return Fase - вернет False если был вызыван несуществующий обьект. Если данного метода нет, программа в целом может войти  в ошибку


__delattr__
метод автоматически вызывается при удалении свойства item(не важно существует оно или нет)

________________________________________________________________
__________________________________________
9 урок Свойства property. Декоратор @property

декоратор @property pfvtyztn utnnth
@имя.setter - заменяет сеттер
Без сеттера свойство автоматически становится Read-Only(только для чтения)

Пример:

Главный сценарий: защищенный атрибут(Чтение + Запись)
class Person:
    def __init__(self, age):
        self._age = age  # Храним данные в _age

    # 1. Геттер (чтение: p.age)
    @property
    def age(self):
        return self._age

    # 2. Сеттер (запись: p.age = 25)
    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Неверный возраст!")

Главные правила:

1) Имена функций у геттера и сеттера должны строго совпадать (age).
2) Внутренний атрибут называют с подчёркиванием (_age), чтобы его имя не совпадало с именем @property (иначе будет бесконечная рекурсия).




___________________________
Урок 11 Дескрипторы data descriptor и non-data descriptor

Дескрипторы - класс, который имеет метод в зависимости от того, какой это класс (данных или не данных)

Если это non_data_sescriptor (дескриптор не данных), то он имеет метод __get__
def __get__(self, instance, owner):
    return...

Если этот data_descriptor(дескриптор данных), то он имеет метод __get__, __set__, __del__
def __get__(self, instance, owner):
    return
def __set__(self, instance, value):..

def __del__(self):..

Итак, приведем пример, дескриптора

class Integer: 
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self,name]

    def __set__(self, instance, value):
        print(f'__set:{self.name} = {value}')
        instance.__dict__[self.name] = value

здесь class Integer - название класса

Затем в классе Point3D создаем экземпляры класса Integer, т.е.,

class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

Здесь x, y, z - и есть дескрипторы, находящиеся в классе Point 3D.

После того как мы создали дескрипторы, автоматически срабатывает метод set_name, в котором
параметр self - ссылка на создаваемый экземпляр класса, то есть name = '_x'
параметр owner - ссылка на класс Point3D
параметр name = имя, которое прописано в классе Point3D, в нашем случае имена x, y, z, которым присваивается экземпляр класса

далее мы создаем экземпляр класса Point3D

pt = Point3D(1,2,3)
_x = 1
_y = 2
_z = 3
 
При создании этого экземпляра, срабатывает инициализатор __init__,  в инициализтаторе идет обращение к дескрипторам, и присваивается соответствущее значение 1, 2, 3 (которое мы прописали в pt)
В этот момент срабатывает сеттер __set__ который находится в класссе Integer.
В сетере self - ссылка на экземпляр класса Integer (который name = '_x')
instance - ссылается на экземпляр класса Point3D(который pt), из которого дескриптор был вызван
value - числовое значение которое мы присваиваем










