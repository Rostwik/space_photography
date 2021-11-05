## Описание

Программа запускает Telegram бота, который подключается к API NASA [Подробнее можно узнать здесь](https://api.nasa.gov/),
скачивает фотографии Земли, сохраняет в директорию "images" в корне проекта. Затем фотографии отправляются в определенную группу Telegram.
Процесс повторяется регулярно с задержкой, которую можно настроить (см.ниже).

## Требования к окружению

Для работы программы необходим установленный Python, pip.


## Как установить

Для корректной работы необходимо установить библиотеки.
Используйте pip для установки зависимостей:

```
pip install -r requirements.txt
```

## Как запустить программу

Необходимо создать файл .env в корне папки программы, и заполнить следующие параметры для подключения к бд:

NASA_API_TOKEN - токен API NASA
TELEGRAM_TOKEN - токен Telegram бота
DELAY_IN_SENDING - задержка между отправкой новой партии фотографий

Далее из консоли запустить программу:

```
python main.py
```
Затем зайти в Telegram бота и ввести команду:

```
/run_nasa
```

## Цель проекта

Автоматизировать работу администратора группы в Telegram.

