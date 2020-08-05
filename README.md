# Library
init commit
------------------------------------------------

Уже развёрнутое приложение
https://mighty-beyond-10110.herokuapp.com

Админка приложения
https://mighty-beyond-10110.herokuapp.com/admin
login - admin
password - admin

------------------------------------------------

Всё необходимые для деплоя файлы с настройками уже в проекте.
Всё что необходимо сделать:
- Скачать архив репозитория
- распаковать в папку (допустим Library)
- в папке с проектом (Library) из консоли запускаем следующие команды:
  - git init
  - git add .
  - git commit -m "initial commit"
    это инициирует репозиторий.
- Теперь, когда мы инициализировали репозиторий, добавили в него и закоммитили все файлы, мы готовы объявить этот репозиторий приложением heroku:
  - heroku create
- в консоли копируем имя приложения созданного на heroku
- вставляем как дополнительную переменную в settings.py, переменная - ALLOWED_HOSTS = ['имя приложения на heroku']
- ещё раз коммитим изменения - git commit -m "deploy commit"
- пушим изменения командой git push
- деплоим приложение на heroku командой git push heroku master

------------------------------------------------

Функционал:
Доступно создание книг, авторов, издательств и должников.
Доступно редактирование должников на странице "Список должников", имя каждого должника - ссылка на его профиль.
При создании книги доступна загрузка обложки книги.
Рекомендуемый сценарий:
  - Создаём автора
  - Создаём издательство
  - Создаём книгу
  - Создаём должника и привязываем к нему книгу (книги).
  
Enjoy
