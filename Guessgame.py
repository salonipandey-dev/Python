import random 
num=random.randint(1,10)
print(num)
guess =int(input("please guess your number between 1 and 10"))

if num == guess:
    print("you are right")

else:
    print("try again , cutiee")
