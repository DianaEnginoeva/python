Синтаксические полезности

```python 
d = []
```

```python
list_comprehension = [i * 2 for i in range(10) if i % 2 == 1]
```

вместо

```python
for i in range(10):
  if i % 2 == 1:
    d.append(i *2)
```



Для словарей

's = {}

for i in range(10):
  if i % 2 == 1:
    d.update({i : i * 2})
    
dict_comprehension = {i: i * 2 for i in range(10) if i % 2 == 1}'

GITHUB
SUBLIME
слишком много синтаксического сахара затрудняет прочтение кода, малое его количество упрощает жизнь
много сахара - будет диабет

числа фибоначчи (есть ли там ноль??)

def fib():
  a, b = 0, 1
  
  while True:
    yield a #если в функции есть yield --> эта функция вернет генератор (yield сохраняет контекст выполнения. он запоминает какую строчку он выполнял последним и возвращается к этой строчке, а не к первой строчке функции)
    
    a, b = b, a + b
    
gen = fib()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


Задания:
1) реализовать свою версию range, используя ключевое слово yield
def yourintellect():
    intellect = 1
    severhoursofhardwork = 1.5
    
    
    while True:
        yield intellect
        
        intellect = intellect * severhoursofhardwork
            
gen = yourintellect()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
2) реализовать бесконечный генератор, который каждый раз получает следующее простое число
def forever_generator():
    a = 1
    
    
    while True:
        yield a
        
        a += 1
            
gen = forever_generator()
while True:
    print(next(gen))
3) реализовать генератор, который каждый раз выдает факториал следующего числа
def factorial():
    value = 1
    while True:
        yield value
        value *= value + 1
        
gen = factorial()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

Работа с файлами

файловый дескриптор

f = open('test2.txt')
f.read() или 
f.readlines() - список всех строчек [проверить]
f.seek(0) - устанавливает принудительно место, с которого мы читаем поток (чтобы начать читать файл сначала)
f.close() - необходимо каждый раз закрывать файл (почему??)
with open('test2.txt') as f:
  print(f.read) - менеджер контекста: самостоятельно закрывает файл, в том числе, когда случаются ошибки и исключения
  
Декораторы  

декоратор- паттер проектирования
меняет поведение функции
def dec(func):
    print('Created')
    return func
return max

r = dec(min)

r(1, 2)



