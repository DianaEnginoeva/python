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

