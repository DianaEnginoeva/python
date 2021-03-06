
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
- цель: продемонстрировать, как разные части системы работают вместе (убедиться, что ваш код хорошо работает с другим кодом, который вы используете)
- требует таких ресурсов, как экземпляры баз данных и аппаратное обеспечение 
- более убедительно демострирует работу системы (особенно для не-программистов), чем модульное


#### Не нужно писать тесты, если:

- Вы делаете простой сайт-визитку из 5 статических html-страниц и с одной формой отправки письма. На этом заказчик, скорее всего, успокоится, ничего большего ему не нужно. Здесь нет никакой особенной логики, быстрее просто все проверить «руками»

- Вы занимаетесь рекламным сайтом/простыми флеш-играми или баннерами – сложная верстка/анимация или большой объем статики. Никакой логики нет, только представление

- Вы делаете проект для выставки. Срок – от двух недель до месяца, ваша система – комбинация железа и софта, в начале проекта не до конца известно, что именно должно получиться в конце. Софт будет работать 1-2 дня на выставке

- Вы всегда пишете код без ошибок, обладаете идеальной памятью и даром предвидения. Ваш код настолько крут, что изменяет себя сам, вслед за требованиями клиента. Иногда код объясняет клиенту, что его требования — гов не нужно реализовывать

В первых трех случаях по объективным причинам (сжатые сроки, бюджеты, размытые цели или очень простые требования) вы не получите выигрыша от написания тестов.


Чем более простую и мелкую часть системы мы тестируем — тем дешевле тесты, чем более сложную (составную) — тем сложнее. И ваша задача как специалиста — исходить не из того, чтобы соответствовать своим представлениям о видах тестирования, а писать тесты так, чтобы они в идеале покрывали большее число кейсов при небольших затратах.

#### Ваши тесты должны:

- Быть достоверными
- Не зависеть от окружения, на котором они выполняются
- Легко поддерживаться
- Легко читаться и быть простыми для понимания (даже новый разработчик должен понять что именно тестируется)
- Соблюдать единую конвенцию именования
- Запускаться регулярно в автоматическом режиме

#### Hypothesis 
это библиотека Python для создания модульных тестов, которые проще писать и которорые более эффективны при запуске
1. Проводит ваши тесты против гораздо более широкого спектра сценариев, чем может быть у человеческого тестера, и обнаруживает крайние случаи в вашем коде, которые вы в противном случае пропустили бы
2. Затем она превращает их в простые и понятные сбои, которые экономят ваше время и деньги по сравнению с их исправлением, если они проскользнули через трещины и пользователь столкнулся с ними

##### Как это работает:
Гипотеза интегрируется в ваш обычный рабочий процесс тестирования. Начало работы так же просто, как установка библиотеки и использование какого-либо кода с ее помощью - никаких новых сервисов для запуска, никаких новых тестовых роликов для изучения.
Она работает путем создания случайных данных, соответствующих вашей спецификации, и проверки того, что ваша гарантия по-прежнему сохраняется в этом случае. Если она найдет пример, где это не так, берет этот пример и сокращает его, упрощая, пока не найдет гораздо меньший пример, который все еще вызывает проблему. Затем она сохраняет этот пример позже, так что, как только обнаружит проблему с вашим кодом, она не забудет его в будущем.


#### Regression
выполняются всякий раз, когда что-либо было изменено в системе, чтобы проверить, что новые ошибки не были введены. Это означает, что вы повторно запускаете свои модульные и интеграционные тесты после всех исправлений, обновлений и исправлений ошибок.

#### Acceptance
вы должны проверить, что программа работает так, как пользователь/клиент ожидает. "Приемочные" тесты гарантируют, что функциональность соответствует бизнес-требованиям (похож на тест интеграции, но сфокусирован на использовании, а не на компонентах).
