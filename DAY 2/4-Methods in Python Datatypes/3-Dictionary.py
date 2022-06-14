
staff = {'staff_id':22,'name': "Rishiraj", 'age':35, 'is_married': False,'height':6.1}
print(staff)
print(staff['name'])


staff['is_married']=True
print(staff)

staff['children']=['Jenny','Ruku','Shova']
print(staff)

# print(staff['salary'])
print(staff.get('salary'))

print(staff.items())
print(staff.keys())
print(staff.values())

# staff.pop('height')

# clear, popitem, copy, update are some other methods that can be used