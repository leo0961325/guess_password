import random 

random = random.randint(1,100)

while True :
    num = int(input("Guess number : "))
    if num == random :
        print("Congratuaion !")
        break
    elif random > num and not (num>100) :
        print("you must guess upper !")
    elif random < num and not (num>100) :
        print("you must guess lower !")
    elif num > 100 or num < 0 :
        print("not include the range !")
    else :
        print("error")