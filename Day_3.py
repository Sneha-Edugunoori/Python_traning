#instance variable depends on the state of the object

# class student:
#     def __init__(self):    #constructor
#         self.name = "Sneha"
#         self.roll = 19    #declaring a instance variable inside a constructor

#     def getdata(self):
#         self.s_mb = 1234567890  #declaring a instance variable inside a method

# obj = student() 
# obj.getdata()
# obj.s_branch = "CS"  #adding instance variable by using object
# print(obj.__dict__)
# print(obj.s_mb)
# del obj.roll
# print(obj.__dict__)





#static variable isn not dependent on object         ### we cannot use the static var using obj but can acess using *class name*
# class College:
#     collagename = "Apsit"  #static var(1 memory)
#     def __init__(self):
#         self.name = "Sneha" # instant var

# principal = College()   #object creation
# teacher = College()    #object creation
# accountant = College()    #object creation
# print("principle=",principal.collagename,".....",principal.name)
# print("teacher=",teacher.collagename,".....",teacher.name)
# print("accountant=",accountant.collagename,".....",accountant.name)  #access

# College.collagename = "Clg"    #second way to add static var
# principal.name  = "Raaajjj"

# print("principle=",principal.collagename,".....",principal.name)
# print("teacher=",teacher.collagename,".....",teacher.name)
# print("accountant=",accountant.collagename,".....",accountant.name)  #access



#where we can declare static var?
#inside a class but outside of method
#in a constructor by using a class name 
#in a instatnce method by using class name
#in a cls method by using cls var
#static method by using cls name

#How do we access statuc var?
#inside instance method using self or cls anme 
# in a constructor using self or cls name
# in a cls method using cls var or cls name
# inside a static method using obj or cls name
# outside the cls using obj or cls name 
#we can declare static mwthod using @staticmethod decorate


# how do we delete static var?
# del classname.Staticvariablename
# inside classmethod we can use cls variable: del cls:Staticvariablename


# class Student:
#     #by using cls name we can access static method
#     @staticmethod  #decorate
#     def getinfo(fname,lname):
#         print("fname=",fname,"lname=",lname)

#     @staticmethod
#     def contact_detail(mob,roll):
#         print("mob=",mob,"roll=",roll)

# Student.getinfo("Sneha","Edugunoori")
# Student.contact_detail(1234567890,12345)  #access static method using class nam

#Inheritance = extending a property from one cls to another cls 
#-base cls = a cls which inherits its prop
#-derived cls = a cls which extends prop from base cls

# types of inheritance:
# 1.Single level inheritance
# 2.Multi level inheritance
# 3.Multiple inheritance


#single lvl

# class College: #parent cls
#     def College_name(self):  #member func of clg
#       print("Apsit")

# class Student(College): #child cls
#     def student_info(self):  #member func of student
#         print("Name: Sneha")
#         print("Branch: ds")

# obj = Student() #obj create child cls
# obj.College_name()
# obj.student_info()



#multi lvl example
# class College:     #first cls first lvl
#     def college_name(self):
#         print("Apsit")


# class Student(College): #second cls second lvl
#     def student_info(self):
#         print("Name: Sneha")
#         print("Branch: ds")

# class Exam(Student): #child cls
#     def subject(self):
#         print("Maths,Science,Eng")

# obj = Exam() #obj create child cls
# obj.college_name()
# obj.student_info()
# obj.subject()





#multiple inheritance
# class A:
#     def displayA(self):
#         print("A class")
#         class B:
#             def displayB(self):
#                 print("B class")
#                 class C:
#                     def displayC(self):
#                         print("C class")
#                         obj = C()
#                         obj.displayC()
#                         obj = B()
#                         obj.displayB()
#                         obj = A()
#                         obj.displayA()
                    


#Abstraction
# a cls which contains one or more abtract method is called as abstract cls 
# METHOD that has declaration but does not have an implementation is called abstract method

# from abc import ABC , abstractmethod
# class Help4code(ABC):
#     @abstractmethod


#Polymorphism:
# 1. Method Overloading: It is a feature that allows you to define multiple methods with the same name but different parameters.

class operations:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(self,a)
    def add(self,a,b,c):
        print(self,a,b,c)
obj = operations()
obj.add(10)
obj.add(10,20)
obj.add(1,2,3)
# in py method overloading and constructor overloading does not support 
# 2. Method Overriding: It is a feature that allows you to override a method of a parent class in a child class.


class Rbi:
    def homeLoan_ROI(self):
        print("RBI Home Loan ROI is 7.5%")
        def carLoan_ROI(self):
            print("RBI Car Loan ROI is 8.5%")
class Sbi(Rbi):
    def homeLoan_ROI(self):
        print("SBI Home Loan ROI is 7.2%")
obj = Sbi() 
obj.homeLoan_ROI()
obj.carLoan()
























    
