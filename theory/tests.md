Так вот, есть только шкала. Чем более простую и мелкую часть системы мы тестируем — тем дешевле тесты, чем более сложную (составную) — тем сложнее. И ваша задача как специалиста — исходить не из того, чтобы соответствовать своим представлениям о видах тестирования, а писать тесты так, чтобы они в идеале покрывали большее число кейсов при небольших затратах.
Разработка через тестирование (англ. test-driven development, TDD)

#### unit tests VS integration tests
##### unit tests
- target: to verify that a relatively small piece of code is doing what it is intended to do
- easy to write and execute
- effectiveness depends on what the programmer considers to be useful
- don't have dependencies on outside systems

##### integration tests
- target: to demonstrate that different pieces of the system work together
- require resources like database instances and hardware to be allocated for them
- do a more convincing job of demonstrating the system works (especially to non-programmers) than a set of unit tests can


#### юнит-тестирование или интеграционное
##### юнит-тестирование (модульное)
- цель: убедиться, что относительно небольшая часть кода делает то, что она должна
- легкое в написании и выполнении
- эффективность зависит от того, что считает полезным программист
- не зависит от внешних систем

##### интеграционное
- цель: продемонстрировать, как разные части системы работают вместе
- требует таких ресурсов, как экземпляры баз данных и аппаратное обеспечение 
- более убедительно демострирует работу системы (особенно для не-программистов), чем модульное


