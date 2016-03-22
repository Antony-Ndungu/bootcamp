#student1 dictionary
student1 = {
    'name': 'An Other',
    'langs': ['Python', 'JavaScript', 'PHP', "HTML"],
    'age': 23
}

#student2 dictionary
student2 ={
    'name': 'Antony',
    'langs': ['css', 'JavaScript', 'PHP', 'Python'],
    'age': 25
    }
    
#student3 dictionary
student3 = {
    'name': 'Ndungu',
    'langs': ['css', 'Java', 'PHP'],
    'age': 35
    }
    
#students are going to be added to this list using the function add_student(student)
list_of_students = []

#function add a student to list_of_students

def add_student(student):
    """Adds a student dictionary to a list of students
     @params student
     @return doesn't return anything"""
    list_of_students.append(student)
    
def oldest_student(list_of_students):
    """Finds the oldest student
    @params list_of_students
    @return the oldest student in the list_of_students
    """
    oldest = list_of_students[0]["age"]
    if(len(list_of_students) == 1):
        return list_of_student[0]
    else:
        for i in range(1, len(list_of_students)):
            if(oldest < list_of_students[i]["age"]):
               oldest = list_of_students[i]["age"]
        return list_of_students[i]
            



#student_lang() function definition
def student_lang(lang):
    """finds out names of students who know a particular language
    @params lang
    @returns list of students who know the language lang
    """
    list_know_lang = []
    for i in range(len(list_of_students)):
        for j in range(len(list_of_students[i]["langs"])):
            if(lang.lower() == list_of_students[i]["langs"][j].lower()):
                list_know_lang.append(list_of_students[i]["name"])
    return list_know_lang

#Testing the code
#Adding three students            
add_student(student1)
add_student(student2)
add_student(student3)

student = oldest_student(list_of_students)

print "Printing the oldest student"
print student
print ""

print "list of students who know Python:" 
print student_lang("Python")
print " "
print "list of students who know HTML:"
print student_lang("HTmL")
    
