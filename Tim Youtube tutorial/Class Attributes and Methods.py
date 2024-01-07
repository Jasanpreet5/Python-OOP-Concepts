class Person:
    number_of_people = 0      # this is class attribute
    GRAVITY = -9.8
    
    def __init__(self, name):
        self.name = name
        # Person.number_of_people += 1
        Person.add_person()    # calling the class method
        
    @classmethod         # this is class method common to all objects or instances of class Person
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cl):
        cl.number_of_people += 1
        
p1 = Person("Tim")
print(Person.number_of_people)
p2 = Person("jill")
print(Person.number_of_people)

print(Person.number_of_people_())        # Using class method