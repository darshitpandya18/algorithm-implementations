import random

def RNG():
	# Function defines, selects and returns the output 
	# of one of those
	return random.randint(1,3)

def check_winner(input_1, input_2):
	#Checks the winner as per the input 1 an input 2

	if input_1 == 1 and input_2 == 2:
		print("Computer Wins")

	elif input_1 == 1 and input_2 == 3:
		print("User Wins")

	elif input_1 == 2 and input_2 == 1:
		print("User Wins")

	elif input_1 == 2 and input_2 == 3:
		print("Computer Wins")

	elif input_1 == 3 and input_1 == 1:
		print("Computer Wins")

	elif input_1 == 3 and input_1 == 2:
		print("User Wins")

	elif input_1 == input_2:
		print("Draw! Try again")


input_1 = int(input("Enter the user input: "))
input_2 = RNG()
print("Computer Selected: ", input_2)
#1: Rock
#2: Paper
#3: Scissor
check_winner(input_1, input_2)

