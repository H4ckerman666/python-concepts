class Person():
    def __init__(self, name, surname, alias="Without Alias"):
        self.alias = alias
        #! private attribute with __ 
        self.__name = name
        self.__surname = surname

    def get_name(self):
        return self.__name


me = Person("Yisus", "Robles", "H4ckerman666")
print(me.alias)
print(me.get_name())
