password = "mikoduck"
chance = 3
while True :
    guess = input ("Please enter your password :")
    if guess == password :
        print("You got it !")
        break
    else :
        chance = chance -1
        print("you wrong !" , "you have" , chance , "chance")
        if chance == 0 :
            break