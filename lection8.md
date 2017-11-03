### Декораторы
```python
import time

def do_some():
  start = time.clock()
  result = 9
  print('Passed', time-clock() - start()) #узнать сколько по времени работает функция
  return result
```
Декоратор, по сути, это синтаксический сахар. Его использовать правильно и вроде бы проще, чем другие решения
```python
import time

def timeit(func):
    def _inner():
        start = time.clock()
        result = func()

        print('Passed', time.clock() - start())
        return result
    return _inner

@timeit
def do_some():
    return 10

s= do_some()
print(s)
```

