import random 
student_ages = []
for i in range(100):
    student_ages.append(random.randint(10,65))
print (student_ages)
idx = 1
for student_age in student_ages:
    for i in range(idx , len(student_ages)):
        if student_age > student_ages[i]:
            temp = student_age
            student_ages[i - 1] = student_ages[i]
            student_ages[i] = temp
    idx += 1
print(student_ages)