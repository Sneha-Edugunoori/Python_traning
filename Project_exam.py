#from engineering.first_year.first_sem import f2_sem
#from Engineering.MCA.first_sem import first_subj
#from engineering.MCA.second_sem import second_subj
# importing modules from packages like subject name
choice =0 # global variable
class Exam(object):
    def __init__(self):
        self.sname=None
        self.collegename=0
        self.classname = 0
        self.rollno =0
        self.login()# calling function
        
    def login(self):# constructor part (called function)
            print("=========================")

            username=input("Enter username")
            password=input("Enter password")

            print("=========================")
            print()
            # Login section
            if username==password:
                print("Login successfully")
                self.getdata() # calling function
            else:
                print("Login fail try again")
 #=============================================================
    print()
    #Enter Your Profile Detail
    def getdata(self):
        self.sname      = input("Enter Your Name")
        self.collegename= input("Enter Your College Name")
        self.classname  = input("Enter Your Class Name")
        self.rollno     = input("Enter Your Roll Number")
        print()
        #====================End Of Profile Section========================
        # static subject declartion
        print(" choose any branch for giving exam")
        print("1. Mechanical Egineering")
        print("2. Information Technology")
        print("3. Computer Science")
        print("4. Civil Engineering")
        print()

        choice = int(input("Enter your choice")) # subject selection logic part
        if choice==1:
            self.mechanical() # calling function
        elif choice==2:
            pass
        elif choice==3:
            pass
        elif choice==4:
            pass
        else:
            print("you have entered wrong choice")

        # called function part
    def mechanical(self):
        print("1. First Semester")
        print("2. Second Semester")
        print("Enter your Semester Number")
        # logical part
        choice =int(input("Enter your choice"))
        if choice == 1:
            #first_subj()  # calling function
            print("Math")
        elif choice== 2:
            pass #second_subj()

    def information(self):
        print("1. First Semester")
        print("2. Second Semester")
        choice =int(input("Enter your choice"))
        if choice == 1:
            pass
        elif choice== 2:
            pass

    def computer(self):
        print("1. First Semester")
        print("2. Second Semester")
        choice =input("Enter your choice")
        if choice == 1:
            pass
        elif choice== 2:
            pass

    def civil(self):
        print("1. First Semister")
        print("2. Second Semister")
        choice =input("Enter your choice")
        if choice == 1:
            pass
        elif choice== 2:
            pass

#object creation of class
#obj = Exam()
#obj.login()
#==================================================end=========================
# Examination Calculation part
class Calculation(object):
    def __init__(self):
        self.stat=0
        self.dmgt=0
        self.cg =0
        self.toc =0
        self.math=0
        self.total=0
        self.percentage=0
        self.ps = 0
        print()
        print("Do You Want To Put Examination Marks Enter Yes/No")
        print()
        Yes = input("Enter yes/no")
        if Yes == "yes":
            self.calculatemarks() # calling function
        else:
            print("Thank You For Visiting Here")
        print()
# taking a marks for subject
    def calculatemarks(self):                 
        self.stat = int(input("Enter Marks Of Statistics:"))
        self.dmgt = int(input("Enter Marks Of DMGT :"))
        self.cg   = int(input("Enter Marks Of CG   :"))
        self.toc  = int(input("Enter Marks Of TOC  :"))
        self.math = int(input("Enter Marks Of Math1:"))
        print()

        if self.stat >=40 and self.dmgt>=40 and self.cg>=40 and self.toc>=40 and self.math>=40:
            self.ps="pass"
            print("You are pass")
        else:
            self.ps="Fail"
            print("You are fail")
            
        self.total = self.stat+self.dmgt+self.cg+self.toc+self.math
        self.percentage = self.total/5.0


#obj1 = Calculation()    
#================================================================================

#Assesment class

class Assesment(Exam, Calculation): # multiple inheritance

    def __init__(self):    # child class constructor
        Exam.__init__(self)     # calling parent class constructor
        Calculation.__init__(self)

    def result(self):
        
        print("===============================================================")
        print("                                                               ")
        print("         College Name: ",self.collegename ,"                   ")
        print("                                                               ")
        print("===============================================================")

        print("|        Student Name: ",self.sname,  "                       |")
        print("|        Class Name  : ",self.classname,"                     |")
        print("|        Roll No     : ",self.rollno,      "                  |")
        print("===============================================================")
        print("                                                               ")
        print(" Subject Name     :     Total Marks    :  Obtained Marks :     ")                
        print("                                                               ")
        print(" Statistic        :",   "   100   "   "      :",  self.stat,  ":")
        print(" DMGT             :",   "   100   "   "      :",  self.dmgt,  ":")
        print(" CG               :",   "   100   "   "      :",  self.cg,    ":")
        print(" TOC              :",   "   100   "   "      :",  self.toc,   ":")
        print(" Math             :",   "   100   "   "      :",  self.math , ":")
        print("===============================================================")
        print("                                                               ")
        print("Result Status     :",                              self.ps,"   ")
        print("Total Marks       :",      "500",                           "  ")
        print("Obtained Marks    :",                          self.total,      )
        print("Percentage        :",      self.percentage,               "    ")
        print("===============================================================")

obj2 = Assesment()
obj2.result()
