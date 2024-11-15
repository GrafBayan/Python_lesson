class Car:

    def __init__(self, model, vin, number):
        self.model = model
        if self.__is_valid_vin(vin):
            self.vin = vin
        if self.__is_valid_numbers(number):
            self.numbers = number

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        elif vin_number not in range(1000000, 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, number):
        if not isinstance(number, str):
            raise IncorrectCarNumber('Некорректный тип данных для номеров')
        elif len(number) > 6:
            raise IncorrectCarNumbers('Неверная длина номера')


class IncorrectCarNumbers(Exception):
    def __init__(self, message, *args):
        self.message = message


class IncorrectVinNumber(Exception):
    def __init__(self, message, *args):
        self.message = message



try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')