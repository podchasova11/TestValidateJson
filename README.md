# TestValidateJson
В проекте создать три файла: template.json, schema.json, и validate.py.
TestValidateJson/  
│  
├── template.json   # Файл с данными ответа сервера  
│  
├── schema.json     # Файл со схемой валидации  
│  
└── validate.py      # Файл с кодом для валидации  

В терминале выполните команду:
```
pip install jsonschema
```
____________________________

### Запуск кода
Выберите файл validate.py в проекте.
Нажмите правую кнопку мыши и выберите "Run 'validate'".
Результаты выполнения кода появятся в консоли внизу.

### Ожидаемый результат
Если данные в template.json соответствуют схеме в schema.json, вы увидите сообщение:
```
Валидация прошла успешно.
```
Если есть ошибки, они будут выведены в формате:
```
Ошибка валидации: <сообщение об ошибке>  
```
Готов рабочий проект в PyCharm для валидации JSON данных.
