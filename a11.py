from abc import ABC, abstractmethod
class Operation(ABC):
    @abstractmethod
    def add(self,a,b):
        pass
    @abstractmethod
    def multiply(self,a,b):
        pass
class Addition(Operation):
    def add(self,a,b):
        return a+b
    def multiply(self,a,b):
        pass

class Multiplication(Operation):
    def add(self,a,b):
        pass
    def multiply(self,a,b):
        return a*b
a=Addition()
print("Addition Result:",a.add(5,3))
m=Multiplication()
print("Multiplication Result:",m.multiply(5,3))



# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#         print("This message is from the abstract class")
#         print("Area formula is different for each shape")

# class Circle(Shape):

#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius*self.radius
    
# c=Circle(5)
# #s=Shape(5)
# print("Area of Circle:",c.area())
# print("Area of Circle:",c.area())









# class Parent:
#     def __init__(self):
#         self.__secret="Parent Private Data"
#     def __private_method(self):
#         print("This is a private method in prent")
#     def show(self):
#         print(self.__secret)
    
# class Child(Parent):
#     def access_parent_private(self):
#         obj._Parent__private_method()
# obj=Child()
# obj.show()
# obj.access_parent_private()




# class Test:
#     def __init__(self):
#         self.__secret="Hidden Value"

# obj=Test()
# print(obj._Test__secret)








# class BankAccount:
#     def __init__(self,balance):
#         self.__balance=balance
#     def __secret_method(self):
#         print("This is a private method")
#     def show_balance(self):
#         return self.__balance
# acc=BankAccount(1000)
# print(acc.show_balance)
# print(acc.show_balance())
# print(acc._BankAccount__balance)


      


# class login:
#     def authenticate(self):
#         print("checking username & password")
# class Secure(login):
#     def authenticate(self):
#         super().authenticate()
#         print("Scanning fingurement")
# user=Secure()
# user.authenticate()








# class parent:
#     def luk(self):
#         print("hello world")
# class child(parent):
#     def van(self):
#         print("hello world")
# a=parent()
# b=child()

# a.luk()
# b.van()






# class Father:
#     def skills(self):
#         print("Father : cooking")
# class Mother:
#     def talents(self):
#         print("Mother: Editing")
# class child(Father, Mother):
#     def hoby(self):
#         print("Child : Painting")
# c=child()
# c.skills()
# c.talents()
# c.hoby()






# class Vehicle:
#     def move(self):
#         print("Vehicles help us travel from one place to another")
# class Car(Vehicle):
#     def fuel_type(self):
#         print("Car runs on petrol or diseal")
# class Electrical(Car):
#     def charge(self):
#         print("Electric car runs on battery and needs charging")
# tesla = Electrical()
# tesla.move()
# tesla.fuel_type()
# tesla.charge()









# class vehicle:
#     def __init__(self,brand):
#         self.brand=brand
# class car(vehicle):
#     def __init__(self,brand,model):
#         super().__init__(brand)
#         self.model=model
#     def display(self):
#         print(f"brand:{self.brand}, model:{self.model}")
# c=car("Toyata","Fortuner")
# c.display()





# class vehicle:
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color
#         print("vehicle initialized")
# class car(vehicle):
#         def __init__(self,brand,color,model):
#             super().__init__(brand,color)
#             self.model=model
#             print("car initialized")
# mycar=car("Land rover","Black","Defender")
# print(mycar.brand)
# print(mycar.model)
# print(mycar.color)







# class car:
#     def setenginemodel(self,engine):
#         self.engine=engine
#     def getenginemodel(self):
#         print(self.engine)
# class honda(car):
#     def setcarmodel(self,model):
#         self.model=model
#     def getcarmodel(self):
#         print(self.model)
# mycar=honda()
# mycar.setenginemodel("Land rover - EK-1")
# mycar.setcarmodel('Defender')
# print('car details')
# mycar.getenginemodel()
# mycar.getcarmodel()







# class House:
#     def set_address(self,house_address,street_number):
#         self.house_address= house_address
#         self.street_number= street_number
# class location(House):
#     def display_house_number(self):
#         print("House Address:",self.house_address)
#         print("Street Number:",self.street_number)
# luk=location()
# luk.set_address("Dudekula Street","12A")
# luk.display_house_number()





# class Vehicle :
#     def medium(self):
#         print("Mahindra Thar RoXX")
# class car(Vehicle):
#     def medium(self):
#         print("Land Rover Defender")

# D=car()
# D.medium()
# D.medium()








# class MathTool:
#     def add(self,*args):
#         return sum(args)
# tool=MathTool()
# print(tool.add(5))
# print(tool.add(5,10,))
# print(tool.add(5,10,15))




# class Area:
#     def findArea(self, a=None, b=None):
#         if a is not None and b is None :
#             print("Area of Square:", a * a)
#         elif a is not None and b is not None:
#             print("Area of Rectangle:", a * b)
       

# obj = Area()
# obj.findArea()
# obj.findArea(5)
# obj.findArea(5, 10)





# class MathTool:
#     def add(self,a=2,b=2,c=2):
#         return a+b+c
# tool=MathTool()
# print(tool.add(5))
# print(tool.add(5,10,))
# print(tool.add(5,10,15))






# class student:
#     def  __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def getMarks(self):
#         return self.marks
#     def setMarks(self, new_marks):
#         self.marks= new_marks 
# s1=student("Dudekula Arshad",1000)
# print("Befor update: ",s1.getMarks())
# s1.setMarks(1150)
# print("Afer updare: ",s1.getMarks())

    

# class car:
#     def setName(self,name):
#         self.name= name
#     def getName(self):
#         return self.name
# Honda = car()
# carname=input("Enter the car name: ")
# Honda.setName(carname)
# print("Car name: ", Honda.getName())






# from functools import reduce
# numbers=[1,2,3,4,5]
# result=reduce(lambda a,b:a+b,numbers,10)
# print(f"sum of numbers in a list = {result}")
#so in lambda function 10 is a initializer




# from functools import reduce
# numbers=[1,2,3,4,5]
# result=reduce(lambda a,b:a+b,numbers)
# print(f"sum of numbers in a list = {result}")



# class student:
#     def __init__(self,name,marks):
#         self.name =name
#         self.marks=marks
# s1=student("Arshad",{"Math":90,"Science": 95,"English":98})
# print(s1.name)
# print(s1.marks)

# class student:
#     def __init__(self,name,subjects):
#         self.name =name
#         self.subjects=subjects
# s1=student("Arshad",("Java","Python","c++",))
# print(s1.name)
# print(s1.subjects)

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def average(self):
#         return sum(self.marks)/ len(self.marks)
# s1=student("Arjun",[80,90,95])
# print(f"{s1.name}'s average marks:",s1.average())





# class student:
#     def __init__(self,name,marks):
#         self.name =name
#         self.marks=marks
# s1=student("Arshad",[90,95,98])
# print(s1.name)
# print(s1.marks)



# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# person1=person("Arjun",23)
# print(person1.name)
# print(person1.age)
# print("--------------")
# person2=person("Charna Teja",22)
# print(person2.name)
# print(person2.age)
# print("--------------")
# person3=person("Arshad",21)
# print(person3.name)
# print(person3.age)
# print("--------------")


# class car:
#     def __init__(self,new):
#         self.new= new
# my_car=car("Mahindra Thar ROXX")
# your_car=car("Defender")
# print(my_car.new)
# print(your_car.new)

