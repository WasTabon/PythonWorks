import csv
import statistics

header = ['Ім\'я', 'Прізвище', 'Вік', 'Спеціальність']

with open('students.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)

students_data = [
    ['Іван', 'Бобов', 22, 'Інформатика'],
    ['Олена', 'Бобова', 20, 'Математика'],
    ['Павло', 'Бобов', 25, 'Фізика'],
    ['Наталія', 'Бобова', 19, 'Хімія'],
    ['Андрій', 'НеБобов', 21, 'Біологія']
]

with open('students.csv', 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(students_data)

with open('students.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(', '.join(row))

with open('students.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    print('\nСтуденти старші 20 років:')
    for row in csvreader:
        name, surname, age, specialty = row
        if int(age) > 20:
            print(f'{name} {surname}, {age} років, {specialty}')

updated_specialty = 'обчислювальна техніка'
with open('students.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    rows = list(csvreader)

rows[1][3] = updated_specialty

with open('students.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)

with open('students.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    rows = list(csvreader)

del rows[2]

with open('students.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)

with open('students.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    rows = list(csvreader)
    header = rows[0]
    sorted_rows = sorted(rows[1:], key=lambda x: int(x[2]))

with open('students.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(sorted_rows)

age_by_specialty = {}
with open('students.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        _, _, age, specialty = row
        age_by_specialty.setdefault(specialty, []).append(int(age))

for specialty, ages in age_by_specialty.items():
    average_age = statistics.mean(ages)
    print(f'\nСередній вік студентів спеціальності "{specialty}": {average_age:.2f} років')
