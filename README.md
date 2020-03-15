# TestHTTP
## Запуск тестов
```
python3 -m pytest test.py
```
## Результат выполнения
![](https://github.com/Diromer337/TestHTTP/blob/master/test_res/test_res.png?raw=true)
## Обнаруженные баги
В результате выполнения тестов и с помощью ручного тестирования были обнаружены следующие баги
1. Символ 'i' воспринимается сервером как символ '1'
  - Пример запроса
  ```
  {"string": "2i3"}
  ```
  - Ожидаемый результат
  ```
  {"number": 5}
  ```
  - Фактический результат
  ```
  {"number": 6}
  ```
2. Символ '<' вызывает отключение от сервера
 - Пример запроса
  ```
  {"string": "32a>"}
  ```
  - Ожидаемый результат
  ```
  {"number": 5}
  ```
  - Фактический результат
  ```
  http.client.RemoteDisconnected: Remote end closed connection without response
  ```
