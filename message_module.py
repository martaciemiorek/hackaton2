from upgrade_you_grade_module import upgraded_grade

def create_message(imported_data):
    name_list = imported_data['name_list']
    surname_list = imported_data['surname_list']
    grade_list = imported_data['grade_list']
    unsubmitted_tasks_list = imported_data["unsubmitted_tasks_list"]

    upgraded_grades = upgraded_grade(grade_list, unsubmitted_tasks_list)

    for name, surname, grade, unsubmitted_tasks, upgraded_grades in zip(name_list, surname_list, grade_list, unsubmitted_tasks_list, upgraded_grades):
        txt = (f'Dear {name} {surname} your current grade is {grade}. You still need to submitt {unsubmitted_tasks} tasks, which can improve your grade yo {upgraded_grades}.')
        print(txt)
