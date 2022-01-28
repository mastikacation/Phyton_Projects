name = input("Type your name: ")
print("Good Morning", name , "you are finally awake")

answer = input(
    "Its already 9 AM and your alarm is ringing. You are late to work and you are stinking are you gonna take a shower? (yes/no)? ").lower()
if answer == "yes":

    answer = input ("You left home after taking a shower. While going to work you saw a patisserie on street and your stomach is rumbling. Do you want to enter and buy breakfast? (yes/no) ").lower()

    if answer == "yes":
        print("You bought breakfast for yourself and your coworkers as an apolagize for being late. Everyone is happy good job! You won the game")
        quit()

    elif answer == "no":
        
        print("You went to work directly and your boss got mad at you for being late. You are fired good luck at finding a job! ^^ ")
    
    else:
        
        print("Not a valid option. You lose. ")


elif answer == "no":
    print("You went to work late while stinking, your boss is mad at you. You are fired good luck at finding a job! ^^ ")

else:
    print("Not a valid option. You lose. ")

print("Nice try", name)
