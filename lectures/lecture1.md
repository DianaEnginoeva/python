### Типы данных 
- int 
- float 
- complex (квадрат которого равен -1) 
- bool (например, a = True) 
bool(0, None) -> False 
bool(любое другое) -> True
- string<br>
т. к. python - динамический язык, нельзя сказать, сколько точно займет места тот или иной тип, например, int

### Операторы
- == сравнение
- != не равно 

not True -> False 
-none (ничего) 
константа равна только самой себе, не можем переопределить (также как и True), потому что константа 

'a'=="a" -> True 
можем строку умножить на число 
у конкатенации нет обратной операции 

5**0.5 (квадратный корень из 5) 

5**-1 (1/5) 

5**-2 (1/25) 

2 and 4 - выводит последнее значение 

2 and 0 - выводит 0, потому что False 

or - выводит первое значение 

условия 

```python
if test1: 
  state1 
elif test2: 
  state2 
else: 
  state3 
```
многострочная строка
```python
print(""" 
This string contains multiline 
text. And extra spaces. 
""")
```
приведение к строке
```python
# Casting to string: 
print(str(4))

print(str(4 + 1)) 

print(str(4) + '1') # 41
```

[] -оператор индексирования (получает элемент по индексу)
```python
'abc'[0] # a
``` 
срез не включительно
```python
'abc'[0-3] #abc
```
последний символ
```python
'abc'[-1]
```
3-й с конца
```python
'abc'[-3]
```
от минус одного до -4 не включительно с шагом -1
```python
'abc'[-1:-4:-1]
```
вся строка
```python
'abc'[:]
```
от одного до 4 не включительно с шагом 2
```python
'abcd'[1:4:2]
```
проверка вхождения подстроки в строку 
```python
# Testing occurrence 
print('be' in 'To be or not to be?') # True 
print('123' in '123') # True 
print('100' in '200') # False
```
```python
print('I am not there' not in 'String')
```
форматирование
```python
# String format: 
print('Hello, {}. You are learning {}'.format('Nikita', 'Python'))
```
Пример:
```python
a='Diana' 
print('Darova, {}'.format(a)) # Darova, Diana
```
разбивает строку на части, используя разделитель, и возвращает эти части списком
```python
for number in '123'.split(' '): 
  print(number)
```
длина строки
```python
# String length: 
print(len('7 chars'))
```
узнать кол-во памяти, занимаемое нулем (в байтах)
```python
import sys
sys.getsizeof(0)
```
! Григорий Петров - it-speaker 
