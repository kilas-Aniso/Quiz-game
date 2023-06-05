print("Welcome to my quiz")


playing = input("DO you want to play ")
if playing.lower() != "yes":
    quit()

print("Okay ! Lets's play :)")
score = 0

answer = input ("What does CPU stand for? ")

if answer.lower() == "central process unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input ("What is the capial city of Somalia? ")

if answer.lower() == "Mogadishu":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input ("Who is the president of Kenya? ")

if answer.lower() == "Ruto" or "William Ruto":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input ("What does GPU stand for? ")

if answer.lower() == "Graphics process unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input ("which country has the longest coastline in Africa  ? ")

if answer.upper() == "Somalia":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input ("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


print(" You got " + str(score) + " questions correct!" )
print(" You got " + str((score/4) * 100) + " %!" )


