<h2>Django</h2>

Установка Django на macbook:

1. Verify that you have Python on your computer
```terminal
python --version
```
2. Verify that you have pip 
```terminal
pip --version
```
OR
2. Install pip
```terminal
curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py
```
3. Using pip to install Django
```terminal
sudo pip install Django
```


Создать новый проект
django-admin startproject first_project

нахуя?
python manage.py runserver
перейти по указанной ссылке
например: Starting development server at http://127.0.0.1:8000/

??? типы масштабирования бд (репликация)

python manage.py migrate

https://www.slothparadise.com/how-to-install-django-on-mac/

python manage.py createsuperuser


http://127.0.0.1:8000/admin/login/?next=/admin/


python manage.py startapp hello_app
