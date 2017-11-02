Лекция 4 

Ответы на теоретический тест

1)
- Нехэшируемые типы данных не могут быть в словаре
- Tuple используют вместо List, когда не нужно изменять
- Слабые стороны linked-list: медленный поиск конкретного элемента, 

Какова сложность получения объекта 
2)
- Except ловит все исключения
- except exception as e - не ловит специальные исключения, есть переменная, в которой хранится ошибка
- 3 функции, которые принимают любое кол-во позиционных элементов: print, min, max
- Для каких задач может применяться синтаксис ** - для получения любого кол-ва именованных аргументов, чтобы передать в объект все ключи словаря test(**{‘1’: ‘o’}), для возведения в квадрат
- Какие проблемы решает замыкание - (замыкание - это ) - можно явно не передавать переменные в функцию, есть случаи, в которых переменную можно передать только с помощью замыкания
- Зачем используется git stage - промежуточное состояние

dir(объект) - посмотреть какие методы и атрибуты есть у данного объекта и его родителя

объект._dict_ - методы и атрибуты только данного объекта (посмотреть все ключи и значения)

Deque - тип данных, типа List, можно добавлять в начало и удалять из начала

hacktoberfest

Исключения

- [x] 'AttributeError', 
a=5
a.append(8)
- [x] 'Exception',
raise Exception('Test')
- [x] 'ImportError’,
import randomm (=ModuleNotFoundError)
- [x] 'IndentationError', (неправильное кол-во пробелов)
- [x] 'IndexError',
a=[1, 2]
print(a[3])
- [x] 'KeyError',
dic={'1': 'p'}
print(dic['p'])
- [x] 'KeyboardInterrupt',
ctrl+c
- [x] 'TypeError',
a=5
print(a[1])
- [x] 'ValueError',
a=[1, 2, 3]
a.index(4)
- [x] 'ZeroDivisionError'
a=1/0

Обработка исключений (в случае, если пользователь ошибется)

try:
except ValueError as e:
print(‘’, e)

Декомпозиция - разбиение большой задачи на более мелкие

Объектно-ориентированное программированние

Зачем? Чтобы писать более простой код. Чтобы переиспользовать код и тем самым помогать разработчику.

Каким образом он помогает сделать код более простым? ООП помогает писать меньше кода (если есть объекты, можно не писать отдельные функции).

Самый лучший код - не написанный.

1. Инкапсуляция - сокрытие данных (можно использовать уже придуманные функции и т.д. и не париться), ответ на вопрос - что можно менять, что можно делать, нужна для того, чтобы не накосячить.
2. Наследование - возможность переиспользовать родительский код из дочерних.
3. Полиморфизм - позволяет использовать функции по разному, вне зависимости от типа их параметров (функция print, например, может печатать любой тип данных).

В python строгая динамическая типизация.

Утиная типизация - если что-то крякает, как утка, плавает, как утка, скорее всего, это - утка (самое простое решение является, скорее всего, правильным).

Пример:
есть a + b
Значит, скорее всего, a и b - относятся к типу данных, который поддерживает сложение.
ТО есть, если что-то похоже на что-то, можно использовать это, как это самое.

У каждого объекта в Python может быть несколько супер-классов (класс, от которого объект наследует). 

Из родителя нельзя получить доступ к другим наследникам.

Все эти принципы помогают решать глобальную задачу: переиспользовать код.

Класс - это шаблон, первоначально производит примерно одинаковые объекты. 

class Test(object): #наследование от object
pass

t=Test() #создание объекта класса

объекты по умолчанию не равны друг другу

id(t) #адрес в памяти объекта

Если адрес в памяти у объектов равен, то объекты равны (только в этом случае).

Функция внутри класса - метод.

class Test(object):
number = 4
value = 10
def run():
print('Runn!')

Нельзя вызвать run с помощью объекта t

class Test(object):
number = 4
value = 10
def run(self):
print('Runn!', self)

Можно вызвать run с помощью объекта t

Эквивалентные по исторической причине
Test.run(t)
t.run()

self - это параметр (можно написать другой и все будет работать)

Передать еще один параметр 

class Test(object):
number = 4
value = 10
def run(self, a):
print('Runn!',
self, a)

t = Test()
t.run(7) #Runn! <__main__.Test object at 0x105621f98> 7

t.run() #Traceback (most recent call last):
File "<pyshell#498>", line 1, in <module>
t.run()
TypeError: run() missing 1 required positional argument: 'a'

__init__ - конструктор

class Test(object):
def __init__(self, z, x):
print(x, z)

t = Test() #ошибка

t = Test(4, 6) #6 4

Сохраняем значение в атрибут 

class Test(object):
def __init__(self, z, x):
print(x, z)
self.x=x
self.z=z
self.y = 'Y!'

t=Test(1, 3) #3 1
t.x, t.y, t.z #(3, 'Y!', 1)

__mro__ (method resolution order - порядок разрешения методов) - чтобы Python правильно находил атрибуты объектов???? 

AsyncTest.__mro__ #(<class '__main__.AsyncTest'>, <class '__main__.Test'>, <class 'object'>)

setattr(g, ’12factor’, 12) ???
getattr(g, ’12factor’) ???

Практика

1. Написать класс, который принимает в конструкторе число и имеет три метода: увеличить на 1 и уменьшить на 1. а также метод "показать значение"

Неправильно:
class Task1(object):
def __init__(self, x):
pass
def decrease(x):
dec=x + 1
print(dec)
def increase(x):
inc = x - 1
print(inc)
def number(x):
print(x)

Правильно:
class Number(object):
def __init__(self, number):
self.number = number #сохраняем переменную, чтобы мы могли использовать ее в других частях класса
def decrease(self):
self.number= self.number - 1
return self.number
def increase(self):
self.number= self.number - 1
return self.number
def show(x):
print(self.number)

2. Написать класс, который принимает в конструкторе любое количество аргументов. У него есть два метода: один возвращает минимальное значение, другой максимальное

Правильно:
class MultipleValues(object):
def __init__(self, *numbers):
self.numbers = numbers

def get_min(self):
return min(self.numbers)

def get_max(self):
return max(self.numbers)

m = MultipleValues(1, 2, 3, 10, -9)
print(m.get_min())
print(m.get_max())

3. Написать класс, который принимает два числа. И у него есть 4 метода для вывода результата разных мат.операций: деление, умножение, сложение и вычитание

Неправильно:
class Task3(object):
def __init__(self, x, y):
pass
def add(x, y):
amount = x + y
print(amount)
def mul(x, y):
composition = x * y
print(composition)
def sub(x, y):
diffrence = x - y
print(diffrence)
def div(x, y):
division = x / y
print(division)

Правильно:
class MathApplication(object):
def __init__(self, number1, number2):
self.number1 = number1
self.number2 = number2

def multiply(self):
return self.number1 * self.number2

def divide(self):
return self.number1 / self.number2

def sum(self):
return self.number1 + self.number2

def minus(self):
return self.number1 - self.number2

public - пользователь будет использовать
_protected - не будет использовать

__что-то__ - магическая штука (метод), потому что явно мы её не используем.
Переопределяет поведение класса в разных ситуациях.

class AlwaysEqual(object):
def __equal (self, other):
print(other)
return True

Вопросы:
1. Зачем нужен конструктор? Что он делает?
2.
