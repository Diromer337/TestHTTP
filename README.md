# TestHTTP
## Запуск тестов
```
python3 -m pytest test.py
```
## Результат выполнения
![Результаты тестов](TestHTTP/test_res/Screenshot from 2020-03-15 16-25-28.png)
## Обнаруженные баги
В результате выполнения тестов и с помощью ручного тестирования были обнаружены следующие баги
1. Символ 'i' воспринимается сервером как символ '1'
  * Пример запроса
  ```
  {"string": "2i3"}
  ```
  * Ожидаемый результат
  ```
  {"number": 5}
  ```
  * Фактический результат
  ```
  {"number": 6}
  ```
2. 
