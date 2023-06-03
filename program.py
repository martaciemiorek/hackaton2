from open_csv_module import open_csv
from upgrade_you_grade_module import upgraded_grade
from message_module import create_message


def main():
    data = open_csv('1A.csv')
    current_grades = data['grade_list']
    unsubmitted_tasks = data['unsubmitted_tasks_list']
    factor_list = upgrade_factor(unsubmitted_tasks)
    upgraded_grades = upgraded_grade(current_grades, factor_list)
    data['grade_list'] = upgraded_grades
    create_message(data)

if __name__ == "__main__":
    main()