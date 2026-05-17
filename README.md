# Adelya wishlists

course project

> «проектирование и реализация социальной платформы для обмена вишлистами и организации дарения».
> Это приложение где пользователь может регистрироваться, создавать свой список подарков и добавлять себе друзей(друзья , родственники, семья ), при заходе на страницу будет видно что выбрал другой человек,  также приложение может отравлять уведомления о предстоящих праздниках, и можно добавлять нужные даты самостоятельно.

## tasks


* [ ] nofifications (celery, telegram, gmail, app) - тут нужно написать скрипт который будет запускаться в селери каждый час и проверять (видимо проходясь по каждому пользователю) есть ли актуальные для данного пользователя события в ближайшие 30 дней
    * [ ] events
    * [ ] birthdays
    * [ ] custom events

* [x] my wishlist page
* [x] friend's page
* [x] auth system (API JWT)
* [x] friends
* [ ] gift recommendations (with AI - mb openAI api - or some algorithms)
    * [ ] get: list of recommendations with pagination
* [ ] goods - можно посмотреть какие товары выбирают другие и добавить копию в свой вишлист
    * [ ] get: list of products with pagination


## run

Установка зависимостей
```bash
poetry install
```

❗ Запуск всего приложения
```bash
docker-compose up -d
```

Для миграций
создание (при разработке)
```bash
docker-compose exec app alembic revision --autogenerate -m "some msg"
```


❗ выполение
```bash
docker-compose exec app alembic upgrade head
```

❗ Для заполнения бд базовыми записями 
```bash
poetry run python -m app.db.seed
# or
docker-compose exec app python -m app.db.seed
```

При обновлении кода, добавлении новых зависимостей и т.д.
```bash
docker-compose up --build
```

