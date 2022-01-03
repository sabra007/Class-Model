class Animal: 
    """Animal Class"""
    def __init__(self, animal_type):
        print(f'Animal {animal_type} was created.')
        self.__animal_type = animal_type
        self.__weight = 0.1
        self.__color = "transparent"

    @property
    def animal_type(self):
        return self.__animal_type

    @property
    def weight(self):
        return self.__weight

    @property
    def color(self):
        return self.__color

    @animal_type.setter
    def animal_type(self, new_animal_type):
       self.__animal_type = new_animal_type
    
    @weight.setter
    def weight(self, new_weight):
       self.__weight = new_weight

    @color.setter
    def color(self, new_color):
       self.__color = new_color



class Book:
    """Book class"""
    def __init__(self, title):
        self.__title = title
        self.__author = 'tbd'
        self.__publisher = "tbd"
        self.__year = 2022
        self.__price = 0.0

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def publisher(self):
        return self.__publisher

    @property
    def year(self):
        return self.__year

    @property
    def price(self):
        return self.__price


    @title.setter
    def title(self, new_title):
       self.__title = new_title
    
    @author.setter
    def author(self, new_author):
       self.__author = new_author
    
    @publisher.setter
    def publisher(self, new_publisher):
       self.__publisher = new_publisher

    @year.setter
    def year(self, new_year):
       self.__year = new_year

    @price.setter
    def price(self, new_price):
       self.__price = new_price



class Vehicle:
    """Vehicle class"""
    def __init__(self):
        self.__make = 'make'
        self.__model = 'model'
        self.__trim = "trim"
        self.__year = 2022
        self.__color = 'color'

    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def trim(self):
        return self.__trim

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color


    @make.setter
    def make(self, new_make):
       self.__make = new_make
    
    @model.setter
    def model(self, new_model):
       self.__model = new_model
    
    @trim.setter
    def trim(self, new_trim):
       self.__trim = new_trim

    @year.setter
    def year(self, new_year):
       self.__year = new_year

    @color.setter
    def color(self, new_color):
       self.__color = new_color


