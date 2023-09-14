class Student:
    __schoolName = 'XYZ School' #protected class atribute
    def __init__(self, name, age):
        self.__name = name #protected instance atribute
        self.__age=age

    def get_name(self):
        return self.__name