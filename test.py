class Backpack():

    def __init__(self, gift = None):
        self.items = []
        if gift:
            self.items.append(gift)

    def movetobackpack(self, item):
        '''Move item to our backpack'''
        self.items.append(item)
        print(f'В рюкзак положили {item}')

    def __str__(self):
        '''Пробуем переопределить строковой метод'''
        return 'Нихуя себе, получилось!' + str(self.items)


my_backpack = Backpack('Телефон')
print(my_backpack)
