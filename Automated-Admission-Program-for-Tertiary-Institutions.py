#Create an admission program to calculate the aggregate score and tell the student the faculty and
#department he or she is likely to be admitted to.

#the following dictionary has the available faculties as keys, with a list of their departments as corresponding values

Faculties = {"Science": ["Applied Mathematics", "Computer Science", "Maths and Statistics", "Zoology", "Industrial Chemistry", "Geology"], 
    "Pharmacy": ["Pharmaceutics", "Industrial Pharmacy", "Pharmacology"],
    "Technology": ["Mechanical Engineering", "Production Engineering", "Architecture" "Electrical Engineering", "Computer Engineering"], 
    "Basic Medical Sciences": ["Medicine", "Anatomy", "Physiotherapy", "Psychiatry", "Human Nutrition", "Biochemistry", "Medical Laboratory Technology"], 
    "Law": ["Private and Business Law", "Islamic Law", "Public and International Law"], 
    "Agriculture and Forestry": ["Forest Management", "Anumal Science", "Agronomy", "Agricultural Economics"], 
    "Social Science": ["Economics", "Sociology", "Psychology", "Banking and Finance", "Business Administration"],
    "Education": ["Educational Management", "Teacher Education", "Adult Education", "Guidance and Counseling"]
}

#the python list, Subjects, holds a list of the secondary school subjects which candidates have taken
Subjects = {"Sciences": ["Maths", "English", "Biology", "Chemistry", "Physics"], 
"Arts": ["Maths", "English", "Religion", "Government", "Literature"], 
"Socio-economics": ["Maths", "English", "Geography", "Economics", "Commerce"]}

# this is an instruction to receive candidates' input of their subject combination
O_levelin = input("Kindly Choose your O Level subjects by typing: \n Science, Arts or Social Science \n")
# all entries rendered in lowercase, to cater for differences in user input
O_level = O_levelin.lower()

# ascertain that candidate inputs the right subject area
if O_level != "science" and O_level != "social science" and O_level != "arts":
    print("Kindly type in one from the above")

# compute total score from 5 relevant science subjects and express as percentage
aggregate = 0
if O_level == "science":
    for i in Subjects["Sciences"]:
        grades = int(input("Kindly input your marks in " + i + ": "))
        aggregate = aggregate + grades
    
    percentage = aggregate/5
    
    # this function will be called repeatedly to congratulate candidates and display their scores
    def welcome():
        print("\n Congratulations! You made a total of " + str(aggregate) + " marks")
        print("which amounts to " + str(percentage) + "%")
        print("You are qualified for admission to the following departments:\n")
    
    # check that candidate made the base-mark of 45%
    if percentage < 45:
        print("\n Sorry, your " + str(percentage) + "% score  does not meet the requirements for admission into any Faculty.\n")
    
    # the following instructions provide faculty and department recommendation to science students based on grades made
    elif percentage >= 80:
        welcome()
        print("\n FACULTY OF BASIC MEDICAL SCIENCES")
        for i in Faculties["Basic Medical Sciences"]:
            print(i)
        print("\n FACULTY OF PHARMACY")    
        for i in Faculties["Pharmacy"]:
            print(i)
        print("\n FACULTY OF TECHNOLOGY")
        for i in Faculties["Technology"]:
            print(i)
        print("\n FACULTY OF SCIENCES")
        for i in Faculties["Science"]:
            print(i)
            
    elif percentage < 80 and percentage >= 70:
        welcome()
        print("\n FACULTY OF PHARMACY")    
        for i in Faculties["Pharmacy"]:
            print(i)
        print("\n FACULTY OF TECHNOLOGY")
        for i in Faculties["Technology"]:
            print(i)
        print("\n FACULTY OF SCIENCES")
        for i in Faculties["Science"]:
            print(i)
            
    elif percentage < 70 and percentage >= 60:
        welcome()
        print("\n FACULTY OF TECHNOLOGY")
        for i in Faculties["Technology"]:
            print(i)
        print("\n FACULTY OF SCIENCES")
        for i in Faculties["Science"]:
            print(i)
            
    elif percentage < 60 and percentage >= 45:
        welcome()
        print("\n FACULTY OF SCIENCES")
        for i in Faculties["Science"]:
            print(i)
        print("\n FACULTY OF AGRICULTURE AND FORESTRY")
        for i in Faculties["Agriculture and Forestry"]:
            print(i)
            
# the following instructions provide faculty and department recommendation to social science students based on grades made
if O_level == "social science":
    for i in Subjects["Socio-economics"]:
        grades = int(input("Kindly input your marks in " + i + ": "))
        aggregate = aggregate + grades
    
    percentage = aggregate/5
    
    # this function will be called repeatedly to congratulate candidates and display their scores
    def welcome():
        print("\n Congratulations! You made a total of " + str(aggregate) + " marks")
        print("which amounts to " + str(percentage) + "%")
        print("You are qualified for admission to the following departments:\n")
    
    # check that candidate made the base-mark of 45%
    if percentage < 45:
        print("\n Sorry, your " + str(percentage) + "% score  does not meet the requirements for admission into any Faculty.\n")
    
    elif percentage >= 65:
        welcome()
        print("\n FACULTY OF SOCIAL SCIENCES")
        for i in Faculties["Social Science"]:
            print(i)
        print("\n FACULTY OF EDUCATION")    
        for i in Faculties["Education"]:
            print(i)
        print("\n FACULTY OF AGRICULTURE AND FORESTRY")
        for i in Faculties["Agriculture and Forestry"]:
            print(i)
            
    elif percentage < 65 and percentage >= 45:
        welcome()
        print("\n FACULTY OF EDUCATION")    
        for i in Faculties["Education"]:
            print(i)
        print("\n FACULTY OF AGRICULTURE AND FORESTRY")
        for i in Faculties["Agriculture and Forestry"]:
            print(i)
            
# the following instructions provide faculty and department recommendation to Arts students based on grades made
if O_level == "arts":
    for i in Subjects["Arts"]:
        grades = int(input("Kindly input your marks in " + i + ": "))
        aggregate = aggregate + grades
    
    percentage = aggregate/5
    
    # this function will be called repeatedly to congratulate candidates and display their scores
    def welcome():
        print("\n Congratulations! You made a total of " + str(aggregate) + " marks")
        print("which amounts to " + str(percentage) + "%")
        print("You are qualified for admission to the following departments:\n")
    
    # check that candidate made the base-mark of 45%
    if percentage < 45:
        print("\n Sorry, your " + str(percentage) + "% score  does not meet the requirements for admission into any Faculty.\n")
    
    elif percentage >= 70:
        welcome()
        print("\n FACULTY OF LAW")
        for i in Faculties["Law"]:
            print(i)
        print("\n FACULTY OF Education")    
        for i in Faculties["Education"]:
            print(i)
            
    elif percentage < 65 and percentage >= 45:
        welcome()
        print("\n FACULTY OF EDUCATION")    
        for i in Faculties["Education"]:
            print(i)
