### Scrapy

скрэпинг = парсинг

API официально разрешено
Против скрэпинга есть различные инструменты защиты

HTTP - чтобы клиент мог работать с веб-сервером
- request (заголовок (серверная инфа), тело запроса)
- response (заголовок (серверная инфа), тело запроса)


##### Запросы:

- GET - получить
- POST - отправить (СОЗДАТЬ, создает новые данные)
- PUT - обновляет существующие данные (ИЗМЕНИТЬ, полностью заменяет)
- DELETE - УДАЛИТЬ
- HEAD - заголовок (без тела)
- PATCH - улучшить, изменить (частично изменяет данные)
- OPTIONS - системный, используется, например, при проверки https-сертификатов, проверяет, какие запросы можно отправлять (сихронные или асинхронные)
дополнительные запросы нужны, чтобы указать контекст и не использовать один и тот же метод для разных действий

ВСЕГДА HEAD, OPTIONS и то, что используешь.

[Swagger](http://petstore.swagger.io/#/) - документирование API

- асинхронные запросы - могу происходить без вашего ведома, более ограничены в плане безопасности
- синхронные запросы - 

Cookies - активность пользователя, которая сохраняется. Изначально это заголовок (данные передаются и хранятся в формате ключ-значение).

IP - интернет-протокол, который обеспечивает работу всей существующей сети (каждый ресурс индентифицирует, с помощью порта позволяет распределять пакеты по разным компьютерам, 

### TCP/IP:

1. application (FTP, Telnet, DNS)
2. transport (TCP, UDP)
3. internet (IP, ICMP, ARP)
4. network interface

Если есть буферизация, можно использовать UDP.

```python
import requests

response = requests.get('https://ya.ru')
print(response.status_code)
```

##### Статусы http:

- 200 - success (всегда, когда что-то хорошо)
- 201 - created (что-то создалось)
- 401 - unauthorized
- 405 - метод не разрешен
- 418 - I'm a teapot
- 302 - временно перемещено

```python
import requests

url = 'http://habrahabr.ru'
print(url)

response = requests.get(url)
response.content
```

### Заметки:

- Утилита Postman 
- [Let’s Encrypt](https://letsencrypt.org/) - сервис бесплатных https-сертификатов
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - html-парсер
- [Pythex](https://pythex.org/)
- [Scrapy](https://scrapy.org/)
- [Пример Scrapy](https://github.com/mos-polytech/2017/blob/master/code/course8/scrapy_example/spider.py)
