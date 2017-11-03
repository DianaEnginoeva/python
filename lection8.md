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

1. Написать функцию, которая возвращает генероторное выражение, которое включает в себя все четные числа от 0 до 100

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
