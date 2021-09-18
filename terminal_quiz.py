# Codecademy Capstone
# Capital Cities Quiz Game

import random

user_answer = ""
score = 80
line = "---------------------------------------------"
win = """--------------------
|                  |
|    You Won!      |
|                  |
____________________"""

num_of_questions = 0
lives = 3

q_a = {"France?" : "Paris",
       "Great Britain?" : "London",
       "USA?" : "Washington",
       "Germany?" : "Berlin",
       "Italy?" : "Rome",
       "Spain?" : "Madrid",
       "Japan?" : "Tokyo",
       "China?" : "Beijing",
       "India?" : "New Delhi",
       "Australia?" : "Canberra",
       "Belgium?" : "Brussels"}

username = input("Please enter your first name: ")
print(line)
print("Hello", username, "Let's play a game of Capital Cities!")
print("Get 10 correct to win the game.")
print("Press q to quit game.")
print(line)

while(user_answer != "q"):
    print()
    random_country = random.choice(list(q_a.keys()))
    answer = q_a[random_country]

    if(num_of_questions <= 10):

        if(score == 100):
            print(win)
            break
        else:
            print("What is the capital of", random_country)
            print()
            user_answer = input("What is your answer? ").lower()
            print()
            if(user_answer == "q"):
                print()
                print("Thanks for playing, your final score is", score)
                break
            elif(user_answer == answer.lower()):
                q_a.pop(random_country)
                print("That is correct!")
                score += 10
                num_of_questions += 1
                print("You're current score is", score)
            else:
                num_of_questions += 1
                lives -= 1
                print("Sorry that is the wrong answer")
                print("You have:", lives, "lives left")
                print("You're current score is", score)
    else:
        print("Game over, you're final scoe is", score)

