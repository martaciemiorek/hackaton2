import csv

def open_csv():
    try:
        with open('1A.csv', 'r') as file:
            reader = csv.DictReader(file, dialect='excel')
            name_list =[]
            surname_list = []
            grade_list = []
            unsubmitted_tasks_list = []

            for row in reader:
                name_list.append(row['name'])
                surname_list.append(row['surname'])
                grade_list.append(row['grade'])
                unsubmitted_tasks_list.append(row['unsubmitted_tasks'])

    except UnicodeError:
        print("Wrong file encoding")

    return {
        'name_list': name_list,
        'surname_list': surname_list,
        'grade_list': grade_list,
        'unsubmitted_tasks_list': unsubmitted_tasks_list
            }


