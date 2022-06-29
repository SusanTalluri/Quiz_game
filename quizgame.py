print("Welcome to my computer quiz!") # Weclome page to the user

# ask the user for an input promt if he wants to play the game or no
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    print('Great Job!')
    score += 1
else:
    print('Incorrect!')
    print('Better luck next time!')

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    print('Great Job!')
    score += 1
else:
    print('Incorrect!')
    print('Better luck next time!')

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
    print('Great Job!')
else:
    print('Incorrect!')
    print('Better luck next time!')

answer = input("What does ROM stand for? ")
if answer.lower() == "read olny memory":
    print('Correct!')
    score += 1
    print('Great Job!')
else:
    print('Incorrect!')
    print('Better luck next time!')
print("Hurray! You got " + str(score) + " questions correct!")
print("Hurray! You got " + str((score/4) * 100) + "%")