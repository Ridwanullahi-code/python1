from random import randint
Game_running = True
new_round = True
while Game_running == True:
	random_number = randint(1,10)
	number = int(input("Guess a number between 1 and 10: "))
	print(f"random number is: {random_number} and number is: {number}") 
	if number == random_number:
		print("You guessed it! You won!")
	elif number > random_number:
		print("Too high, try again!")
	elif number < random_number:
		print("Too low, try again!")

	if number == random_number:
		Game_running = False
playing = input("Do you want to keep playing (y/n) ")
while new_round == True:
	if playing == "y":
		random_number = randint(1,10)
		number = int(input("Guess a number between 1 and 10: "))
		print(f"random number is: {random_number} and number is: {number}") 
		if number == random_number:
			print("You guessed it! You won!")
		elif number > random_number:
			print("Too high, try again!")
		elif number < random_number:
			print("Too low, try again!")
	elif playing == "n":
		print("Thanks for playing. Bye!")
		break






