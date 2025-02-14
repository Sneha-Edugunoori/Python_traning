#incapsulation : is a process of protecting the data and functionality in a single unit , called an obj
#creating a basse cls
class Base:  #Parent cls
    def __init__(self):
        print("Parent cls constructor called")
        self.a = "Sneha"    #pubic data member
        self.__c = "Edugunoori"  #private data member

class Derived(Base):    #Child cls
         def __init__(self):
               Base.__init__(self)
               print("calling private member of base cls")
               print(self.a)
               print(self.__c) 

# obj1 = Derived()
# print(obj1.a)
# print(obj1.__c)
# obj2 = Base()
# print(obj2.__c)

#Private data member is *only* accessible inside the cls (they are strictly private)




class Rbi:
      #declaring public method
      def publicPolicy(self):
            print("cehck the public policy")

    #declaring private method
      def __privatePolicy(self):
            print("There is some private policy which is not accessible for public")

class Sbi(Rbi):
      def __init__(self):
            Rbi.__init__(self)


      def calingPublicMethod(self):
            print("\nInside child class")
            self.publicPolicy()

      def callingPrivateMehtod(self):
            self._privatePolicy()

obj1 = Sbi()
obj1.callingPrivateMehtod()
obj1.calingPublicMethod()
obj1.publicPolicy()
obj1.__privatePolicy()
obj2 = Rbi()
obj2.publicPolicy()
obj2.__privatePolicy()





