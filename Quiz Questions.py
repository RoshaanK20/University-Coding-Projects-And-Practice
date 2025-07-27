import random 

#Generating Random Quizes
number_1 = random.randint(0,99)
number_2 = random.randint(0,99)

#Choices between "+" & "-" equation
operation = random.choice(["+","-"])

#Prompt user to enter your answer
user_answers = input(" What Is " + str(number_1) + " " + operation + " " +str(number_2) + " = ")

#Convert user's answer into integers
user_answers = int(user_answers)

#Correct Answer based on chosen operation
if (operation == "+"):
   correct_answer = number_1 + number_2
elif (operation == "-"):
   correct_answer = abs(number_1 - number_2 and number_2 - number_1)

#Display Result
if (user_answers == correct_answer):
   print("\033[2;32;40m Correct Hogya Shera!")
else :
   print("\033[2;31;40m Incorrect Hai Shera!" "\033[2;32;40m The Correct Answer Is",correct_answer)
