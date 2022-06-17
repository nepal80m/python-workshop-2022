staff = {
    'staff_id': 22,
    'name': 'Rishiraj',
    'age': 35,
    'is_married': True,
    'height': 6.1
}
print(staff)
print(staff['name'])  # to access value using keys
staff['age'] = 25
print(staff)
staff['children'] = ['monika', 'seeru', 'nirmala']
print(staff)
staff.pop('age')
print(staff)
staff.clear()
print(staff)
