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

