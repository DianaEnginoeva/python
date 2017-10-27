Вопросы теста:
- почему писать длинные функции - плохо?

Ссылки на ответы теста:
агрегация, композиция - http://plssite.ru/it_etc/csharp_agregation_article.html
неправильное использование наследованя - https://books.google.ru/books?id=_9ZLDAAAQBAJ&pg=PA283&lpg=PA283&dq=%D0%BD%D0%B5%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5+%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5+%D0%BD%D0%B0%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F&source=bl&ots=PB5S_6q4YL&sig=dcWNHTyuOroVYzsWuKxiet8N5Go&hl=ru&sa=X&ved=0ahUKEwi2-KHep5DXAhXMHJoKHbP8A2gQ6AEIPjAF#v=onepage&q=%D0%BD%D0%B5%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%B0%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F&f=false

Синтаксические полезности
'd = []

list_comprehension = [i * 2 for i in range(10) if i % 2 == 1]

вместо

for i in range(10):
  if i % 2 == 1:
    d.append(i *2)'



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



