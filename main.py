from random import choice

name1 = input('First name: ')
name2 = input('Second name: ')
name3 = input('Third name: ')
name4 = input('Fourth name: ')

students = [name1, name2, name3, name4]
selected_student = choice(students)

print('The selected student is {}'.format(selected_student))
