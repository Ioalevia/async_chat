"""Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с
информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для
этого:
a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар
(item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция
должна предусматривать запись данных в виде словаря в файл orders.json. При
записи данных указать величину отступа в 4 пробельных символа;
b. Проверить работу программы через вызов функции write_order_to_json() с передачей
в нее значений каждого параметра."""


import json


def write_order_to_json(item, quantity, price, buyer, date):

    with open('orders.json', 'r', encoding='UTF-8') as f_out:
        data = json.load(f_out)

    with open('orders.json', 'w', encoding='UTF-8') as f_in:
        orders_list = data['orders']
        order_info = {'item': item, 'quantity': quantity,
                      'price': price, 'buyer': buyer, 'date': date}
        orders_list.append(order_info)
        json.dump(data, f_in, indent=4, ensure_ascii=False)


write_order_to_json('mac', '100', '100', 'Mike', '12.12.2012')
write_order_to_json('intel', '150', '1000', 'Emma', '11.11.2011')
write_order_to_json('amd', '200', '900', 'Hill', '10.108.2010')
