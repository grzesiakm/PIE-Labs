import json
import random
from statistics import mean


def read_from_file(filename):
    data = None
    try:
        with open(filename, "r") as file:
            data = json.loads(file.read())
    except IOError:
        print("Problem with file")
        exit()
    return data

def write_into_file(filename, data):
    with open(filename, "w") as file:
        file.write(json.dumps(data, indent=4))

def create_a_class_diary():
    class_name = {
        'students': {},
        'subjects': {}
    }
    return class_name

def get_last_id(class_name):
    last = 0
    for auto_id in class_name['students'].keys():
        if last < auto_id:
            last = auto_id
    return last

def add_student(name, surname, class_name):
    auto_id = get_last_id(class_name) + 1
    student = {
        'id': auto_id,
        'name': name,
        'surname': surname,
        'grades': {},
        'attendance': {}
    }
    class_name['students'][auto_id] = student
    
def add_subject(class_name, subject_name):
    class_name['subjects'][subject_name] = []

def add_grade(student, subject_name, grade):
    student['grades'][subject_name].append(grade)

def enroll_student(class_name, student, subject_name):
    student['grades'][subject_name] = []
    student['attendance'][subject_name] = []
    add_subject(class_name, subject_name)
    class_name['subjects'][subject_name].append(student['id'])       
    student['attendance'][subject_name].append(random.randint(0, 1))
    
def check_full_attendance(class_name, subject_name):
    sum = 0
    for student in class_name['students']:
        if student['attendance'][subject_name] == 1:
            sum += 1
            
def display_student(class_name, id):
    return class_name['students'][str(id)]           
            
def mean_per_subject(class_name, subject_name):
    present = class_name['subjects'][subject_name]
    students = filter(lambda student: student['id'] in present, class_name['students'].values())
    grades = []
    for student in students:
        grades.extend(student['grades'][subject_name])
    sub_mean = round(mean(grades), 2)
    return "Mean of all students' grades in {} is {}".format(subject_name, sub_mean)

def mean_per_student(class_name, student):
    full_mean = []
    for subject_name in student['grades']:
        full_mean.append(mean(student['grades'][subject_name])) 
    full_mean = round(mean(full_mean), 2)
    return "Mean for {} {} = {}".format(student['name'], student['surname'], full_mean)

            
            
if __name__ == "__main__":
    diary_Ia = read_from_file('start_data.json')

    student = display_student(diary_Ia, 1)
    enroll_student(diary_Ia, student, 'Maths')
    add_grade(student, 'Maths', 4)
    
    print(student['grades'])
    print(mean_per_subject(diary_Ia, 'Maths'))
    for student in diary_Ia['students'].values():
        print(mean_per_student(diary_Ia, student))
    write_into_file('diary_Ia.json', diary_Ia)

