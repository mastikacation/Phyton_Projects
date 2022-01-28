print ("Welcome To my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print ("Okay, Lets Play!")
score = 0

answer = input( "What is monkeys favourite fruit? ")
if answer.lower() == "banana":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")

answer = input( "Which animal is king of the jungle? ")
if answer.lower() == "lion":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")

answer = input( "What is the name of first cloned animal? ")
if answer.lower() == "dolly":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")

answer = input( "Which animal can sense blood from kilometers away? ")
if answer.lower() == "shark":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")

answer = input( "Which wild species is famous for their laugh? ")
if answer.lower() == "hyenas":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")

answer = input( "What is the species of famous cartoon chracter Tom? ")
if answer.lower() == "cat":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")

answer = input( "Which animal is considered as a divine being in India? ")
if answer.lower() == "cow":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")

answer = input( "Which animal produces honey? ")
if answer.lower() == "bee":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")

answer = input( "Which animal's soup started the Covid-19 virus? ")
if answer.lower() == "bat":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")

answer = input( "Which kind of animal was Shrek's companion and best friend in the films? ")
if answer.lower() == "donkey":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")

print ("You got " + str(score) + " questions correct! ")
print ("You got " + str((score)/10 * 100) + "%. correct! ")