# try:
#     a=int(input("Enter first integer no."))
#     b=int(input("Enter second integer no."))
#     print(a/b)
#     #default except block should be in the end 

# except(ValueError,ZeroDivisionError) as message:
#     print("Error: ",message)

# except:       #default except block
#     print("An error occurred")
#             #or
# else:
#     print("No exception occurred")
# finally:
#     print("This block will always execute")



# try:
#     a=int(input("Enter first integer no."))
#     b=int(input("Enter second integer no."))
#     try:
#         print(a/b)
#     except ZeroDivisionError as msg:
#         print(msg)
# except ValueError as msg:
#         print(msg)



#File handling
#use when we want to store permanent data on hard disck for future purpose, file handling is used to read and write data from file

# f = open("myfile.txt","w")  # w = write mode (opens files in write mode, also creates file if not exists)
# print("Name of file",f.name)
# print("file mode",f.mode)
# print("readble",f.readable())
# print("writable",f.writable())
# print("file has colsed:",f.closed)
# f.close()
# print("File has closed", f.closed)



# f = open("myfile.txt", "r")
# print(f.read())


#overwrite the data
# f = open("myfile.txt", "w")
# f.write("Hello, world!\n")
# f.close()


#append
# for _ in range (3):
# f = open("myfile.txt", "a")
# f.write("Heyyyyyyyy!")


# f = open("covid.txt","w")
# mylist = ["Sneha","\n","Chinuu"]
# f.writelines(mylist)
# f.close()
# print("Written work has done succesfully")

#with statement
#with statement is used to open file, it automatically closes the file 
# with open("myfile.txt","w") as f:
#     f.write("Hello, world!")
#     f.write("Hello, Sneha!")
#     f.write("Hello, Chinuu!")
#     print("File has closed")
#     print("File closed",f.closed) 
# print("File closed",f.closed) 

   
# with open("myfile.txt","r") as f:
#     mylist = []
#     for line in f:
#      mylist.append(line)
#      print(mylist)  # print the list




#CSV
# import csv
# f = open("Student.csv","a",newline="") 
# a = csv.writer(f)  #writerfunc = returns a writable obj
# a.writerow(["StudentID","RollNo","Name"])
# studentId = int(input("Enter student ID:"))
# rollNo = int(input("Enter roll no:"))
# name = input("Enter name:")
# a.writerow([studentId,rollNo,name])




#Students Result
# import csv
# f = open("ApsitInfo.csv","a",newline="")
# a = csv.writer(f)
# a.writerow(["Id","Name","Email","MobileNo","p1","p2","p3","p4,""p5","ToatalMarks","%","Grade"])
# Id = int(input("Enter ur Id:"))
# Name = input("Enter ur Name:")
# Email = input("Enter ur Email:")
# MobileNo = input("Enter ur MobileNo:")
# p1 = int(input("Enter p1:"))
# p2 = int(input("Enter p2:"))
# p3 = int(input("Enter p3:"))
# p4 = int(input("Enter p4:"))
# p5 = int(input("Enter p5:"))
# TotalMarks = p1 + p2 + p3 + p4 + p5
# percentage = (TotalMarks/500)*100
# if percentage >= 90:
#     grade = "A"
# elif percentage >= 80:
#  grade = "B"
# elif percentage >= 70:
#    grade = "C"
# elif percentage >= 60:
#    grade = "D"
# else:
#  grade = "F"
# a.writerow([Id,Name,Email,MobileNo,p1,p2,p3,p4,p5,TotalMarks,percentage,grade])
# # f.close()  # close the file

    

# import csv
# f1 = open("img.png","rb")
# data = f1.read()
# f2 = open("image.png","wb")
# f2.write(data)



#what is pickling?
# Pickling is a process in Python where we can convert an object into a byte stream. 
#dump method = it is used to pickle the obj 
#load method = it is used to unpickle the obj



#logging with python
# import logging
# logging.basicConfig(filename="newfile.txt",level=logging.DEBUG)
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")


# import logging

# logging.basicConfig(filenam= "newfile.txt",level=logging.DEBUG)

# try:
#     a= int(input("Enter a integer:"))
#     b = int(input("Enter a integer:"))
#     print(a/b)
# except ZeroDivisionError as msg:
#     print(msg)
#     logging.error("div by zero")