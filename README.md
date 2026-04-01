# Adelya wishlists

course project

> «проектирование и реализация социальной платформы для обмена вишлистами и организации дарения».
> Это приложение где пользователь может регистрироваться, создавать свой список подарков и добавлять себе друзей(друзья , родственники, семья ), при заходе на страницу будет видно что выбрал другой человек,  также приложение может отравлять уведомления о предстоящих праздниках, и можно добавлять нужные даты самостоятельно.

## tasks


* [ ] nofifications (celery, telegram, gmail) - тут нужно написать скрипт который будет запускаться в селери каждый час и проверять (видимо проходясь по каждому пользователю) есть ли актуальные для данного пользователя события в ближайшие 30 дней
    * [ ] events
    * [ ] birthdays
    * [ ] custom events

* my wishlist page
    * [x] get: list of wishlist items
        * [x] need to display tags also - Для запроса на список items в вишлисте нужно добавить поле тегов в ответе в теле каждого item
    * [x] post: create wish {"product_name", "description", "rate"(насколько интересен подарок владельцу вишлиста), "tags"<->M2M, "expiration_date"(default: none)}
    * [x] delete: completely delete product, 
    * [x] post: update {"product_name", "description", add tags, set status}
    * [x] patch: add tags
    * [x] patch: set status ("is_gifted", "is_delivering", "is_archieved", "is_deleted") # если уже заказан и был внезапно удален или archieved, то об этом придет уведомление другу-заказчику; если gifted, то будет отображаться в отдельной секции видной всем; если archieved, то будет видно только владельцу вишлиста
* friend's wishlist page
    * [x] get: pruduct ordered (отмечаем подарок как уже заказанный, чтобы другие пользователи видели, но не сам friend)
    * subscribe or accept (см. пункт firends)
* auth system (API JWT)
    * [x] post: sign up
    * [x] post: sign in
    * [x] post: sign out
* friends
    * [x] delete: (удалить запись промежуточной таблицы friendship)
    * [x] post: add or accept (создать или обновить (если друг уже подписан на вас) запись промежуточной таблицы friendship)
* [ ] gift recommendations (with AI - mb openAI api - or some algorithms)
    * [ ] get: list of recommendations with pagination
* [ ] goods - можно посмотреть какие товары выбирают другие и добавить копию в свой вишлист
    * [ ] get: list of products with pagination


## run

Установка зависимостей
```bash
poetry install
```

Запуск всего приложения
```bash
docker-compose up -d
```

Для миграций
```bash
docker-compose exec app alembic revision --autogenerate -m "init"
docker-compose exec app alembic upgrade head
```

При обновлении кода, добавлении новых зависимостей и т.д.
```bash
docker-compose up --build
```

# file structure

Главная папка с кодом:

```bash
app/
├── api/
│   ├── __init__.py
│   ├── auth.py
│   └── users.py
│
├── constants/
│   └── auth.py
│
├── core/
│   ├── config.py
│   └── security.py
│
├── db/
│   ├── base.py
│   └── session.py
│
├── dependencies/
│   └── auth.py
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── wishlist.py
│   ├── wish_item.py
│   ├── friendship.py
│   ├── event.py
│   └── notification.py
│
├── schemas/
│   ├── __init__.py
│   └── auth.py
│
├── services/
│   ├── __init__.py
│   └── auth.py
│
└── main.py
```



Для системы авторизации:
```bash
app/
 ├── api/
 │   └── auth.py
 ├── core/
 │   └── security.py
 ├── constants/
 │   └── auth.py
 ├── models/
 │   └── user.py
 ├── schemas/
 │   └── auth.py
 ├── services/
 │   └── auth.py
 └── dependencies/
     └── auth.py
```


Смотри, я могу следующие пять разделов сделать 
1. Описание проекта в целом: 
Диаграмма вариантов использования, общая диаграмма компонентов всего приложения (т.е. как отедльные части бек, фронтенд и бд взаимодействуют), Развертывание приложения.
2. проектирование и разработка базы данных с применением технологии ORM:
Описание моделей, ER Диаграмма
3. разработка серверной части (FastAPI)
4. Клиентская часть (React, typescript, vite, bootstrap)
