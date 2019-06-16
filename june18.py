 a=int(input("enter 1st no."))
 b=int(input("enter 2nd no."))
 def add(num1 , num2):
     sum=num1+num2
     print(sum)
 add(a,b)
 def sub(num1 , num2):
     minus=num1-num2
     print(minus)
 def mult(num1 , num2):
     prdct=num1*num2
     print(prdct)
 def div(num1 , num2):
     divide=num1/num2
     print(divide)
 sub(a,b)
 mult(a,b)
 div(a,b)
 def my_pet(owner , pet):
     print(owner,"is an owner of", pet)
 my_pet(owner="john",pet="cat")
def chk_num(number):
    if number % 2 == 0:
        print("number is even")
    else:
        print("number is odd")
num = int(input("enter num"))
chk_num(num)
