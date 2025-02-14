import getpass

class MCQ:
    def __init__(self):
        self.no_questions = []
        self.questions = []
        self.option1 = []
        self.option2 = []
        self.option3 = []
        self.option4 = []
        self.correct = []
        self.score = 0
        self.no_of_correct_ans = 0
        self.no_of_wrong_ans = 0
        
    def user(self):
        print("***** Enter User Details *****")
        self.name = str(input("Enter Your Name : "))
        self.roll = int(input("Enter Your Roll No : "))
        
    def personal_deatils(self):
        print("***** Personal Details *****")
        print(f"Name of the student : {self.name}")
        print(f"Roll no : {self.roll}")
    
    def add_question(self):
        self.admin_user = input("Enter Admin User Name :")
        self.admin_pass = getpass.getpass("Enter Admin Password: ")
        if self.admin_user == self.admin_pass:
            self.no_questions = int(input("Enter Number of Questions you want to add : "))
            for i in range(int(self.no_questions)):
                print("=================================")
                self.questions.append(input("Enter Question : "))
                self.option1.append(input("Enter Option 1 : "))
                self.option2.append(input("Enter Option 2 : "))
                self.option3.append(input("Enter Option 3 : "))
                self.option4.append(input("Enter Option 4 : "))
                self.correct.append(input("Enter Correct Option (1/2/3/4) : "))
                print("=================================")
        else:
            print("Invalid Admin User Name or Password")

    def start_test(self):
            print("***** Start Test *****")
            for i in range((self.no_questions)):
                print("=================================")
                print(f"Question {i+1} : {self.questions[i]}")
                print(f"Option 1 : {self.option1[i]}")
                print(f"Option 2 : {self.option2[i]}")
                print(f"Option 3 : {self.option3[i]}")
                print(f"Option 4 : {self.option4[i]}")
                ans = int(input("Enter The Correct Option 1/2/3/4 : "))
                print("=================================")    
                if ans == int(self.correct[i]):
                    self.score += 10
                    self.no_of_correct_ans += 1
                else:
                    self.no_of_wrong_ans += 1
        
    def results(self):
        print("***** Results *****")
        print("=================================")
        print(f"Total Questions : {self.no_questions}")
        print(f"Total Score : {self.score}")
        print(f"No of Correct Answers : {self.no_of_correct_ans}")
        print(f"No of Wrong Answers : {self.no_of_wrong_ans}")
        print("=================================")


if __name__ == "__main__":
    mcq = MCQ()

    while True:
        print("\n***** Main Menu *****")
        print("1. Enter Details of Student")
        print("2. Display Student Details")
        print("3. Add Questions")
        print("4. Start Test")
        print("5. Results")
        print("6. Exit")
        choice = input("Enter Your Choice : ")

        if choice == "1":
            mcq.user()
        elif choice == "2":
            mcq.personal_deatils()
        elif choice == "3":
            mcq.add_question()
        elif choice == "4":
            mcq.start_test()
        elif choice == "5":
            mcq.results()
        elif choice == "6":
            print("Exiting... Thank you for using the Banking System.")
            break
        else:
            print("Invalid Option..... Try Again")