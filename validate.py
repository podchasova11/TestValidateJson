import json  
import jsonschema  
from jsonschema import validate  
from jsonschema.exceptions import ValidationError  

# Чтение файла template.json  
with open('template.json', 'r') as f:  
    data = json.load(f)  

# Чтение схемы из файла schema.json  
with open('schema.json', 'r') as f:  
    schema = json.load(f)  

# Функция для валидации  
def validate_data(data, schema):  
    try:  
        validate(instance=data, schema=schema)  
        print("Валидация прошла успешно.")  
    except ValidationError as e:  
        print("Ошибка валидации:", e.message)  

# Вызов функции валидации  
validate_data(data, schema)  
