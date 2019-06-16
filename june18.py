# #*********ADD SUBTRACT MUTIPLY DIVIDE****************
#  a=int(input("enter 1st no."))
#  b=int(input("enter 2nd no."))
#  def add(num1 , num2):
#      sum=num1+num2
#      print(sum)
#  add(a,b)
#  def sub(num1 , num2):
#      minus=num1-num2
#      print(minus)
#  def mult(num1 , num2):
#      prdct=num1*num2
#      print(prdct)
#  def div(num1 , num2):
#      divide=num1/num2
#      print(divide)
#  sub(a,b)
#  mult(a,b)
#  div(a,b)
# #**********positioning in udf***********#
#  def my_pet(owner , pet):
#      print(owner,"is an owner of", pet)
#  my_pet(owner="john",pet="cat")
# #*********even\odd*********#
# def chk_num(number):
#     if number % 2 == 0:
#         print("number is even")
#     else:
#         print("number is odd")
# num = int(input("enter num"))
# chk_num(num)
#***************************8
def display_result(winner, score, **other_info):
    print("The winner was " + winner)
    print("The score was " + score)
    for key, value in other_info.items():
        print(key + ": " + value)
display_result(winner="Real Madrid", score="1-0",
overtime ="yes", injuries="none", test ="done")