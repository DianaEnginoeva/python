### Декораторы
```python
import time

def do_some():
  start = time.clock()
  result = 9
  print('Passed', time-clock() - start()) #узнать сколько по времени работает функция
  return result
```
Декоратор, по сути, это синтаксический сахар. Его использовать правильно и вроде бы проще, чем другие решения. Умеет подменять функцию (что позволяет нам выполнять действия до функции, и/или  после)
```python
import time

def timeit(func):
    def _inner():
        start = time.clock()

        result = func()

        print('Passed', time.clock() - start)
        return result
    return _inner

@timeit #do_some = timeit(do_some) - идентично
def do_some():
    return 10


s = do_some()
print(s)
```

PyCharm 

Генератор - некая новая структура данных, синтаксический сахар. Помогает решить определенный спект задач.

```python
gen = (i for i in (1, 2, 3))
next(gen)
next(gen)
next(gen)
next(gen)
```

yield делает любую функцию генератором

```python
def num():
  yield 9
```

### Задачи из дз

1. Генераторы

```python
import random
from datetime import datetime, timedelta


def all_even_numbers():
    number = 0

    while True:
        yield number
        number += 2



def random_increasing_number():
    number = random.randint(1, 100)

    while True:
        yield number
        number += random.randint(1, 5)


def next_day():
    day = datetime.today().date()

    while True:
        yield day

        day += timedelta(days=1)

day = next_day()
print(next(day))
print(next(day))
print(next(day))
print(next(day))
print(next(day))
```

### Тестирование

 ```python
 import unittest


def min_or_max(numbers, find_min=True):
    if find_min:
        return min(numbers)
    else:
        return max(numbers)


class TestMinOrMax(unittest.TestCase):
    def test_input_values(self):
        result = min_or_max([1, 2, 3])
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
```

mypy - утилита
pytest

Виртуальна среда - папка, в которой будут хранится зависимости проекта (зависимости нужны, чтобы можно было переиспользовать тесты)    

python3 -m venv .venv #.название среды
ls .venv #проверяем создали ли мы папку
source .venv/bin/activate 
pip install pytest
pytest function_ex.py #название модуля, запуск тестов


#### Для windows (cmd)
```cmd
py -m venv .venv
C:\Users\151-321\.venv\Scripts\activate
pip install pytest
```

[WakaTime](https://wakatime.com/) - за сколько реально сделана задача

#### PyCharm

Settings -> Project Interpreter -> Папка -> Установить pytest
Project -> Edit Configuration -> Путь к тестируемому файлу -> Apply -> Run


### Доп.инфа

The __init__.py files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name, such as string, from unintentionally hiding valid modules that occur later (deeper) on the module search path. In the simplest case, __init__.py can just be an empty file, but it can also execute initialization code for the package or set the __all__ variable, described later.

[_ init _](https://ru.stackoverflow.com/questions/420987/%D0%9E%D0%B1%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BA-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%BD%D0%BE%D0%B9-%D0%B2-init-py)
