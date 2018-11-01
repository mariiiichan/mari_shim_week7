from random import randint

# Available weapons => Store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False 
playerScore = 2
computerScore = 2

# Make the computer pick one item at random
computer = choices[randint(0, 2)]

# Show the computer's choice in the terminal window
print("Computer chooses: ", computer)
print("You and the computer have 3 lives.") #i want to show how it has lives

while player is False:
	print("Choose your weapon!")
	player = input("Rock, Paper, or Scissors?\n")
	print("Player chooses:", player)

	if (player == computer):
		print("Tie! Get it together!")

	elif player == "Rock":
		if computer == "Paper":
			# Computer won
			print("You lose!", computer, " covers ", player)
			playerScore -= 1 #subtracting a life
			print("Score is", playerScore. "|", computerScore)
		else:
			print("You win!", player, " smashes ", computer)
			computerScore -= 1 #subtracting a life

			
			
		

	elif player == "Paper":
		if computer == "Scissors":
			# Computer won
			print("You lose!", computer, " cuts ", player)
			playerScore -= 1:
			print("Score is ", playerScore, "|", computerScore)
		else:
			print("You win!", player, " covers ", computer)
			computerScore -= 1:
			print("Score is ", playerScore, "|", computerScore)

	elif player == "Scissors":
		if computer == "Rock":
			# Computer won
			print("You lose!", computer, " smashes ", player)
			playerScore -= 1:
			print("Score is ", playerScore, "|", computerScore)
		else:
			print("You win!", player, " cuts ", computer)
			computerScore -= 1:
			print("Score is ", playerScore, "|", computerScore)


	elif player == "Quit":
		exit()

	else:
		print("Not a valid option. Please re-enter your choice, and check your spelling!\n")

	elif
		if playerScore == 0: 
			print("You lose. Try again")

		else computerScore == 0:
			print("Computer loses. You win!"):

	

	player = False
	computer = choices[randint(0,2)]
