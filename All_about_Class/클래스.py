class Person:
    def __init__(self,name,age):
        self.name=name
        self.age = age 

    def get_name(self):
        print("제 이름은", (self.name), "입니다")
    
    def get_age(self):
        print("제 나이는", (self.age),"입니다")



A = Person('Kim',25)
A.get_name()
A.get_age()
