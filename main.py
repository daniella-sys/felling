class Book:
    def __init__(self, title, author, years, famous):
        self.title = title
        self.author = author
        self.years = years
        self.famous = famous
#Виводемо інформацію
    def display_info(self):
        print(f"title: {self.title}, author: {self.author}, years: {self.years}, famous: {self.famous}")

#Створення самого класу з даними
book1 = Book("48 laws of power", "Robert Green", 2021, True)
book1.display_info()








