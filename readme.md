# Тестовое задание. 
## Необходимо реализовать django приложение, которое будет взаимодействовать с платежной системой stripe.

Для запуска приложения вы можете сделать следующее:
Вы можете перейти по ссылке http://epetrishchev.pythonanywhere.com/ и можете рользоваться приложением, добавлять товары в магазин и покупать их. Там все просто уверен вы разберетесь.

Или равзерните проект на своем локальном копмьютере. Для этого:
1. Клонируйте репозиторий командой `git clone https://github.com/epetrishchev/test_stripe.git`
2. Установите виртуальное окружение `python -m venv myvenvname`
3. Установите зависимости из файла `requirements.txt`
4. Создайте аккаунт на сайте stripe.com и получите свои PUBLIC_KEY и SECRET_KEY.
5. В корневой папке проекта создайте файл `.env` и заполните его данным по шаблону из файла `.env.dist` который также лежит в коневой папке.
6. Перейдите в папку test_stripe/app/ Запустите django проект командами `python manage.py migrate` и `python manage.py runserver`
