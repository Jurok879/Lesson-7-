class Product:

# создаем конструктор для класса "Product"
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

# создаем метод для возвращения строкового значения в формате условия
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop(Product):

# создаем конструктор для дочернего класс "Shop"
    def __init__(self, name, weight, category, __file_name='products.txt'):
        super().__init__(name, weight, category)
        self.__file_name =  __file_name

# возвращаем в функцию данные, открытого файла
    def get_products(self):
        file = open(self.__file_name, 'r')
        pl = file.read()
        file.close()
        return f'{pl}'

# создаем метод для выполнения условий
    def add(self, *products):
        for i in products:
            dp = (str(i))
            file = open(self.__file_name, 'r')
            dl = file.read()
            file.close()
            if dp in dl:
                print(f'Продукт {dp} уже есть в магазине')
# добавляем данные в открытый файл, если их там нет
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{dp}\n')
                file.close()



s1 = Shop(str, float, str)
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
