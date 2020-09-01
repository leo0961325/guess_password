password = "python"
guess = ""
guess_count = 0 
guess_limited = 3
out_of_guess = False


while guess != password and not (out_of_guess) :
    if guess_count < guess_limited:
        guess = input("enter the password : ")
        guess_count += 1
    else :
        out_of_guess = True


if out_of_guess : 
    print("you wrong")
else :
    print("you got it !")

