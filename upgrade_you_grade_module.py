    # Each submitted task improves current grade by 0.5. Eg. 2 extra tasks improve grade B to A. 6 submitted tasks improve grade F to B.
    # In the case of non-integer numbers, round down, eg. 7 submitted tasks improve grade F to B.
possible_grades = ['A', 'B', 'C', 'D', 'E', 'F']

def tasks_str_to_int(tasks_list):
    #This function changes values of tasks_list form str to int.
    tasks_list_int =[]

    for i in tasks_list:
        int_i = int(i)
        tasks_list_int.append(int_i)

    return tasks_list_int

def upgrade_factor(tasks_list_int):
    # This function calculates a factor, by which grade is to be upgraded and creates a list with those values.
    upgrade_list =[]

    for i in tasks_list_int:
        grade_upgrade = int(i/2)
        upgrade_list.append(grade_upgrade)
    return upgrade_list

tasks_list_int = tasks_str_to_int(tasks_list)
factor_list = upgrade_factor(tasks_list_int)

def upgraded_grade(current_grades, factor):
    possible_grades = ['A', 'B', 'C', 'D', 'E', 'F']
    upgraded_grades=[]
    for grade, factor in zip(current_grades, factor):
        id_current_grade = possible_grades.index(grade)
        upgraded = possible_grades[id_current_grade - factor]
        upgraded_grades.append(upgraded)
    return upgraded_grades

upgraded_grades = upgraded_grade(current_grades, factor_list)

