from pprint import pprint
class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'


    def get_products(self):
        file = open(self.__file_name, 'r')
        a = file.read()
        file.close()
        return a

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for i in products:
            if i.name in self.get_products():
                print(f'Продукт {i} уже есть в магазине')
            else:
                file.write(f'{i.name}, {i.weight}, {i.category}\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())