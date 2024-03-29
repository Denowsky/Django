# Django
## Задание 1
Создайте три модели Django: клиент, товар и заказ.

Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

Поля модели «Клиент»:
* имя клиента
* электронная почта клиента
* номер телефона клиента
* адрес клиента
* дата регистрации клиента

Поля модели «Товар»:
* название товара
* описание товара
* цена товара
* количество товара
* дата добавления товара

Поля модели «Заказ»:
* связь с моделью «Клиент», указывает на клиента, сделавшего заказ
* связь с моделью «Товар», указывает на товары, входящие в заказ
* общая сумма заказа
* дата оформления заказа

Допишите несколько функций CRUD для работы с моделями по желанию.

## Задание 2
Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
* за последние 7 дней (неделю)
* за последние 30 дней (месяц)
* за последние 365 дней (год)

Товары в списке не должны повторяться.

## Задание 3
Создайте форму для редактирования товаров в базе
данных.
Измените модель продукта, добавьте поле для хранения
фотографии продукта.
Создайте форму, которая позволит сохранять фото.

## Задание 4
Создать суперюзера, выполнить вход в административную панель. Создать группы пользователей в соответствии с их функциями. Настроить вывод информации о клиентах, товарах и заказах.