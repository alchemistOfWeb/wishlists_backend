# Adelya wishlists

course project

> «проектирование и реализация социальной платформы для обмена вишлистами и организации дарения».
> Это приложение где пользователь может регистрироваться, создавать свой список подарков и добавлять себе друзей(друзья , родственники, семья ), при заходе на страницу будет видно что выбрал другой человек,  также приложение может отравлять уведомления о предстоящих праздниках, и можно добавлять нужные даты самостоятельно.

## tasks

* [ ] nofifications
    * [ ] events
    * [ ] birthdays
    * [ ] custom events

* [ ] gift recommendations (with AI - mb openAI api - or some algorithms)
* [ ] my wishlist page
    * [ ] add wish {"product_name", "description", "rate"(насколько интересен подарок владельцу вишлиста), "tags"<->M2M, "expiration_date"(default: none)}
    * [ ] delete, update {"product_name", "description"}
    * [ ] patch: add tags
    * [ ] patch: set status ("is_gifted", "is_delivering", "is_archieved", "is_deleted") # если уже заказан и был внезапно удален или archieved, то об этом придет уведомление другу-заказчику; если gifted, то будет отображаться в отдельной секции видной всем; если archieved, то будет видно только владельцу вишлиста
    * [ ] 