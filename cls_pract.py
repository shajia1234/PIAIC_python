days = ["monday" , "Tuesday" , "wednesday" , "thursday" , "friday" , "Sunday"]
for day in days:
    if day == "Sunday":
        print("It's holiday")
    else:
        print("It's working day")
element = days[2:4]
print(element)
a = days.pop()
print(a)
b = days.pop()
print(b)
names = ('python' , 'c++' , 'java')
print(names)
#names.append('pi')
#elements = names[0:2]
print(names[1:3])
names = list(names)
names[0] = 'java'
#print(names)
names = tuple(names)
#print(names)