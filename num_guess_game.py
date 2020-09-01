import random 


start = int(input("Start number : ")) #step3 : set guess range , and the range you can set between 1 to 1000
end = int(input("End number : ")) 
random = random.randint(start,end) 
count = 0

while True :
    num = int(input("Guess number : "))
    count += 1
    if num == random :
        print("Congratuaion !")
        print("you total guess" , count , "times" ) #step2 also
        break
    elif random > num and not (num>1000) :
        print("you must guess upper !")
    elif random < num and not (num>1000) :   
        print("you must guess lower !")
    elif num > 1000 or num < 0 :   
        print("not include the range !")
    else :
        print("error")
    print("you guess" , count , "times")  #step2 : set how many time you have guessed