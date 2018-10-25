print("This is my conditions file")
# let the user pick a temp,see what happens to water (conditional statements)
# cuurent_temp is the temperature variable (user inputs this)
current_temp = False 

while current_temp is False: 
	# user input - this chanegs temp on every iteration
	current_temp = input("Enter a temperature:  \n")
	print(current_temp)

	if(int(current_temp) < 0) or (int(current_temp) == 0):
		print("water is a solid, icy!")
		current_temp = False 

	# if its below 0, obvi its frozen 
	elif (int(current_temp) < 100):
		print("water is a liquid, profit!")
		current_temp = False

	# if its above 100, obvi its a gas 
	elif (int(current_temp > 100)) or (int(current_temp == 100)):
		print("water is a vapor, cuz it's HOT")
		current_temp = False 

