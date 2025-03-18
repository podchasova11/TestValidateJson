# import json
#
# import data
# import jsonschema
# from jsonschema import validate
# from jsonschema.exceptions import ValidationError
#
# # Чтение файла template.json
# with open('template.json', 'r') as f:
#     data = json.load(f)
#
# # Чтение схемы из файла schema.json
# with open('schema.json', 'r') as f:
#     schema = json.load(f)
#
#
# # Функция для валидации
# def validate_data(data, schema):
#     try:
#         validate(instance=data, schema=schema)
#         print("Валидация прошла успешно.")
#     except ValidationError as e:
#         print("Ошибка валидации:", e.message)
#
#
# # Вызов функции валидации
# validate_data(data, schema)


# Функция для валидации с накоплением ошибок
# import json
# import jsonschema
# from jsonschema import validate
# from jsonschema.exceptions import ValidationError
#
# # Пример схемы
# schema = {
#     "type": "object",
#     "properties": {
#         "vehicles": {
#             "type": "array",
#             "minItems": 1,
#             "items": {
#                 "type": "object",
#                 "properties": {
#                     "gosNumber": {
#                         "type": "string"
#                     },
#                     "depotNumber": {
#                         "type": "integer"
#                     },
#                     "is_active": {
#                         "type": "boolean"
#                     }
#                 },
#                 "required": ["gosNumber", "depotNumber", "is_active"]
#             }
#         }
#     },
#     "required": ["vehicles"]
# }
#
# # Пример данных для валидации (с двумя ошибками)
# data = {
#     "vehicles": [
#         {
#             "gosNumber": "string1",
#             "depotNumber": "123",  # Неправильный тип, это строка
#             "is_active": True
#         },
#         {
#             "gosNumber": "string2",
#             "is_active": None  # Неправильный тип, должен быть boolean
#         }
#     ]
# }
#
#
# # Функция для валидации с накоплением ошибок
# def validate_data(data, schema):
#     errors = []
#
#     # Проверка наличия массива "vehicles"
#     if "vehicles" not in data:
#         errors.append("Ошибка: отсутствует поле 'vehicles'.")
#     else:
#         # Проверка валидации для каждого элемента массива "vehicles"
#         for index, vehicle in enumerate(data["vehicles"]):
#             try:
#                 validate(instance=vehicle, schema=schema["properties"]["vehicles"]["items"])
#             except ValidationError as e:
#                 errors.append(f"Ошибка в элементе {index + 1}: {e.message}")
#
#     if errors:
#         print("Ошибки валидации:")
#         for error in errors:
#             print(f" - {error}")
#     else:
#         print("Данные корректные.")
#
#
# # Вызов функции валидации
# validate_data(data, schema)

