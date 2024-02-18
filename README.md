# Django
## Задание (first/OnlineShop)
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