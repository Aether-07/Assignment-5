#Task 1
Mark_sheet = {
    'Alice':85,
    'Bob':78,
    'Charlie':83,
    'David':82,
    'Eve':76
}

name = input("Enter the student's name:")
if name in Mark_sheet:
    print(f"{name}'s marks:",Mark_sheet[name])
else:
    print('Student not found')

#Task 2
list = [1,2,3,4,5,6,7,8,9,10]
print('Original list:',list)
print('Extracted first five elements:',list[:5])
list.reverse()
print('Reversed extracted elements:',list[5:])