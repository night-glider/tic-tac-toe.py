print("\twelcome to tic_tac_toe.py!\n")
print("\tType where you want to place your O\n")
print("\t(in format <row><column>)")
print("\t(for example '22')")

cell = input("Your turn:")
#what happens if player goes 1,1
if cell == "11":
	print("New O on 1,1:")
	print("- - - - -")
	print("| O     |")
	print("|       |")
	print("|       |")
	print("- - - - -")
	
	print("Enemy turn:")
	print("- - - - -")
	print("| O     |")
	print("|       |")
	print("| X     |")
	print("- - - - -")
	
	cell = input("Your turn:")
	#what happens if player goes 2,1
	if cell == "21":
		print("New O on 2,1:")
		print("- - - - -")
		print("| O O   |")
		print("|       |")
		print("| X     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| O O   |")
		print("|       |")
		print("| X X   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("| O O O |")
			print("|       |")
			print("| X X   |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("| O O   |")
			print("| O     |")
			print("| X X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O   |")
			print("| O     |")
			print("| X X X |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("| O O   |")
			print("|   O   |")
			print("| X X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O X |")
			print("|   O   |")
			print("| X X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O O X |")
				print("| O O   |")
				print("| X X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O O   |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O O X |")
				print("|   O O |")
				print("| X X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("|   O O |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O O X |")
				print("|   O   |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("| O O   |")
			print("|     O |")
			print("| X X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O   |")
			print("|   X O |")
			print("| X X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O O O |")
				print("|   X O |")
				print("| X X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O O   |")
				print("| O X O |")
				print("| X X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| O X O |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O O   |")
				print("|   X O |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("| O O   |")
			print("|       |")
			print("| X X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O   |")
			print("|   X   |")
			print("| X X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O O O |")
				print("|   X   |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O O   |")
				print("| O X   |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O X   |")
				print("| X X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O O   |")
				print("|   X O |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,1
	if cell == "31":
		print("New O on 3,1:")
		print("- - - - -")
		print("| O   O |")
		print("|       |")
		print("| X     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| O X O |")
		print("|       |")
		print("| X     |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("| O X O |")
			print("| O     |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X O |")
			print("| O     |")
			print("| X   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X O |")
				print("| O O   |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O O   |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X O |")
				print("| O   O |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O X O |")
				print("| X   X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X O |")
				print("| O     |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O X   |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("| O X O |")
			print("|   O   |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X O |")
			print("|   O X |")
			print("| X     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O X O |")
				print("| O O X |")
				print("| X     |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O O X |")
				print("| X   X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X O |")
				print("|   O X |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X O X |")
				print("| X O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X O |")
					print("| X O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X O |")
				print("|   O X |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("| O X O |")
			print("|     O |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X O |")
			print("|     O |")
			print("| X   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O X O |")
				print("| O   O |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O X O |")
				print("| X   X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X O |")
				print("|   O O |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("|   O O |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X O |")
				print("|     O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("|   X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("| O X O |")
			print("|       |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X O |")
			print("| X     |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X O |")
				print("| X O   |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X O X |")
				print("| X O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X O |")
					print("| X O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X O |")
				print("| X   O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X   O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X O |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X O |")
				print("| X     |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X   X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X O |")
					print("| X O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("| O X O |")
			print("|       |")
			print("| X   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X O |")
			print("|       |")
			print("| X X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O X O |")
				print("| O     |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O X   |")
				print("| X X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X O |")
				print("|   O   |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X O |")
				print("|     O |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 1,2
	if cell == "12":
		print("New O on 1,2:")
		print("- - - - -")
		print("| O     |")
		print("| O     |")
		print("| X     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| O X   |")
		print("| O     |")
		print("| X     |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("| O X O |")
			print("| O     |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X O |")
			print("| O     |")
			print("| X   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X O |")
				print("| O O   |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O O X |")
				print("| X   X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X O |")
				print("| O   O |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O X O |")
				print("| X   X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X O |")
				print("| O     |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O X   |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("| O X   |")
			print("| O O   |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X X |")
			print("| O O   |")
			print("| X     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X X |")
				print("| O O O |")
				print("| X     |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X X |")
				print("| O O   |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O O X |")
				print("| X O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X X |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X X |")
				print("| O O   |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("| O X   |")
			print("| O   O |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X   |")
			print("| O X O |")
			print("| X     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O X O |")
				print("| O X O |")
				print("| X     |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O X O |")
				print("| X X   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X   |")
				print("| O X O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X   |")
				print("| O X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X   |")
				print("| O X O |")
				print("| X   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X   |")
				print("| O X O |")
				print("| X X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("| O X   |")
			print("| O     |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X X |")
			print("| O     |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X X |")
				print("| O O   |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O O   |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O X X |")
					print("| O O O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X X |")
				print("| O   O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O X O |")
				print("| X O   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X X |")
				print("| O     |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O   X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X X |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("| O X   |")
			print("| O     |")
			print("| X   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X X |")
			print("| O     |")
			print("| X   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X X |")
				print("| O O   |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X X |")
				print("| O   O |")
				print("| X   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O   O |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X X |")
					print("| O O O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X X |")
				print("| O     |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O X   |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,2
	if cell == "22":
		print("New O on 2,2:")
		print("- - - - -")
		print("| O     |")
		print("|   O   |")
		print("| X     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| O   X |")
		print("|   O   |")
		print("| X     |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#i hate my life...
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("| O O X |")
			print("|   O   |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O X |")
			print("|   O X |")
			print("| X     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O O X |")
				print("| O O X |")
				print("| X     |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O O X |")
				print("| X   X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O O X |")
				print("|   O X |")
				print("| X O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O O X |")
				print("|   O X |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("| O   X |")
			print("| O O   |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X X |")
			print("| O O   |")
			print("| X     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X X |")
				print("| O O O |")
				print("| X     |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X X |")
				print("| O O   |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O O   |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O X X |")
					print("| O O O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X X |")
				print("| O O   |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("| O   X |")
			print("|   O O |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   X |")
			print("| X O O |")
			print("| X     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X O O |")
				print("| X     |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X O O |")
				print("| X   X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O O X |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O   X |")
				print("| X O O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X O O |")
				print("| X O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X X |")
					print("| X O O |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O   X |")
				print("| X O O |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("| O   X |")
			print("|   O   |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X X |")
			print("|   O   |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O X X |")
				print("| O O   |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O O X |")
				print("| X O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X X |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X X |")
				print("|   O O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("|   O O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| O X X |")
					print("| O O O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X X |")
				print("|   O   |")
				print("| X O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("| O   X |")
			print("|   O   |")
			print("| X   O |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,2
	if cell == "32":
		print("New O on 3,2:")
		print("- - - - -")
		print("| O     |")
		print("|     O |")
		print("| X     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| O     |")
		print("|   X O |")
		print("| X     |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("| O O   |")
			print("|   X O |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O   |")
			print("|   X O |")
			print("| X   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O O O |")
				print("|   X O |")
				print("| X   X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O O   |")
				print("| O X O |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| O X O |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O O   |")
				print("|   X O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("| O   O |")
			print("|   X O |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   O |")
			print("|   X O |")
			print("| X X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O O |")
				print("|   X O |")
				print("| X X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O   O |")
				print("| O X O |")
				print("| X X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O X O |")
				print("| X X   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O   O |")
				print("|   X O |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("| O     |")
			print("| O X O |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O     |")
			print("| O X O |")
			print("| X   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O   |")
				print("| O X O |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| O X O |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O   O |")
				print("| O X O |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O X O |")
				print("| X   X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O     |")
				print("| O X O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   X |")
				print("| O X O |")
				print("| X O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("| O     |")
			print("|   X O |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X   |")
			print("|   X O |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O X O |")
				print("|   X O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X X O |")
				print("| X O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X O |")
					print("| X X O |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O X   |")
				print("| O X O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O X O |")
				print("| X O   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X   |")
				print("|   X O |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("|   X O |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("| O     |")
			print("|   X O |")
			print("| X   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O     |")
			print("|   X O |")
			print("| X X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O   |")
				print("|   X O |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O   O |")
				print("|   X O |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O     |")
				print("| O X O |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X   |")
				print("| O X O |")
				print("| X X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,3
	if cell == "23":
		print("New O on 2,3:")
		print("- - - - -")
		print("| O     |")
		print("|       |")
		print("| X O   |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| O     |")
		print("|     X |")
		print("| X O   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("| O O   |")
			print("|     X |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O   |")
			print("| X   X |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X   X |")
				print("| X O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O O   |")
				print("| X O X |")
				print("| X O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O O   |")
				print("| X   X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X X |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("| O   O |")
			print("|     X |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   O |")
			print("| X   X |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X   X |")
				print("| X O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O   O |")
				print("| X O X |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| X O X |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X O X |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O   O |")
				print("| X   X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| X X X |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("| O     |")
			print("| O   X |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O     |")
			print("| O X X |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O   |")
				print("| O X X |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O X X |")
				print("| X O   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O   O |")
				print("| O X X |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| O X X |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O O |")
					print("| O X X |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O     |")
				print("| O X X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   X |")
				print("| O X X |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("| O     |")
			print("|   O X |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X   |")
			print("|   O X |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O X O |")
				print("|   O X |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X O X |")
				print("| X O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X O |")
					print("| X O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O X   |")
				print("| O O X |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X   |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X   |")
				print("|   O X |")
				print("| X O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("| O     |")
			print("|     X |")
			print("| X O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O     |")
			print("|   X X |")
			print("| X O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O   |")
				print("|   X X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("|   X X |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O   O |")
				print("|   X X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| X X X |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O     |")
				print("| O X X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   X |")
				print("| O X X |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,3
	if cell == "33":
		print("New O on 3,3:")
		print("- - - - -")
		print("| O     |")
		print("|       |")
		print("| X   O |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| O X   |")
		print("|       |")
		print("| X   O |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("| O X O |")
			print("|       |")
			print("| X   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X O |")
			print("| X     |")
			print("| X   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X O |")
				print("| X O   |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X O |")
				print("| X   O |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X O |")
				print("| X     |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X X   |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O X O |")
					print("| X X O |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("| O X   |")
			print("| O     |")
			print("| X   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X   |")
			print("| O   X |")
			print("| X   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O X O |")
				print("| O   X |")
				print("| X   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O X X |")
				print("| X   O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O X O |")
					print("| O X X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X   |")
				print("| O O X |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X   |")
				print("| O   X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X   |")
				print("| O X X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O X X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("| O X   |")
			print("|   O   |")
			print("| X   O |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("| O X   |")
			print("|     O |")
			print("| X   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X   |")
			print("|   X O |")
			print("| X   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O X O |")
				print("|   X O |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O X   |")
				print("| O X O |")
				print("| X   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O X O |")
				print("| X   O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X   |")
				print("|   X O |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X   |")
				print("| X X O |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O X O |")
					print("| X X O |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("| O X   |")
			print("|       |")
			print("| X O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X X |")
			print("|       |")
			print("| X O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O X X |")
				print("| O     |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O   X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X X |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X X |")
				print("|   O   |")
				print("| X O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X X |")
				print("|     O |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X   O |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X X |")
					print("| X O O |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	
	print("wrong cell!")
	quit()
#what happens if player goes 2,1
if cell == "21":
	print("New O on 2,1:")
	print("- - - - -")
	print("|   O   |")
	print("|       |")
	print("|       |")
	print("- - - - -")
	
	print("Enemy turn:")
	print("- - - - -")
	print("|   O   |")
	print("| X     |")
	print("|       |")
	print("- - - - -")
	
	cell = input("Your turn:")
	#what happens if player goes 1,1
	if cell == "11":
		print("New O on 1,1:")
		print("- - - - -")
		print("| O O   |")
		print("| X     |")
		print("|       |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| O O   |")
		print("| X   X |")
		print("|       |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("| O O O |")
			print("| X   X |")
			print("|       |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("| O O   |")
			print("| X O X |")
			print("|       |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O X |")
			print("| X O X |")
			print("|       |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O O X |")
				print("| X O X |")
				print("| O     |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X O X |")
				print("| O X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O O X |")
					print("| X O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O O X |")
				print("| X O X |")
				print("|   O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O O X |")
				print("| X O X |")
				print("|     O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("| O O   |")
			print("| X   X |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O   |")
			print("| X   X |")
			print("| O X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X   X |")
				print("| O X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O O   |")
				print("| X O X |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X O X |")
				print("| O X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O O X |")
					print("| X O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O O   |")
				print("| X   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X X |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("| O O   |")
			print("| X   X |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O   |")
			print("| X   X |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X   X |")
				print("| X O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O O   |")
				print("| X O X |")
				print("| X O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O O   |")
				print("| X   X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X   X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O O X |")
					print("| X O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("| O O   |")
			print("| X   X |")
			print("|     O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O X |")
			print("| X   X |")
			print("|     O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O O X |")
				print("| X O X |")
				print("|     O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O O X |")
				print("| X   X |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X   X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O O X |")
					print("| X O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O O X |")
				print("| X   X |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X X |")
				print("|   O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,1
	if cell == "31":
		print("New O on 3,1:")
		print("- - - - -")
		print("|   O O |")
		print("| X     |")
		print("|       |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   O O |")
		print("| X     |")
		print("|     X |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O O O |")
			print("| X     |")
			print("|     X |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|   O O |")
			print("| X O   |")
			print("|     X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X O O |")
			print("| X O   |")
			print("|     X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| X O O |")
				print("| X O O |")
				print("|     X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X O O |")
				print("| X   X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X O O |")
				print("| X O   |")
				print("| O   X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| X O O |")
				print("| X O   |")
				print("|   O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("|   O O |")
			print("| X   O |")
			print("|     X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X O O |")
			print("| X   O |")
			print("|     X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| X O O |")
				print("| X O O |")
				print("|     X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X O O |")
				print("|   X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X O O |")
					print("| X O O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X O O |")
				print("| X   O |")
				print("| O   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X X O |")
				print("| O   X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| X O O |")
				print("| X   O |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X X O |")
				print("|   O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|   O O |")
			print("| X     |")
			print("| O   X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O O |")
			print("| X     |")
			print("| O X X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#i hate my life...
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X     |")
				print("| O X X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   O O |")
				print("| X O   |")
				print("| O X X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   O O |")
				print("| X   O |")
				print("| O X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|   O O |")
			print("| X     |")
			print("|   O X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O O |")
			print("| X   X |")
			print("|   O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X   X |")
				print("|   O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   O O |")
				print("| X O X |")
				print("|   O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O O |")
				print("| X   X |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X   X |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X O O |")
					print("| X O X |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,2
	if cell == "22":
		print("New O on 2,2:")
		print("- - - - -")
		print("|   O   |")
		print("| X O   |")
		print("|       |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   O   |")
		print("| X O   |")
		print("|   X   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O O   |")
			print("| X O   |")
			print("|   X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O X |")
			print("| X O   |")
			print("|   X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O O X |")
				print("| X O O |")
				print("|   X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X O O |")
				print("|   X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| O O X |")
					print("| X O O |")
					print("| O X X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X O O |")
					print("| O X X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O O X |")
				print("| X O   |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X O X |")
				print("| O X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O O X |")
					print("| X O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O O X |")
				print("| X O   |")
				print("|   X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|   O O |")
			print("| X O   |")
			print("|   X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O O |")
			print("| X O   |")
			print("| X X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X O   |")
				print("| X X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   O O |")
				print("| X O O |")
				print("| X X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X O O |")
				print("| X X   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   O O |")
				print("| X O   |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X O   |")
				print("| X X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("|   O   |")
			print("| X O O |")
			print("|   X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O   |")
			print("| X O O |")
			print("|   X X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O   |")
				print("| X O O |")
				print("|   X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X O O |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   O O |")
				print("| X O O |")
				print("|   X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X O O |")
				print("|   X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X O O |")
					print("| X O O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O   |")
				print("| X O O |")
				print("| O X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| X O O |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O X |")
					print("| X O O |")
					print("| O X X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X O O |")
					print("| O X X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|   O   |")
			print("| X O   |")
			print("| O X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O   |")
			print("| X O X |")
			print("| O X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O   |")
				print("| X O X |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X O X |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X O X |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   O O |")
				print("| X O X |")
				print("| O X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   O   |")
				print("| X O X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| X O X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O X |")
					print("| X O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|   O   |")
			print("| X O   |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("| X O   |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X O   |")
				print("|   X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   O X |")
				print("| X O O |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| X O O |")
				print("|   X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X O X |")
					print("| X O O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| X O O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O X |")
				print("| X O   |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| X O X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O X |")
					print("| X O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,2
	if cell == "32":
		print("New O on 3,2:")
		print("- - - - -")
		print("|   O   |")
		print("| X   O |")
		print("|       |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   O   |")
		print("| X X O |")
		print("|       |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O O   |")
			print("| X X O |")
			print("|       |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O   |")
			print("| X X O |")
			print("|     X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X X O |")
				print("|     X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| O   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|   O O |")
			print("| X X O |")
			print("|       |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X O O |")
			print("| X X O |")
			print("|       |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X O O |")
				print("| X X O |")
				print("| O     |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X X O |")
				print("| O   X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| X O O |")
				print("| X X O |")
				print("|   O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X X O |")
				print("| X O   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X O O |")
				print("| X X O |")
				print("|     O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|   O   |")
			print("| X X O |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X O   |")
			print("| X X O |")
			print("| O     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| X O O |")
				print("| X X O |")
				print("| O     |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X X O |")
				print("| O X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| X O O |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| X O   |")
				print("| X X O |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| X X O |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X O   |")
				print("| X X O |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| X X O |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X O O |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|   O   |")
			print("| X X O |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O   |")
			print("| X X O |")
			print("|   O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X X O |")
				print("|   O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O   |")
				print("| X X O |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| X X O |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|   O   |")
			print("| X X O |")
			print("|     O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("| X X O |")
			print("|     O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X X O |")
				print("|     O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X O |")
				print("|   X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O X |")
				print("| X X O |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| X X O |")
				print("| O   O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| X O X |")
					print("| X X O |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   O X |")
				print("| X X O |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| X X O |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 1,3
	if cell == "13":
		print("New O on 1,3:")
		print("- - - - -")
		print("|   O   |")
		print("| X     |")
		print("| O     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   O   |")
		print("| X X   |")
		print("| O     |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O O   |")
			print("| X X   |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O   |")
			print("| X X   |")
			print("| O   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X X   |")
				print("| O   X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| O   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O O   |")
				print("| X X   |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X X |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|   O O |")
			print("| X X   |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O O |")
			print("| X X   |")
			print("| O   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X X   |")
				print("| O   X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("| O   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X X O |")
				print("| O   X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   O O |")
				print("| X X   |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X X X |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("|   O   |")
			print("| X X O |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("| X X O |")
			print("| O     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X X O |")
				print("| O     |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X O |")
				print("| O   X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   O X |")
				print("| X X O |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| X X O |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   O X |")
				print("| X X O |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| X X O |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|   O   |")
			print("| X X   |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O   |")
			print("| X X X |")
			print("| O O   |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|   O   |")
			print("| X X   |")
			print("| O   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O   |")
			print("| X X X |")
			print("| O   O |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,3
	if cell == "23":
		print("New O on 2,3:")
		print("- - - - -")
		print("|   O   |")
		print("| X     |")
		print("|   O   |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   O X |")
		print("| X     |")
		print("|   O   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O O X |")
			print("| X     |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O X |")
			print("| X     |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O O X |")
				print("| X O   |")
				print("| X O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O O X |")
				print("| X   O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X   O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O O X |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O O X |")
				print("| X     |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X   |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|   O X |")
			print("| X O   |")
			print("|   O   |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("|   O X |")
			print("| X   O |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("| X   O |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X   O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X   O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O O X |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   O X |")
				print("| X O O |")
				print("| X O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   O X |")
				print("| X   O |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| X X O |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|   O X |")
			print("| X     |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("| X     |")
			print("| O O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X     |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X   |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   O X |")
				print("| X O   |")
				print("| O O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   O X |")
				print("| X   O |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| X X O |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|   O X |")
			print("| X     |")
			print("|   O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("| X     |")
			print("| X O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X     |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X   |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   O X |")
				print("| X O   |")
				print("| X O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   O X |")
				print("| X   O |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| X X O |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,3
	if cell == "33":
		print("New O on 3,3:")
		print("- - - - -")
		print("|   O   |")
		print("| X     |")
		print("|     O |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   O   |")
		print("| X     |")
		print("|   X O |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O O   |")
			print("| X     |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O   |")
			print("| X X   |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X X   |")
				print("|   X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O O   |")
				print("| X X   |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X X |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|   O O |")
			print("| X     |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O O |")
			print("| X X   |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X X   |")
				print("|   X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("|   X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O O |")
				print("| X X   |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X X X |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|   O   |")
			print("| X O   |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("| X O   |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X O   |")
				print("|   X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   O X |")
				print("| X O O |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| X O O |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O X |")
					print("| X O O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O X |")
				print("| X O   |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| X O   |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| X O X |")
					print("| X O O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| X O O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("|   O   |")
			print("| X   O |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O   |")
			print("| X X O |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("|   X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O   |")
				print("| X X O |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| X X O |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X O O |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|   O   |")
			print("| X     |")
			print("| O X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X O   |")
			print("| X     |")
			print("| O X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| X O O |")
				print("| X     |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X   X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X O O |")
					print("| X O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| X O   |")
				print("| X O   |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| X O X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X O O |")
					print("| X O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| X O   |")
				print("| X   O |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| X   O |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X O X |")
					print("| X O O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| X O O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	
	print("wrong cell!")
	quit()
#what happens if player goes 3,1
if cell == "31":
	print("New O on 3,1:")
	print("- - - - -")
	print("|     O |")
	print("|       |")
	print("|       |")
	print("- - - - -")
	
	print("Enemy turn:")
	print("- - - - -")
	print("|     O |")
	print("| X     |")
	print("|       |")
	print("- - - - -")
	
	cell = input("Your turn:")
	#what happens if player goes 1,1
	if cell == "11":
		print("New O on 1,1:")
		print("- - - - -")
		print("| O   O |")
		print("| X     |")
		print("|       |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| O   O |")
		print("| X     |")
		print("| X     |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("| O O O |")
			print("| X     |")
			print("| X     |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("| O   O |")
			print("| X O   |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X O |")
			print("| X O   |")
			print("| X     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X O |")
				print("| X O O |")
				print("| X     |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X O O |")
				print("| X X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X O |")
					print("| X O O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X O |")
				print("| X O   |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X O   |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O X O |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X O |")
				print("| X O   |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("| O   O |")
			print("| X   O |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   O |")
			print("| X   O |")
			print("| X   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X   O |")
				print("| X   X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O   O |")
				print("| X O O |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X O O |")
				print("| X   X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O X O |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O   O |")
				print("| X   O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| X X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("| O   O |")
			print("| X     |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X O |")
			print("| X     |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X O |")
				print("| X O   |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X O   |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O X O |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X O |")
				print("| X   O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X X O |")
				print("| X O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X O |")
					print("| X X O |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X O |")
				print("| X     |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X   X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X O |")
					print("| X O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("| O   O |")
			print("| X     |")
			print("| X   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   O |")
			print("| X     |")
			print("| X X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X     |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O   O |")
				print("| X O   |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O   O |")
				print("| X   O |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,1
	if cell == "21":
		print("New O on 2,1:")
		print("- - - - -")
		print("|   O O |")
		print("| X     |")
		print("|       |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   O O |")
		print("| X   X |")
		print("|       |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O O O |")
			print("| X   X |")
			print("|       |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|   O O |")
			print("| X O X |")
			print("|       |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O O |")
			print("| X O X |")
			print("| X     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X O X |")
				print("| X     |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   O O |")
				print("| X O X |")
				print("| X O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   O O |")
				print("| X O X |")
				print("| X   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X O X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|   O O |")
			print("| X   X |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O O |")
			print("| X   X |")
			print("| O X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X   X |")
				print("| O X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   O O |")
				print("| X O X |")
				print("| O X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   O O |")
				print("| X   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X X X |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|   O O |")
			print("| X   X |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O O |")
			print("| X X X |")
			print("|   O   |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|   O O |")
			print("| X   X |")
			print("|     O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O O |")
			print("| X   X |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X   X |")
				print("|   X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   O O |")
				print("| X O X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X O X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O O |")
				print("| X   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X   X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X O O |")
					print("| X O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,2
	if cell == "22":
		print("New O on 2,2:")
		print("- - - - -")
		print("|     O |")
		print("| X O   |")
		print("|       |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|     O |")
		print("| X O X |")
		print("|       |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O   O |")
			print("| X O X |")
			print("|       |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X O |")
			print("| X O X |")
			print("|       |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O X O |")
				print("| X O X |")
				print("| O     |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X O |")
				print("| X O X |")
				print("|   O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X O X |")
				print("|   O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| O X O |")
					print("| X O X |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X O |")
				print("| X O X |")
				print("|     O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O O |")
			print("| X O X |")
			print("|       |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O O |")
			print("| X O X |")
			print("| X     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X O X |")
				print("| X     |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   O O |")
				print("| X O X |")
				print("| X O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   O O |")
				print("| X O X |")
				print("| X   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X O X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|     O |")
			print("| X O X |")
			print("| O     |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|     O |")
			print("| X O X |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("| X O X |")
			print("|   O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("| X O X |")
				print("|   O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X O X |")
				print("| X O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X O |")
					print("| X O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   X O |")
				print("| X O X |")
				print("| O O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   X O |")
				print("| X O X |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| X O X |")
				print("|   O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X X O |")
					print("| X O X |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|     O |")
			print("| X O X |")
			print("|     O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("| X O X |")
			print("|     O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("| X O X |")
				print("|     O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   X O |")
				print("| X O X |")
				print("| O   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   X O |")
				print("| X O X |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| X O X |")
				print("|   O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#i hate my life...
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X X O |")
					print("| X O X |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,2
	if cell == "32":
		print("New O on 3,2:")
		print("- - - - -")
		print("|     O |")
		print("| X   O |")
		print("|       |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|     O |")
		print("| X   O |")
		print("| X     |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O   O |")
			print("| X   O |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   O |")
			print("| X X O |")
			print("| X     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X X O |")
				print("| X     |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O   O |")
				print("| X X O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X X O |")
				print("| X O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X O |")
					print("| X X O |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O   O |")
				print("| X X O |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O O |")
			print("| X   O |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O O |")
			print("| X   O |")
			print("| X X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X   O |")
				print("| X X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   O O |")
				print("| X O O |")
				print("| X X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X O O |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   O O |")
				print("| X   O |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|     O |")
			print("| X O O |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("| X O O |")
			print("| X     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("| X O O |")
				print("| X     |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X O O |")
				print("| X X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X O |")
					print("| X O O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   X O |")
				print("| X O O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| X O O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X O |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   X O |")
				print("| X O O |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|     O |")
			print("| X   O |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     O |")
			print("| X   O |")
			print("| X O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   O |")
				print("| X   O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| X X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O O |")
				print("| X   O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X   O |")
				print("| X O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|     O |")
				print("| X O O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   O |")
				print("| X O O |")
				print("| X O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|     O |")
			print("| X   O |")
			print("| X   O |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 1,3
	if cell == "13":
		print("New O on 1,3:")
		print("- - - - -")
		print("|     O |")
		print("| X     |")
		print("| O     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|     O |")
		print("| X X   |")
		print("| O     |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O   O |")
			print("| X X   |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   O |")
			print("| X X   |")
			print("| O X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X X   |")
				print("| O X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O   O |")
				print("| X X O |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| X X O |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O   O |")
				print("| X X   |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X X   |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O O |")
			print("| X X   |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O O |")
			print("| X X   |")
			print("| O   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X X   |")
				print("| O   X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("| O   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   O O |")
				print("| X X   |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X X   |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("|     O |")
			print("| X X O |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     O |")
			print("| X X O |")
			print("| O   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   O |")
				print("| X X O |")
				print("| O   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| X X O |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("| O   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X X O |")
				print("| O   X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|     O |")
				print("| X X O |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| X X O |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X O |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|     O |")
			print("| X X   |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     O |")
			print("| X X   |")
			print("| O O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   O |")
				print("| X X   |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X X   |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O X O |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O O |")
				print("| X X   |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X X X |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|     O |")
				print("| X X O |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| X X O |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X O |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|     O |")
			print("| X X   |")
			print("| O   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("| X X   |")
			print("| O   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("| X X   |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X X   |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   X O |")
				print("| X X O |")
				print("| O   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   X O |")
				print("| X X   |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,3
	if cell == "23":
		print("New O on 2,3:")
		print("- - - - -")
		print("|     O |")
		print("| X     |")
		print("|   O   |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| X   O |")
		print("| X     |")
		print("|   O   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("| X O O |")
			print("| X     |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X O O |")
			print("| X   X |")
			print("|   O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| X O O |")
				print("| X O X |")
				print("|   O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X O O |")
				print("| X   X |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X   X |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X O O |")
					print("| X O X |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X O O |")
				print("| X   X |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X   X |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("| X   O |")
			print("| X O   |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   O |")
			print("| X O   |")
			print("|   O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O O |")
				print("| X O   |")
				print("|   O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| X   O |")
				print("| X O O |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| X O O |")
				print("|   O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X X O |")
					print("| X O O |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X   O |")
				print("| X O   |")
				print("| O O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("| X   O |")
			print("| X   O |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   O |")
			print("| X   O |")
			print("|   O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O O |")
				print("| X   O |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X X O |")
				print("|   O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| X   O |")
				print("| X O O |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| X O O |")
				print("|   O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X X O |")
					print("| X O O |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X   O |")
				print("| X   O |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   O |")
				print("| X X O |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("| X   O |")
			print("| X     |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   O |")
			print("| X   X |")
			print("| O O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O O |")
				print("| X   X |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X X X |")
				print("| O O   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| X   O |")
				print("| X O X |")
				print("| O O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X   O |")
				print("| X   X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("| X   O |")
			print("| X     |")
			print("|   O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   O |")
			print("| X X   |")
			print("|   O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O O |")
				print("| X X   |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X X   |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| X   O |")
				print("| X X O |")
				print("|   O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X   O |")
				print("| X X   |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,3
	if cell == "33":
		print("New O on 3,3:")
		print("- - - - -")
		print("|     O |")
		print("| X     |")
		print("|     O |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|     O |")
		print("| X   X |")
		print("|     O |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O   O |")
			print("| X   X |")
			print("|     O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   O |")
			print("| X   X |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X   X |")
				print("|   X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O   O |")
				print("| X O X |")
				print("|   X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O   O |")
				print("| X   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| X X X |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O O |")
			print("| X   X |")
			print("|     O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O O |")
			print("| X X X |")
			print("|     O |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|     O |")
			print("| X O X |")
			print("|     O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   O |")
			print("| X O X |")
			print("|     O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O O |")
				print("| X O X |")
				print("|     O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X O X |")
				print("|   X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X O O |")
					print("| X O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X   O |")
				print("| X O X |")
				print("| O   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| X   O |")
				print("| X O X |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| X O X |")
				print("|   O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X X O |")
					print("| X O X |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|     O |")
			print("| X   X |")
			print("| O   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("| X   X |")
			print("| O   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("| X   X |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X   X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X O |")
					print("| X O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   X O |")
				print("| X O X |")
				print("| O   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   X O |")
				print("| X   X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|     O |")
			print("| X   X |")
			print("|   O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     O |")
			print("| X X X |")
			print("|   O O |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		
		print("wrong cell!")
		quit()
	
	print("wrong cell!")
	quit()
#what happens if player goes 1,2
if cell == "12":
	print("New O on 1,2:")
	print("- - - - -")
	print("|       |")
	print("| O     |")
	print("|       |")
	print("- - - - -")
	
	print("Enemy turn:")
	print("- - - - -")
	print("|       |")
	print("| O   X |")
	print("|       |")
	print("- - - - -")
	
	cell = input("Your turn:")
	#what happens if player goes 1,1
	if cell == "11":
		print("New O on 1,1:")
		print("- - - - -")
		print("| O     |")
		print("| O   X |")
		print("|       |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| O     |")
		print("| O   X |")
		print("|     X |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("| O O   |")
			print("| O   X |")
			print("|     X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O X |")
			print("| O   X |")
			print("|     X |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("| O   O |")
			print("| O   X |")
			print("|     X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   O |")
			print("| O   X |")
			print("|   X X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O O |")
				print("| O   X |")
				print("|   X X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O   O |")
				print("| O O X |")
				print("|   X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O O X |")
				print("|   X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O   O |")
				print("| O   X |")
				print("| O X X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("| O     |")
			print("| O O X |")
			print("|     X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O     |")
			print("| O O X |")
			print("| X   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O   |")
				print("| O O X |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| O O X |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O   O |")
				print("| O O X |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O O X |")
				print("| X   X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O     |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   X |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("| O     |")
			print("| O   X |")
			print("| O   X |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("| O     |")
			print("| O   X |")
			print("|   O X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O     |")
			print("| O   X |")
			print("| X O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O   |")
				print("| O   X |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O   X |")
				print("| X O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O   O |")
				print("| O   X |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| O X X |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O O |")
					print("| O X X |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O     |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   X |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,1
	if cell == "21":
		print("New O on 2,1:")
		print("- - - - -")
		print("|   O   |")
		print("| O   X |")
		print("|       |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   O   |")
		print("| O   X |")
		print("|   X   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O O   |")
			print("| O   X |")
			print("|   X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O   |")
			print("| O   X |")
			print("| X X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O O O |")
				print("| O   X |")
				print("| X X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O O   |")
				print("| O O X |")
				print("| X X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O O X |")
				print("| X X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O O X |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O O   |")
				print("| O   X |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| O X X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| O X X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|   O O |")
			print("| O   X |")
			print("|   X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X O O |")
			print("| O   X |")
			print("|   X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| X O O |")
				print("| O O X |")
				print("|   X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| O O X |")
				print("|   X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X O O |")
				print("| O   X |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| O   X |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X O O |")
				print("| O   X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| O X X |")
				print("|   X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X O O |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O O |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|   O   |")
			print("| O O X |")
			print("|   X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O   |")
			print("| O O X |")
			print("| X X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O   |")
				print("| O O X |")
				print("| X X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O O X |")
				print("| X X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O O X |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   O O |")
				print("| O O X |")
				print("| X X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| O O X |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   O   |")
				print("| O O X |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| O O X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|   O   |")
			print("| O   X |")
			print("| O X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X O   |")
			print("| O   X |")
			print("| O X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| X O O |")
				print("| O   X |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| O   X |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| X O   |")
				print("| O O X |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| O O X |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X O   |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X O O |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O O |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|   O   |")
			print("| O   X |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O   |")
			print("| O X X |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O   |")
				print("| O X X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O X X |")
				print("|   X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| O O X |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   O O |")
				print("| O X X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| O X X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| O X X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O   |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X O O |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O O |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,1
	if cell == "31":
		print("New O on 3,1:")
		print("- - - - -")
		print("|     O |")
		print("| O   X |")
		print("|       |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|     O |")
		print("| O   X |")
		print("|   X   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O   O |")
			print("| O   X |")
			print("|   X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   O |")
			print("| O X X |")
			print("|   X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O O |")
				print("| O X X |")
				print("|   X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O   O |")
				print("| O X X |")
				print("| O X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O   O |")
				print("| O X X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O X X |")
				print("|   X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O O |")
			print("| O   X |")
			print("|   X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O O |")
			print("| O   X |")
			print("|   X X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O O |")
				print("| O   X |")
				print("|   X X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   O O |")
				print("| O O X |")
				print("|   X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| O O X |")
				print("|   X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O O |")
				print("| O   X |")
				print("| O X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| O X X |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| O X X |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|     O |")
			print("| O O X |")
			print("|   X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   O |")
			print("| O O X |")
			print("|   X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O O |")
				print("| O O X |")
				print("|   X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| O O X |")
				print("| X X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X   O |")
				print("| O O X |")
				print("| O X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X   O |")
				print("| O O X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   O |")
				print("| O O X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|     O |")
			print("| O   X |")
			print("| O X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("| O   X |")
			print("| O X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("| O   X |")
				print("| O X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   X O |")
				print("| O O X |")
				print("| O X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   X O |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|     O |")
			print("| O   X |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("| O   X |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("| O   X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O   X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   X O |")
				print("| O O X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| O O X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   X O |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,2
	if cell == "22":
		print("New O on 2,2:")
		print("- - - - -")
		print("|       |")
		print("| O O X |")
		print("|       |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|       |")
		print("| O O X |")
		print("|     X |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O     |")
			print("| O O X |")
			print("|     X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O     |")
			print("| O O X |")
			print("|   X X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O   |")
				print("| O O X |")
				print("|   X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O O X |")
				print("|   X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O   O |")
				print("| O O X |")
				print("|   X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| O O X |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O     |")
				print("| O O X |")
				print("| O X X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O   |")
			print("| O O X |")
			print("|     X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O   |")
			print("| O O X |")
			print("| X   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O   |")
				print("| O O X |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| O O X |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   O O |")
				print("| O O X |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| O O X |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   O   |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|     O |")
			print("| O O X |")
			print("|     X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     O |")
			print("| O O X |")
			print("|   X X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   O |")
				print("| O O X |")
				print("|   X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| O O X |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O O |")
				print("| O O X |")
				print("|   X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| O O X |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|     O |")
				print("| O O X |")
				print("| O X X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|       |")
			print("| O O X |")
			print("| O   X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X   |")
			print("| O O X |")
			print("| O   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X   |")
				print("| O O X |")
				print("| O   X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   X O |")
				print("| O O X |")
				print("| O   X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   X   |")
				print("| O O X |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X   |")
				print("| O O X |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|       |")
			print("| O O X |")
			print("|   O X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     X |")
			print("| O O X |")
			print("|   O X |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 1,3
	if cell == "13":
		print("New O on 1,3:")
		print("- - - - -")
		print("|       |")
		print("| O   X |")
		print("| O     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|       |")
		print("| O X X |")
		print("| O     |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O     |")
			print("| O X X |")
			print("| O     |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O   |")
			print("| O X X |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("| O X X |")
			print("| O     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("| O X X |")
				print("| O     |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   O X |")
				print("| O X X |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O X X |")
				print("| O O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| X O X |")
					print("| O X X |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   O X |")
				print("| O X X |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O X |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|     O |")
			print("| O X X |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     O |")
			print("| O X X |")
			print("| O   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   O |")
				print("| O X X |")
				print("| O   X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O O |")
				print("| O X X |")
				print("| O   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| O X X |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| O X X |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|     O |")
				print("| O X X |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   O |")
				print("| O X X |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|       |")
			print("| O X X |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X     |")
			print("| O X X |")
			print("| O O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O   |")
				print("| O X X |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O X X |")
				print("| O O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| X O X |")
					print("| O X X |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| X   O |")
				print("| O X X |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O X X |")
				print("| O O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| X X O |")
					print("| O X X |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X     |")
				print("| O X X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|       |")
			print("| O X X |")
			print("| O   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|       |")
			print("| O X X |")
			print("| O X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O     |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O   |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X O O |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O O |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|     O |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,3
	if cell == "23":
		print("New O on 2,3:")
		print("- - - - -")
		print("|       |")
		print("| O   X |")
		print("|   O   |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|       |")
		print("| O   X |")
		print("|   O X |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O     |")
			print("| O   X |")
			print("|   O X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   X |")
			print("| O   X |")
			print("|   O X |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O   |")
			print("| O   X |")
			print("|   O X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O   |")
			print("| O X X |")
			print("|   O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O   |")
				print("| O X X |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O X X |")
				print("|   O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   O O |")
				print("| O X X |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| O X X |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| O X X |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O   |")
				print("| O X X |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| O X X |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|     O |")
			print("| O   X |")
			print("|   O X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("| O   X |")
			print("|   O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("| O   X |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O   X |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   X O |")
				print("| O O X |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   X O |")
				print("| O   X |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O   X |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|       |")
			print("| O O X |")
			print("|   O X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X     |")
			print("| O O X |")
			print("|   O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O   |")
				print("| O O X |")
				print("|   O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| X   O |")
				print("| O O X |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   O |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X     |")
				print("| O O X |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X   |")
				print("| O O X |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|       |")
			print("| O   X |")
			print("| O O X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X   |")
			print("| O   X |")
			print("| O O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X   |")
				print("| O   X |")
				print("| O O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   X O |")
				print("| O   X |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O   X |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   X   |")
				print("| O O X |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X X |")
				print("| O O X |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,3
	if cell == "33":
		print("New O on 3,3:")
		print("- - - - -")
		print("|       |")
		print("| O   X |")
		print("|     O |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|       |")
		print("| O   X |")
		print("|   X O |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O     |")
			print("| O   X |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O     |")
			print("| O X X |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O   |")
				print("| O X X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O X X |")
				print("|   X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| O O X |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O   O |")
				print("| O X X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| O X X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O O |")
					print("| O X X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O     |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O   |")
			print("| O   X |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X O   |")
			print("| O   X |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| X O O |")
				print("| O   X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| O   X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| X O   |")
				print("| O O X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O O X |")
				print("|   X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X O   |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X O O |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O O |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|     O |")
			print("| O   X |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   O |")
			print("| O   X |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O O |")
				print("| O   X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| O X X |")
				print("|   X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X O O |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O O |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| X   O |")
				print("| O O X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O O X |")
				print("|   X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X   O |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   O |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| X O O |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O O |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|       |")
			print("| O O X |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|       |")
			print("| O O X |")
			print("| X X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O     |")
				print("| O O X |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O   |")
				print("| O O X |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| O O X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|     O |")
				print("| O O X |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   O |")
				print("| O O X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|       |")
			print("| O   X |")
			print("| O X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|       |")
			print("| O X X |")
			print("| O X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O     |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O   |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X O O |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O O |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|     O |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	
	print("wrong cell!")
	quit()
#what happens if player goes 2,2
if cell == "22":
	print("New O on 2,2:")
	print("- - - - -")
	print("|       |")
	print("|   O   |")
	print("|       |")
	print("- - - - -")
	
	print("Enemy turn:")
	print("- - - - -")
	print("|       |")
	print("|   O   |")
	print("| X     |")
	print("- - - - -")
	
	cell = input("Your turn:")
	#what happens if player goes 1,1
	if cell == "11":
		print("New O on 1,1:")
		print("- - - - -")
		print("| O     |")
		print("|   O   |")
		print("| X     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| O     |")
		print("| X O   |")
		print("| X     |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("| O O   |")
			print("| X O   |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O   |")
			print("| X O X |")
			print("| X     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X O X |")
				print("| X     |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O O   |")
				print("| X O X |")
				print("| X O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O O   |")
				print("| X O X |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("| O   O |")
			print("| X O   |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   O |")
			print("| X O X |")
			print("| X     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X O X |")
				print("| X     |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O   O |")
				print("| X O X |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X O X |")
				print("| X O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X O |")
					print("| X O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O   O |")
				print("| X O X |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("| O     |")
			print("| X O O |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X   |")
			print("| X O O |")
			print("| X     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O X O |")
				print("| X O O |")
				print("| X     |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X O O |")
				print("| X X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X O |")
					print("| X O O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X   |")
				print("| X O O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X   |")
				print("| X O O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O X O |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X   |")
				print("| X O O |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("| O     |")
			print("| X O   |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   X |")
			print("| X O   |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X O   |")
				print("| X O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O   X |")
				print("| X O O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X O O |")
				print("| X O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X X |")
					print("| X O O |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O   X |")
				print("| X O   |")
				print("| X O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("| O     |")
			print("| X O   |")
			print("| X   O |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,1
	if cell == "21":
		print("New O on 2,1:")
		print("- - - - -")
		print("|   O   |")
		print("|   O   |")
		print("| X     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   O X |")
		print("|   O   |")
		print("| X     |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O O X |")
			print("|   O   |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O X |")
			print("|   O   |")
			print("| X X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O O X |")
				print("| O O   |")
				print("| X X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O O X |")
				print("| X X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O O X |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O O X |")
				print("|   O O |")
				print("| X X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X O O |")
				print("| X X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O O X |")
					print("| X O O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O O X |")
				print("|   O   |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|   O X |")
			print("| O O   |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("| O O   |")
			print("| X X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("| O O   |")
				print("| X X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O O X |")
				print("| X X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O O X |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   O X |")
				print("| O O O |")
				print("| X X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   O X |")
				print("| O O   |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O O   |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O O O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("|   O X |")
			print("|   O O |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("|   O O |")
			print("| X   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("|   O O |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X O O |")
				print("| X   X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O O X |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   O X |")
				print("| O O O |")
				print("| X   X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   O X |")
				print("|   O O |")
				print("| X O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|   O X |")
			print("|   O   |")
			print("| X O   |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|   O X |")
			print("|   O   |")
			print("| X   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("|   O   |")
			print("| X X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("|   O   |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   O X |")
				print("| O O   |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| O O X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O X |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   O X |")
				print("|   O O |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("|   O O |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O O O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,1
	if cell == "31":
		print("New O on 3,1:")
		print("- - - - -")
		print("|     O |")
		print("|   O   |")
		print("| X     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|     O |")
		print("|   O   |")
		print("| X   X |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O   O |")
			print("|   O   |")
			print("| X   X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   O |")
			print("|   O X |")
			print("| X   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O O |")
				print("|   O X |")
				print("| X   X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O   O |")
				print("| O O X |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| O O X |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O   O |")
				print("|   O X |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("|   O X |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O O |")
			print("|   O   |")
			print("| X   X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X O O |")
			print("|   O   |")
			print("| X   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X O O |")
				print("| O O   |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| O O   |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| X O O |")
				print("|   O O |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("|   O O |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| X O O |")
				print("|   O   |")
				print("| X O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|     O |")
			print("| O O   |")
			print("| X   X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     O |")
			print("| O O X |")
			print("| X   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   O |")
				print("| O O X |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| O O X |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O O |")
				print("| O O X |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| O O X |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|     O |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("|     O |")
			print("|   O O |")
			print("| X   X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("|   O O |")
			print("| X   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("|   O O |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X O O |")
				print("| X   X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O X O |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| X O O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   X O |")
				print("| O O O |")
				print("| X   X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   X O |")
				print("|   O O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("|   O O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X X O |")
					print("| O O O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|     O |")
			print("|   O   |")
			print("| X O X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   O |")
			print("|   O   |")
			print("| X O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O O |")
				print("|   O   |")
				print("| X O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X   O |")
				print("| O O   |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O O   |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| X X O |")
					print("| O O O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| X   O |")
				print("|   O O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   O |")
				print("| X O O |")
				print("| X O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 1,2
	if cell == "12":
		print("New O on 1,2:")
		print("- - - - -")
		print("|       |")
		print("| O O   |")
		print("| X     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|       |")
		print("| O O   |")
		print("| X   X |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O     |")
			print("| O O   |")
			print("| X   X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   X |")
			print("| O O   |")
			print("| X   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O X |")
				print("| O O   |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O O X |")
				print("| X   X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O   X |")
				print("| O O O |")
				print("| X   X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O   X |")
				print("| O O   |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O O   |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O X X |")
					print("| O O O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O   |")
			print("| O O   |")
			print("| X   X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O   |")
			print("| O O X |")
			print("| X   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O   |")
				print("| O O X |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O O X |")
				print("| X   X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   O O |")
				print("| O O X |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| O O X |")
				print("| X   X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   O   |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|     O |")
			print("| O O   |")
			print("| X   X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     O |")
			print("| O O   |")
			print("| X X X |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("|       |")
			print("| O O O |")
			print("| X   X |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|       |")
			print("| O O   |")
			print("| X O X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X   |")
			print("| O O   |")
			print("| X O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X   |")
				print("| O O   |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O O   |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O X X |")
					print("| O O O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   X O |")
				print("| O O   |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   X   |")
				print("| O O O |")
				print("| X O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,2
	if cell == "32":
		print("New O on 3,2:")
		print("- - - - -")
		print("|       |")
		print("|   O O |")
		print("| X     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| X     |")
		print("|   O O |")
		print("| X     |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("| X O   |")
			print("|   O O |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X O   |")
			print("|   O O |")
			print("| X X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| X O O |")
				print("|   O O |")
				print("| X X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("|   O O |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X O   |")
				print("| O O O |")
				print("| X X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X O   |")
				print("|   O O |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("|   O O |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O O O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("| X   O |")
			print("|   O O |")
			print("| X     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   O |")
			print("|   O O |")
			print("| X X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O O |")
				print("|   O O |")
				print("| X X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("|   O O |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X   O |")
				print("| O O O |")
				print("| X X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X   O |")
				print("|   O O |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("| X     |")
			print("| O O O |")
			print("| X     |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("| X     |")
			print("|   O O |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X   |")
			print("|   O O |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| X X O |")
				print("|   O O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| X O O |")
				print("| X O   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X X   |")
				print("| O O O |")
				print("| X O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X X   |")
				print("|   O O |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X X |")
				print("|   O O |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("| X     |")
			print("|   O O |")
			print("| X   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X     |")
			print("|   O O |")
			print("| X X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O   |")
				print("|   O O |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| X O O |")
				print("| X X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| X   O |")
				print("|   O O |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X     |")
				print("| O O O |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,3
	if cell == "23":
		print("New O on 2,3:")
		print("- - - - -")
		print("|       |")
		print("|   O   |")
		print("| X O   |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|       |")
		print("|   O X |")
		print("| X O   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O     |")
			print("|   O X |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O     |")
			print("|   O X |")
			print("| X O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O   |")
				print("|   O X |")
				print("| X O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O   O |")
				print("|   O X |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("|   O X |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O     |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X   |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O   |")
			print("|   O X |")
			print("| X O   |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|     O |")
			print("|   O X |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   O |")
			print("|   O X |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O O |")
				print("|   O X |")
				print("| X O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X   O |")
				print("| O O X |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   O |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| X O O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X   O |")
				print("|   O X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("|   O X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|       |")
			print("| O O X |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|       |")
			print("| O O X |")
			print("| X O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O     |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   X |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O   |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|     O |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| O O X |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|       |")
			print("|   O X |")
			print("| X O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     X |")
			print("|   O X |")
			print("| X O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   X |")
				print("|   O X |")
				print("| X O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O X |")
				print("|   O X |")
				print("| X O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|     X |")
				print("| O O X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   X |")
				print("| O O X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,3
	if cell == "33":
		print("New O on 3,3:")
		print("- - - - -")
		print("|       |")
		print("|   O   |")
		print("| X   O |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   X   |")
		print("|   O   |")
		print("| X   O |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O X   |")
			print("|   O   |")
			print("| X   O |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|   X O |")
			print("|   O   |")
			print("| X   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("| X O   |")
			print("| X   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("| X O   |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   X O |")
				print("| X O O |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   X O |")
				print("| X O   |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| X O   |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|   X   |")
			print("| O O   |")
			print("| X   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X   |")
			print("| O O X |")
			print("| X   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X   |")
				print("| O O X |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   X O |")
				print("| O O X |")
				print("| X   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O O X |")
				print("| X   O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   X   |")
				print("| O O X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X   |")
				print("| O O X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("|   X   |")
			print("|   O O |")
			print("| X   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X X |")
			print("|   O O |")
			print("| X   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X X |")
				print("|   O O |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   X X |")
				print("| O O O |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   X X |")
				print("|   O O |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X X |")
				print("|   O O |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|   X   |")
			print("|   O   |")
			print("| X O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X   |")
			print("|   O X |")
			print("| X O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X   |")
				print("|   O X |")
				print("| X O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   X O |")
				print("|   O X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| X O X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X O |")
					print("| X O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   X   |")
				print("| O O X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X X |")
				print("| O O X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X X |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	
	print("wrong cell!")
	quit()
#what happens if player goes 3,2
if cell == "32":
	print("New O on 3,2:")
	print("- - - - -")
	print("|       |")
	print("|     O |")
	print("|       |")
	print("- - - - -")
	
	print("Enemy turn:")
	print("- - - - -")
	print("|       |")
	print("|   X O |")
	print("|       |")
	print("- - - - -")
	
	cell = input("Your turn:")
	#what happens if player goes 1,1
	if cell == "11":
		print("New O on 1,1:")
		print("- - - - -")
		print("| O     |")
		print("|   X O |")
		print("|       |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| O   X |")
		print("|   X O |")
		print("|       |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("| O O X |")
			print("|   X O |")
			print("|       |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O X |")
			print("|   X O |")
			print("|   X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#i hate my life...
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O O X |")
				print("| O X O |")
				print("|   X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O X O |")
				print("|   X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| O O X |")
					print("| O X O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O O X |")
				print("|   X O |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X O |")
				print("| O X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O O X |")
				print("|   X O |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X O |")
				print("|   X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("| O   X |")
			print("| O X O |")
			print("|       |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   X |")
			print("| O X O |")
			print("| X     |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("| O   X |")
			print("|   X O |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X X |")
			print("|   X O |")
			print("| O     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O X X |")
				print("| O X O |")
				print("| O     |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X X |")
				print("|   X O |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("|   X O |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| O X X |")
					print("| O X O |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X X |")
				print("|   X O |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("|   X O |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("| O   X |")
			print("|   X O |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   X |")
			print("| X X O |")
			print("|   O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X X O |")
				print("|   O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X O |")
				print("| X O   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O   X |")
				print("| X X O |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X X O |")
				print("| O O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X X |")
					print("| X X O |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O   X |")
				print("| X X O |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   X |")
				print("| X X O |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("| O   X |")
			print("|   X O |")
			print("|     O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   X |")
			print("| X X O |")
			print("|     O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X X O |")
				print("|     O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X O |")
				print("| X   O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O   X |")
				print("| X X O |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   X |")
				print("| X X O |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O   X |")
				print("| X X O |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X X O |")
				print("|   O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| O X X |")
					print("| X X O |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,1
	if cell == "21":
		print("New O on 2,1:")
		print("- - - - -")
		print("|   O   |")
		print("|   X O |")
		print("|       |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   O   |")
		print("|   X O |")
		print("|   X   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O O   |")
			print("|   X O |")
			print("|   X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O   |")
			print("| X X O |")
			print("|   X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X X O |")
				print("|   X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|   O O |")
			print("|   X O |")
			print("|   X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O O |")
			print("|   X O |")
			print("|   X X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O O |")
				print("|   X O |")
				print("|   X X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   O O |")
				print("| O X O |")
				print("|   X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| O X O |")
				print("|   X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O O |")
				print("|   X O |")
				print("| O X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("|   X O |")
				print("| O X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|   O   |")
			print("| O X O |")
			print("|   X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X O   |")
			print("| O X O |")
			print("|   X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| X O O |")
				print("| O X O |")
				print("|   X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| O X O |")
				print("| X X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| X O O |")
					print("| O X O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X O   |")
				print("| O X O |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| O X O |")
				print("| O X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X O   |")
				print("| O X O |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| O X O |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X O O |")
					print("| O X O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|   O   |")
			print("|   X O |")
			print("| O X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O   |")
			print("| X X O |")
			print("| O X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X O |")
				print("| O X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   O   |")
				print("| X X O |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| X X O |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X O O |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|   O   |")
			print("|   X O |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O   |")
			print("|   X O |")
			print("| X X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O   |")
				print("|   X O |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   O O |")
				print("|   X O |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   O   |")
				print("| O X O |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| O X O |")
				print("| X X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,1
	if cell == "31":
		print("New O on 3,1:")
		print("- - - - -")
		print("|     O |")
		print("|   X O |")
		print("|       |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|     O |")
		print("|   X O |")
		print("|     X |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O   O |")
			print("|   X O |")
			print("|     X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   O |")
			print("|   X O |")
			print("| X   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O O |")
				print("|   X O |")
				print("| X   X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O   O |")
				print("| O X O |")
				print("| X   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O X O |")
				print("| X   X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O   O |")
				print("|   X O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| X X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O O |")
			print("|   X O |")
			print("|     X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O O |")
			print("|   X O |")
			print("|   X X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O O |")
				print("|   X O |")
				print("|   X X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   O O |")
				print("| O X O |")
				print("|   X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| O X O |")
				print("|   X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O O |")
				print("|   X O |")
				print("| O X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|     O |")
			print("| O X O |")
			print("|     X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("| O X O |")
			print("|     X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("| O X O |")
				print("|     X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O X O |")
				print("|   X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   X O |")
				print("| O X O |")
				print("| O   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O X O |")
				print("| O   X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   X O |")
				print("| O X O |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O X O |")
				print("|   O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|     O |")
			print("|   X O |")
			print("| O   X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     O |")
			print("|   X O |")
			print("| O X X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   O |")
				print("|   X O |")
				print("| O X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| X X O |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O O |")
				print("|   X O |")
				print("| O X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|     O |")
				print("| O X O |")
				print("| O X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   O |")
				print("| O X O |")
				print("| O X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|     O |")
			print("|   X O |")
			print("|   O X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     O |")
			print("|   X O |")
			print("| X O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   O |")
				print("|   X O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("|   X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O O |")
				print("|   X O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|     O |")
				print("| O X O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   O |")
				print("| O X O |")
				print("| X O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 1,2
	if cell == "12":
		print("New O on 1,2:")
		print("- - - - -")
		print("|       |")
		print("| O X O |")
		print("|       |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|       |")
		print("| O X O |")
		print("|   X   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O     |")
			print("| O X O |")
			print("|   X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   X |")
			print("| O X O |")
			print("|   X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O X |")
				print("| O X O |")
				print("|   X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O X O |")
				print("| X X   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O   X |")
				print("| O X O |")
				print("| O X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O   X |")
				print("| O X O |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   X |")
				print("| O X O |")
				print("| X X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O   |")
			print("| O X O |")
			print("|   X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O   |")
			print("| O X O |")
			print("|   X X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O   |")
				print("| O X O |")
				print("|   X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O X O |")
				print("|   X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| O O X |")
					print("| O X O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   O O |")
				print("| O X O |")
				print("|   X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| O X O |")
				print("| X X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O   |")
				print("| O X O |")
				print("| O X X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| O X O |")
				print("| O X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|     O |")
			print("| O X O |")
			print("|   X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("| O X O |")
			print("|   X   |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|       |")
			print("| O X O |")
			print("| O X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X   |")
			print("| O X O |")
			print("| O X   |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|       |")
			print("| O X O |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X   |")
			print("| O X O |")
			print("|   X O |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 1,3
	if cell == "13":
		print("New O on 1,3:")
		print("- - - - -")
		print("|       |")
		print("|   X O |")
		print("| O     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   X   |")
		print("|   X O |")
		print("| O     |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O X   |")
			print("|   X O |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X   |")
			print("|   X O |")
			print("| O   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O X O |")
				print("|   X O |")
				print("| O   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X X O |")
				print("| O   X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O X O |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O X   |")
				print("| O X O |")
				print("| O   X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X   |")
				print("|   X O |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X   |")
				print("| X X O |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O X O |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|   X O |")
			print("|   X O |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("|   X O |")
			print("| O   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("|   X O |")
				print("| O   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("|   X O |")
				print("| O X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   X O |")
				print("| O X O |")
				print("| O   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O X O |")
				print("| O   X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   X O |")
				print("|   X O |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("|   X O |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|   X   |")
			print("| O X O |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X   |")
			print("| O X O |")
			print("| O     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| X X O |")
				print("| O X O |")
				print("| O     |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O X O |")
				print("| O   X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| X X   |")
				print("| O X O |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X X |")
				print("| O X O |")
				print("| O O   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X X   |")
				print("| O X O |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X X |")
				print("| O X O |")
				print("| O   O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|   X   |")
			print("|   X O |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X X |")
			print("|   X O |")
			print("| O O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X X |")
				print("|   X O |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X X O |")
				print("| O O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X X |")
					print("| X X O |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   X X |")
				print("| O X O |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X X |")
				print("| O X O |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X X |")
					print("| O X O |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   X X |")
				print("|   X O |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|   X   |")
			print("|   X O |")
			print("| O   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X X |")
			print("|   X O |")
			print("| O   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X X |")
				print("|   X O |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("|   X O |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   X X |")
				print("| O X O |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X X |")
				print("| O X O |")
				print("| O   O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   X X |")
				print("|   X O |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,3
	if cell == "23":
		print("New O on 2,3:")
		print("- - - - -")
		print("|       |")
		print("|   X O |")
		print("|   O   |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|       |")
		print("|   X O |")
		print("| X O   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O     |")
			print("|   X O |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O     |")
			print("|   X O |")
			print("| X O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O   |")
				print("|   X O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O   O |")
				print("|   X O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| X X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O     |")
				print("| O X O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   X |")
				print("| O X O |")
				print("| X O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O   |")
			print("|   X O |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O   |")
			print("| X X O |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   O   |")
				print("| X X O |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| X X O |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|     O |")
			print("|   X O |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     O |")
			print("| X X O |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   O |")
				print("| X X O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X X O |")
				print("| X O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X O |")
					print("| X X O |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|     O |")
				print("| X X O |")
				print("| X O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|       |")
			print("| O X O |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|       |")
			print("| O X O |")
			print("| X O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O     |")
				print("| O X O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X   |")
				print("| O X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O   |")
				print("| O X O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| O X O |")
				print("| X O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|     O |")
				print("| O X O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| O X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|       |")
			print("|   X O |")
			print("| X O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     X |")
			print("|   X O |")
			print("| X O O |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,3
	if cell == "33":
		print("New O on 3,3:")
		print("- - - - -")
		print("|       |")
		print("|   X O |")
		print("|     O |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|       |")
		print("|   X O |")
		print("|   X O |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O     |")
			print("|   X O |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O     |")
			print("|   X O |")
			print("| X X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O   |")
				print("|   X O |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("|   X O |")
				print("| X X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O   O |")
				print("|   X O |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O     |")
				print("| O X O |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   X |")
				print("| O X O |")
				print("| X X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O   |")
			print("|   X O |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O   |")
			print("| X X O |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X O |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X X O |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   O O |")
				print("| X X O |")
				print("|   X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O   |")
				print("| X X O |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| X X O |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|     O |")
			print("|   X O |")
			print("|   X O |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|       |")
			print("| O X O |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X   |")
			print("| O X O |")
			print("|   X O |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|       |")
			print("|   X O |")
			print("| O X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X   |")
			print("|   X O |")
			print("| O X O |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		
		print("wrong cell!")
		quit()
	
	print("wrong cell!")
	quit()
#what happens if player goes 1,3
if cell == "13":
	print("New O on 1,3:")
	print("- - - - -")
	print("|       |")
	print("|       |")
	print("| O     |")
	print("- - - - -")
	
	print("Enemy turn:")
	print("- - - - -")
	print("|     X |")
	print("|       |")
	print("| O     |")
	print("- - - - -")
	
	cell = input("Your turn:")
	#what happens if player goes 1,1
	if cell == "11":
		print("New O on 1,1:")
		print("- - - - -")
		print("| O   X |")
		print("|       |")
		print("| O     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| O   X |")
		print("| X     |")
		print("| O     |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("| O O X |")
			print("| X     |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O X |")
			print("| X X   |")
			print("| O     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O O X |")
				print("| X X O |")
				print("| O     |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X O |")
				print("| O   X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O O X |")
				print("| X X   |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X X |")
				print("| O O   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O O X |")
				print("| X X   |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X   |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("| O   X |")
			print("| X O   |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   X |")
			print("| X O   |")
			print("| O   X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X O   |")
				print("| O   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X O X |")
				print("| O   X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O   X |")
				print("| X O O |")
				print("| O   X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   X |")
				print("| X O O |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O X |")
					print("| X O O |")
					print("| O X X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X O O |")
					print("| O X X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O   X |")
				print("| X O   |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X O   |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O X X |")
					print("| X O O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X X |")
					print("| X O O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("| O   X |")
			print("| X   O |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X X |")
			print("| X   O |")
			print("| O     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X X |")
				print("| X O O |")
				print("| O     |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X O O |")
				print("| O   X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O X X |")
					print("| X O O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X X |")
					print("| X O O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X X |")
				print("| X   O |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X   O |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X X |")
					print("| X O O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X X |")
					print("| X O O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X X |")
				print("| X   O |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X   O |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X X |")
					print("| X O O |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("| O   X |")
			print("| X     |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   X |")
			print("| X X   |")
			print("| O O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X X   |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X   |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O   X |")
				print("| X X O |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   X |")
				print("| X X O |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O   X |")
				print("| X X   |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("| O   X |")
			print("| X     |")
			print("| O   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   X |")
			print("| X   X |")
			print("| O   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X   X |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X   X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O O X |")
					print("| X O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O   X |")
				print("| X O X |")
				print("| O   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O   X |")
				print("| X   X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,1
	if cell == "21":
		print("New O on 2,1:")
		print("- - - - -")
		print("|   O X |")
		print("|       |")
		print("| O     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   O X |")
		print("|     X |")
		print("| O     |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O O X |")
			print("|     X |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O X |")
			print("|     X |")
			print("| O   X |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|   O X |")
			print("| O   X |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("| O   X |")
			print("| O X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("| O   X |")
				print("| O X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   O X |")
				print("| O O X |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| O O X |")
				print("| O X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   O X |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|   O X |")
			print("|   O X |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("|   O X |")
			print("| O X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("|   O X |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("|   O X |")
				print("| O X X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   O X |")
				print("| O O X |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O O X |")
				print("| O X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   O X |")
				print("|   O X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("|   O X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|   O X |")
			print("|     X |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("| X   X |")
			print("| O O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X   X |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X X |")
				print("| O O   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   O X |")
				print("| X O X |")
				print("| O O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   O X |")
				print("| X   X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|   O X |")
			print("|     X |")
			print("| O   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("|   X X |")
			print("| O   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("|   X X |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X X |")
				print("| O   O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   O X |")
				print("| O X X |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O X |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   O X |")
				print("|   X X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 1,2
	if cell == "12":
		print("New O on 1,2:")
		print("- - - - -")
		print("|     X |")
		print("| O     |")
		print("| O     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| X   X |")
		print("| O     |")
		print("| O     |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("| X O X |")
			print("| O     |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X O X |")
			print("| O X   |")
			print("| O     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| X O X |")
				print("| O X O |")
				print("| O     |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O X O |")
				print("| O   X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| X O X |")
				print("| O X   |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O X   |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X O X |")
				print("| O X   |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O X X |")
				print("| O   O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| X O X |")
					print("| O X X |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("| X   X |")
			print("| O O   |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X X |")
			print("| O O   |")
			print("| O     |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("| X   X |")
			print("| O   O |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X X |")
			print("| O   O |")
			print("| O     |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("| X   X |")
			print("| O     |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   X |")
			print("| O   X |")
			print("| O O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O X |")
				print("| O   X |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O   X |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| X   X |")
				print("| O O X |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   X |")
				print("| O O X |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X   X |")
				print("| O   X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("| X   X |")
			print("| O     |")
			print("| O   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X X |")
			print("| O     |")
			print("| O   O |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,2
	if cell == "22":
		print("New O on 2,2:")
		print("- - - - -")
		print("|     X |")
		print("|   O   |")
		print("| O     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|     X |")
		print("|   O   |")
		print("| O X   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O   X |")
			print("|   O   |")
			print("| O X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   X |")
			print("| X O   |")
			print("| O X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X O   |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X O   |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O O X |")
					print("| X O O |")
					print("| O X X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X O O |")
					print("| O X X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O   X |")
				print("| X O O |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   X |")
				print("| X O O |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O X |")
					print("| X O O |")
					print("| O X X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X O O |")
					print("| O X X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O   X |")
				print("| X O   |")
				print("| O X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O X |")
			print("|   O   |")
			print("| O X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X O X |")
			print("|   O   |")
			print("| O X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X O X |")
				print("| O O   |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O O   |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O O O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| X O X |")
				print("|   O O |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("|   O O |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O O O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X O X |")
				print("|   O   |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("|   O X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|     X |")
			print("| O O   |")
			print("| O X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   X |")
			print("| O O   |")
			print("| O X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O X |")
				print("| O O   |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O O X |")
				print("| O X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| X   X |")
				print("| O O O |")
				print("| O X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X   X |")
				print("| O O   |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   X |")
				print("| O O X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("|     X |")
			print("|   O O |")
			print("| O X   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X X |")
			print("|   O O |")
			print("| O X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X X |")
				print("|   O O |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X O O |")
				print("| O X   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X X |")
					print("| X O O |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   X X |")
				print("| O O O |")
				print("| O X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   X X |")
				print("|   O O |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X X |")
				print("| X O O |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X X |")
					print("| X O O |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|     X |")
			print("|   O   |")
			print("| O X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     X |")
			print("|   O X |")
			print("| O X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   X |")
				print("|   O X |")
				print("| O X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O X |")
				print("|   O X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("|   O X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|     X |")
				print("| O O X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   X |")
				print("| O O X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,2
	if cell == "32":
		print("New O on 3,2:")
		print("- - - - -")
		print("|     X |")
		print("|     O |")
		print("| O     |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| X   X |")
		print("|     O |")
		print("| O     |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("| X O X |")
			print("|     O |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X O X |")
			print("|   X O |")
			print("| O     |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X O X |")
				print("| O X O |")
				print("| O     |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O X O |")
				print("| O   X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| X O X |")
				print("|   X O |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| X X O |")
				print("| O O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| X O X |")
					print("| X X O |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X O X |")
				print("|   X O |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("|   X O |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("| X   X |")
			print("| O   O |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   X |")
			print("| O   O |")
			print("| O X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O X |")
				print("| O   O |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O   O |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O O O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| X   X |")
				print("| O O O |")
				print("| O X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X   X |")
				print("| O   O |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   X |")
				print("| O X O |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| X O X |")
					print("| O X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("| X   X |")
			print("|   O O |")
			print("| O     |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   X |")
			print("|   O O |")
			print("| O X   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O X |")
				print("|   O O |")
				print("| O X   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("|   O O |")
				print("| O X X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O O O |")
					print("| O X X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X   X |")
				print("| O O O |")
				print("| O X   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X   X |")
				print("|   O O |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   X |")
				print("| X O O |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| X O X |")
					print("| X O O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| X O O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("| X   X |")
			print("|     O |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   X |")
			print("|   X O |")
			print("| O O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O X |")
				print("|   X O |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| X X O |")
				print("| O O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| X O X |")
					print("| X X O |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X   X |")
				print("| O X O |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   X |")
				print("| O X O |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X   X |")
				print("|   X O |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("| X   X |")
			print("|     O |")
			print("| O   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   X |")
			print("|     O |")
			print("| O X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O X |")
				print("|     O |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("|   X O |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X   X |")
				print("| O   O |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X X |")
				print("| O   O |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| X   X |")
				print("|   O O |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X X |")
				print("|   O O |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,3
	if cell == "23":
		print("New O on 2,3:")
		print("- - - - -")
		print("|     X |")
		print("|       |")
		print("| O O   |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|     X |")
		print("|   X   |")
		print("| O O   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O   X |")
			print("|   X   |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   X |")
			print("| X X   |")
			print("| O O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X X   |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X   |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O   X |")
				print("| X X O |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   X |")
				print("| X X O |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O   X |")
				print("| X X   |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O X |")
			print("|   X   |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("|   X   |")
			print("| O O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("|   X   |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("|   X X |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   O X |")
				print("| O X   |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O X   |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   O X |")
				print("|   X O |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("|   X O |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|     X |")
			print("| O X   |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     X |")
			print("| O X X |")
			print("| O O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   X |")
				print("| O X X |")
				print("| O O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O X |")
				print("| O X X |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O X X |")
				print("| O O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| X O X |")
					print("| O X X |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|     X |")
				print("| O X X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("|     X |")
			print("|   X O |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X X |")
			print("|   X O |")
			print("| O O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X X |")
				print("|   X O |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("|   X O |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| O X X |")
					print("| O X O |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   X X |")
				print("| O X O |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X X |")
				print("| O X O |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X X |")
					print("| O X O |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   X X |")
				print("|   X O |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|     X |")
			print("|   X   |")
			print("| O O O |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,3
	if cell == "33":
		print("New O on 3,3:")
		print("- - - - -")
		print("|     X |")
		print("|       |")
		print("| O   O |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|     X |")
		print("|   X   |")
		print("| O   O |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O   X |")
			print("|   X   |")
			print("| O   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X X |")
			print("|   X   |")
			print("| O   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O X X |")
				print("| O X   |")
				print("| O   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X X |")
				print("|   X O |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X X O |")
				print("| O   O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O X X |")
					print("| X X O |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O X X |")
				print("|   X   |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O X |")
			print("|   X   |")
			print("| O   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("|   X   |")
			print("| O X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("|   X   |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X   |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   O X |")
				print("| O X   |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O X   |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   O X |")
				print("|   X O |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("|   X O |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|     X |")
			print("| O X   |")
			print("| O   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   X |")
			print("| O X   |")
			print("| O   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O X |")
				print("| O X   |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O X   |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| X   X |")
				print("| O X O |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X X |")
				print("| O X O |")
				print("| O   O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| X   X |")
				print("| O X   |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("|     X |")
			print("|   X O |")
			print("| O   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     X |")
			print("| X X O |")
			print("| O   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   X |")
				print("| X X O |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   X |")
				print("| X X O |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O X |")
				print("| X X O |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| X X O |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O O X |")
					print("| X X O |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|     X |")
				print("| X X O |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|     X |")
			print("|   X   |")
			print("| O O O |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		
		print("wrong cell!")
		quit()
	
	print("wrong cell!")
	quit()
#what happens if player goes 2,3
if cell == "23":
	print("New O on 2,3:")
	print("- - - - -")
	print("|       |")
	print("|       |")
	print("|   O   |")
	print("- - - - -")
	
	print("Enemy turn:")
	print("- - - - -")
	print("|   X   |")
	print("|       |")
	print("|   O   |")
	print("- - - - -")
	
	cell = input("Your turn:")
	#what happens if player goes 1,1
	if cell == "11":
		print("New O on 1,1:")
		print("- - - - -")
		print("| O X   |")
		print("|       |")
		print("|   O   |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| O X X |")
		print("|       |")
		print("|   O   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("| O X X |")
			print("| O     |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X X |")
			print("| O X   |")
			print("|   O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X X |")
				print("| O X O |")
				print("|   O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O X O |")
				print("| X O   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O X X |")
				print("| O X   |")
				print("| O O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X X |")
				print("| O X   |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O X   |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("| O X X |")
			print("|   O   |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X X |")
			print("|   O   |")
			print("|   O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O X X |")
				print("| O O   |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O O X |")
				print("|   O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X X |")
				print("|   O O |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("|   O O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| O X X |")
					print("| O O O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O X X |")
				print("|   O   |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X O   |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O X X |")
					print("| X O O |")
					print("| O O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X X |")
					print("| X O O |")
					print("| O O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("| O X X |")
			print("|     O |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X X |")
			print("|     O |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O X X |")
				print("| O   O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O   O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X X |")
					print("| O O O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X X |")
				print("|   O O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("|   O O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| O X X |")
					print("| O O O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X X |")
				print("|     O |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X   O |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X X |")
					print("| X O O |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("| O X X |")
			print("|       |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X X |")
			print("| X     |")
			print("| O O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X X |")
				print("| X O   |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X O X |")
				print("| O O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X X |")
					print("| X O X |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X X |")
				print("| X   O |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X X O |")
				print("| O O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X X |")
					print("| X X O |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X X |")
				print("| X     |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("| O X X |")
			print("|       |")
			print("|   O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X X |")
			print("|   X   |")
			print("|   O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O X X |")
				print("| O X   |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O X   |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X X |")
				print("|   X O |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("|   X O |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O X X |")
				print("|   X   |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,1
	if cell == "31":
		print("New O on 3,1:")
		print("- - - - -")
		print("|   X O |")
		print("|       |")
		print("|   O   |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   X O |")
		print("|       |")
		print("| X O   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O X O |")
			print("|       |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X O |")
			print("|       |")
			print("| X O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O X O |")
				print("| O     |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O   X |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X O |")
				print("|   O   |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("|   O X |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X O |")
				print("|     O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("|   X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|   X O |")
			print("| O     |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("| O X   |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("| O X   |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O X   |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   X O |")
				print("| O X O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| O X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   X O |")
				print("| O X   |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| O X X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O X X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|   X O |")
			print("|   O   |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X O |")
			print("|   O   |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X X O |")
				print("| O O   |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O O X |")
				print("| X O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| X X O |")
				print("|   O O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| X O O |")
				print("| X O   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X X O |")
				print("|   O   |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("|   O X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("|   X O |")
			print("|     O |")
			print("| X O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X O |")
			print("|     O |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X X O |")
				print("| O   O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O X O |")
				print("| X O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| X X O |")
					print("| O X O |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| X X O |")
				print("|   O O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| X O O |")
				print("| X O   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X X O |")
				print("|     O |")
				print("| X O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|   X O |")
			print("|       |")
			print("| X O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("|   X   |")
			print("| X O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("|   X   |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("|   X X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| O X O |")
					print("| O X X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   X O |")
				print("| O X   |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| O X X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O X X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   X O |")
				print("|   X O |")
				print("| X O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 1,2
	if cell == "12":
		print("New O on 1,2:")
		print("- - - - -")
		print("|   X   |")
		print("| O     |")
		print("|   O   |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   X   |")
		print("| O     |")
		print("|   O X |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O X   |")
			print("| O     |")
			print("|   O X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X   |")
			print("| O X   |")
			print("|   O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O X O |")
				print("| O X   |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O X   |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X   |")
				print("| O X O |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X   |")
				print("| O X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O X   |")
				print("| O X   |")
				print("| O O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|   X O |")
			print("| O     |")
			print("|   O X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X O |")
			print("| O     |")
			print("|   O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| X X O |")
				print("| O O   |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O O X |")
				print("|   O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| X X O |")
				print("| O   O |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O X O |")
				print("|   O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X X O |")
				print("| O     |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O   X |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|   X   |")
			print("| O O   |")
			print("|   O X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X X |")
			print("| O O   |")
			print("|   O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X X |")
				print("| O O   |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O O   |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,2
				if cell == "32":
					print("New O on 3,2:")
					print("- - - - -")
					print("| O X X |")
					print("| O O O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   X X |")
				print("| O O O |")
				print("|   O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   X X |")
				print("| O O   |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X X |")
				print("| O O   |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("|   X   |")
			print("| O   O |")
			print("|   O X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X   |")
			print("| O   O |")
			print("| X O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X   |")
				print("| O   O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X   |")
				print("| O X O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X O |")
					print("| X O X |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   X O |")
				print("| O   O |")
				print("| X O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O   O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X X O |")
					print("| O O O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   X   |")
				print("| O O O |")
				print("| X O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|   X   |")
			print("| O     |")
			print("| O O X |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X X |")
			print("| O     |")
			print("| O O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X X |")
				print("| O     |")
				print("| O O X |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   X X |")
				print("| O O   |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X X |")
				print("| O O   |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   X X |")
				print("| O   O |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X X |")
				print("| O   O |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,2
	if cell == "22":
		print("New O on 2,2:")
		print("- - - - -")
		print("|   X   |")
		print("|   O   |")
		print("|   O   |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   X   |")
		print("|   O X |")
		print("|   O   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O X   |")
			print("|   O X |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X   |")
			print("|   O X |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O X O |")
				print("|   O X |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X O X |")
				print("| X O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X O |")
					print("| X O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O X   |")
				print("| O O X |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O O X |")
				print("| X O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X X |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X   |")
				print("|   O X |")
				print("| X O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|   X O |")
			print("|   O X |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X O |")
			print("|   O X |")
			print("|   O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X X O |")
				print("| O O X |")
				print("|   O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O O X |")
				print("|   O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X X O |")
				print("|   O X |")
				print("| O O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X X O |")
				print("|   O X |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("|   O X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|   X   |")
			print("| O O X |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X   |")
			print("| O O X |")
			print("|   O X |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X   |")
				print("| O O X |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O O X |")
				print("|   O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   X O |")
				print("| O O X |")
				print("|   O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O O X |")
				print("|   O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   X   |")
				print("| O O X |")
				print("| O O X |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X   |")
				print("| O O X |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|   X   |")
			print("|   O X |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X X |")
			print("|   O X |")
			print("| O O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X X |")
				print("|   O X |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("|   O X |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   X X |")
				print("| O O X |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X X |")
				print("| O O X |")
				print("| O O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   X X |")
				print("|   O X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|   X   |")
			print("|   O X |")
			print("|   O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X   |")
			print("|   O X |")
			print("| X O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X   |")
				print("|   O X |")
				print("| X O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   X O |")
				print("|   O X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("|   O X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   X   |")
				print("| O O X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X   |")
				print("| O O X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,2
	if cell == "32":
		print("New O on 3,2:")
		print("- - - - -")
		print("|   X   |")
		print("|     O |")
		print("|   O   |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| X X   |")
		print("|     O |")
		print("|   O   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("| X X O |")
			print("|     O |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X O |")
			print("|   X O |")
			print("|   O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X X O |")
				print("| O X O |")
				print("|   O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O X O |")
				print("|   O X |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X X O |")
				print("|   X O |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| X X O |")
				print("| O O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| X X O |")
					print("| X X O |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X X O |")
				print("|   X O |")
				print("|   O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("| X X   |")
			print("| O   O |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X X |")
			print("| O   O |")
			print("|   O   |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("| X X   |")
			print("|   O O |")
			print("|   O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X   |")
			print("|   O O |")
			print("| X O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| X X O |")
				print("|   O O |")
				print("| X O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("|   O O |")
				print("| X O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X X O |")
					print("| O O O |")
					print("| X O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X X   |")
				print("| O O O |")
				print("| X O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X X   |")
				print("|   O O |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X X |")
				print("|   O O |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("| X X   |")
			print("|     O |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X X |")
			print("|     O |")
			print("| O O   |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("| X X   |")
			print("|     O |")
			print("|   O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X X |")
			print("|     O |")
			print("|   O O |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 1,3
	if cell == "13":
		print("New O on 1,3:")
		print("- - - - -")
		print("|   X   |")
		print("|       |")
		print("| O O   |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   X   |")
		print("|     X |")
		print("| O O   |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O X   |")
			print("|     X |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X   |")
			print("| X   X |")
			print("| O O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O X O |")
				print("| X   X |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X   X |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X O |")
					print("| X O X |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X   |")
				print("| X O X |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X O X |")
				print("| O O   |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,3
				if cell == "33":
					print("New O on 3,3:")
					print("- - - - -")
					print("| O X X |")
					print("| X O X |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| O X   |")
				print("| X   X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|   X O |")
			print("|     X |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("| X   X |")
			print("| O O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("| X   X |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| X   X |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X O |")
					print("| X O X |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   X O |")
				print("| X O X |")
				print("| O O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   X O |")
				print("| X   X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|   X   |")
			print("| O   X |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X X |")
			print("| O   X |")
			print("| O O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X X |")
				print("| O   X |")
				print("| O O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   X X |")
				print("| O O X |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X X |")
				print("| O O X |")
				print("| O O   |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("|   X X |")
				print("| O   X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|   X   |")
			print("|   O X |")
			print("| O O   |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X   |")
			print("|   O X |")
			print("| O O   |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| X X O |")
				print("|   O X |")
				print("| O O   |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X X   |")
				print("| O O X |")
				print("| O O   |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X   |")
				print("| O O X |")
				print("| O O X |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| O O X |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,3
			if cell == "33":
				print("New O on 3,3:")
				print("- - - - -")
				print("| X X   |")
				print("|   O X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,3
		if cell == "33":
			print("New O on 3,3:")
			print("- - - - -")
			print("|   X   |")
			print("|     X |")
			print("| O O O |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,3
	if cell == "33":
		print("New O on 3,3:")
		print("- - - - -")
		print("|   X   |")
		print("|       |")
		print("|   O O |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   X X |")
		print("|       |")
		print("|   O O |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O X X |")
			print("|       |")
			print("|   O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X X |")
			print("| X     |")
			print("|   O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X X |")
				print("| X O   |")
				print("|   O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("| O X X |")
				print("| X   O |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X   O |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X X |")
					print("| X O O |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O X X |")
				print("| X     |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|   X X |")
			print("| O     |")
			print("|   O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X X |")
			print("| O     |")
			print("|   O O |")
			print("- - - - -")
			#Lose condition!
			
			print("oh nooo! You lost!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|   X X |")
			print("|   O   |")
			print("|   O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X X |")
			print("| X O   |")
			print("|   O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X X |")
				print("| X O   |")
				print("|   O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,2
			if cell == "32":
				print("New O on 3,2:")
				print("- - - - -")
				print("|   X X |")
				print("| X O O |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X X |")
				print("| X O O |")
				print("|   O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   X X |")
				print("| X O   |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,2
		if cell == "32":
			print("New O on 3,2:")
			print("- - - - -")
			print("|   X X |")
			print("|     O |")
			print("|   O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X X |")
			print("| X   O |")
			print("|   O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X X |")
				print("| X   O |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| X X O |")
				print("|   O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| O X X |")
					print("| X X O |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   X X |")
				print("| X O O |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X X |")
				print("| X O O |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X X |")
					print("| X O O |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   X X |")
				print("| X   O |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|   X X |")
			print("|       |")
			print("| O O O |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		
		print("wrong cell!")
		quit()
	
	print("wrong cell!")
	quit()
#what happens if player goes 3,3
if cell == "33":
	print("New O on 3,3:")
	print("- - - - -")
	print("|       |")
	print("|       |")
	print("|     O |")
	print("- - - - -")
	
	print("Enemy turn:")
	print("- - - - -")
	print("|       |")
	print("|     X |")
	print("|     O |")
	print("- - - - -")
	
	cell = input("Your turn:")
	#i hate my life...
	#what happens if player goes 1,1
	if cell == "11":
		print("New O on 1,1:")
		print("- - - - -")
		print("| O     |")
		print("|     X |")
		print("|     O |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| O     |")
		print("|     X |")
		print("|   X O |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("| O O   |")
			print("|     X |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O   |")
			print("|   X X |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O O O |")
				print("|   X X |")
				print("|   X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O O   |")
				print("| O X X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| O X X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| O X X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O O   |")
				print("|   X X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("|   X X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| O O X |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("| O   O |")
			print("|     X |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   O |")
			print("| X   X |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O O |")
				print("| X   X |")
				print("|   X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O   O |")
				print("| X O X |")
				print("|   X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O   O |")
				print("| X   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| X X X |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("| O     |")
			print("| O   X |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   X |")
			print("| O   X |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O X |")
				print("| O   X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O   X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O O X |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O   X |")
				print("| O O X |")
				print("|   X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O   X |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("| O     |")
			print("|   O X |")
			print("|   X O |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("| O     |")
			print("|     X |")
			print("| O X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O     |")
			print("| X   X |")
			print("| O X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O   |")
				print("| X   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X X |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O   O |")
				print("| X   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| X X X |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O     |")
				print("| X O X |")
				print("| O X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,1
	if cell == "21":
		print("New O on 2,1:")
		print("- - - - -")
		print("|   O   |")
		print("|     X |")
		print("|     O |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|   O X |")
		print("|     X |")
		print("|     O |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O O X |")
			print("|     X |")
			print("|     O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O O X |")
			print("|     X |")
			print("| X   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O O X |")
				print("| O   X |")
				print("| X   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O   X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O O X |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O O X |")
				print("|   O X |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O O X |")
				print("|     X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("|   X X |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|   O X |")
			print("| O   X |")
			print("|     O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("| O   X |")
			print("| X   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("| O   X |")
				print("| X   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O X X |")
				print("| X   O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   O X |")
				print("| O O X |")
				print("| X   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O O X |")
				print("| X   O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   O X |")
				print("| O   X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O   X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|   O X |")
			print("|   O X |")
			print("|     O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("|   O X |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("|   O X |")
				print("|   X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   O X |")
				print("| O O X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| O O X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O X |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O X |")
				print("|   O X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("|   O X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|   O X |")
			print("|     X |")
			print("| O   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("|     X |")
			print("| O X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("|     X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X   X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O O X |")
					print("| X O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   O X |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O X |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   O X |")
				print("|   O X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| X O X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O X |")
					print("| X O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|   O X |")
			print("|     X |")
			print("|   O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("| X   X |")
			print("|   O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("| X   X |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X X X |")
				print("|   O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   O X |")
				print("| X O X |")
				print("|   O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   O X |")
				print("| X   X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 3,1
	if cell == "31":
		print("New O on 3,1:")
		print("- - - - -")
		print("|     O |")
		print("|     X |")
		print("|     O |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|     O |")
		print("|     X |")
		print("|   X O |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O   O |")
			print("|     X |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   O |")
			print("|     X |")
			print("| X X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O O |")
				print("|     X |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O   O |")
				print("| O   X |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O   X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O   O |")
				print("|   O X |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O O |")
			print("|     X |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O O |")
			print("|     X |")
			print("| X X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O O |")
				print("|     X |")
				print("| X X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   O O |")
				print("| O   X |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| O X X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| O X X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   O O |")
				print("|   O X |")
				print("| X X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X O X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| X O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|     O |")
			print("| O   X |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("| O   X |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("| O   X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O   X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   X O |")
				print("| O O X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O O X |")
				print("|   X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   X O |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|     O |")
			print("|   O X |")
			print("|   X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("|   O X |")
			print("|   X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("|   O X |")
				print("|   X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   X O |")
				print("| O O X |")
				print("|   X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| O O X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("|   X O |")
				print("|   O X |")
				print("| O X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|     O |")
			print("|     X |")
			print("| O X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X O |")
			print("|     X |")
			print("| O X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X O |")
				print("|     X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("|   X X |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   X O |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   X O |")
				print("|   O X |")
				print("| O X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 1,2
	if cell == "12":
		print("New O on 1,2:")
		print("- - - - -")
		print("|       |")
		print("| O   X |")
		print("|     O |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|       |")
		print("| O   X |")
		print("| X   O |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O     |")
			print("| O   X |")
			print("| X   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O     |")
			print("| O X X |")
			print("| X   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O   |")
				print("| O X X |")
				print("| X   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| O X X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O O O |")
					print("| O X X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| O   O |")
				print("| O X X |")
				print("| X   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| O X X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| O O O |")
					print("| O X X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| O     |")
				print("| O X X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X   |")
				print("| O X X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O X X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O   |")
			print("| O   X |")
			print("| X   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O X |")
			print("| O   X |")
			print("| X   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O X |")
				print("| O   X |")
				print("| X   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| O X X |")
				print("| X   O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   O X |")
				print("| O O X |")
				print("| X   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| O O X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O X |")
					print("| O O X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|   O X |")
				print("| O   X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| O X X |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|     O |")
			print("| O   X |")
			print("| X   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     O |")
			print("| O X X |")
			print("| X   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   O |")
				print("| O X X |")
				print("| X   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X O |")
				print("| O X X |")
				print("| X   O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| O X O |")
					print("| O X X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O O |")
				print("| O X X |")
				print("| X   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| O X X |")
				print("| X X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O O |")
					print("| O X X |")
					print("| X X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|     O |")
				print("| O X X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X O |")
				print("| O X X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X O |")
					print("| O X X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| O X O |")
					print("| O X X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|       |")
			print("| O O X |")
			print("| X   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     X |")
			print("| O O X |")
			print("| X   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   X |")
				print("| O O X |")
				print("| X   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O X |")
				print("| O O X |")
				print("| X   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O O X |")
				print("| X   O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("|     X |")
				print("| O O X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   X |")
				print("| O O X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("|       |")
			print("| O   X |")
			print("| X O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     X |")
			print("| O   X |")
			print("| X O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   X |")
				print("| O   X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O   X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O X X |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O X |")
				print("| O   X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O   X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|     X |")
				print("| O O X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   X |")
				print("| O O X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,2
	if cell == "22":
		print("New O on 2,2:")
		print("- - - - -")
		print("|       |")
		print("|   O X |")
		print("|     O |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("| X     |")
		print("|   O X |")
		print("|     O |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("| X O   |")
			print("|   O X |")
			print("|     O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X O X |")
			print("|   O X |")
			print("|     O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X O X |")
				print("| O O X |")
				print("|     O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O O X |")
				print("|   X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X O X |")
				print("|   O X |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("|   O X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| X O X |")
				print("|   O X |")
				print("|   O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("| X   O |")
			print("|   O X |")
			print("|     O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   O |")
			print("| X O X |")
			print("|     O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O O |")
				print("| X O X |")
				print("|     O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X O X |")
				print("| X   O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X   O |")
				print("| X O X |")
				print("| O   O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| X   O |")
				print("| X O X |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   O |")
				print("| X O X |")
				print("| X O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("| X     |")
			print("| O O X |")
			print("|     O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X   |")
			print("| O O X |")
			print("|     O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| X X O |")
				print("| O O X |")
				print("|     O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O O X |")
				print("| X   O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X X   |")
				print("| O O X |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X   |")
				print("| O O X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| X X   |")
				print("| O O X |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X X |")
				print("| O O X |")
				print("|   O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("| X     |")
			print("|   O X |")
			print("| O   O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   X |")
			print("|   O X |")
			print("| O   O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O X |")
				print("|   O X |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| X O X |")
				print("| O   O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,3
				if cell == "23":
					print("New O on 2,3:")
					print("- - - - -")
					print("| X O X |")
					print("| X O X |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X   X |")
				print("| O O X |")
				print("| O   O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   X |")
				print("| O O X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,3
			if cell == "23":
				print("New O on 2,3:")
				print("- - - - -")
				print("| X   X |")
				print("|   O X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,3
		if cell == "23":
			print("New O on 2,3:")
			print("- - - - -")
			print("| X     |")
			print("|   O X |")
			print("|   O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X X   |")
			print("|   O X |")
			print("|   O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| X X O |")
				print("|   O X |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("|   O X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,2
				if cell == "12":
					print("New O on 1,2:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X X   |")
				print("| O O X |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X   |")
				print("| O O X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X X   |")
				print("|   O X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 1,3
	if cell == "13":
		print("New O on 1,3:")
		print("- - - - -")
		print("|       |")
		print("|     X |")
		print("| O   O |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|       |")
		print("|     X |")
		print("| O X O |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O     |")
			print("|     X |")
			print("| O X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O   X |")
			print("|     X |")
			print("| O X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#i hate my life...
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| O O X |")
				print("|     X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O X |")
				print("| X   X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| O O X |")
					print("| X O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O   X |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O   X |")
				print("|   O X |")
				print("| O X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O   |")
			print("|     X |")
			print("| O X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   O   |")
			print("|   X X |")
			print("| O X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O O   |")
				print("|   X X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O O   |")
				print("| X X X |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   O O |")
				print("|   X X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O O |")
				print("| X X X |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|   O   |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   O X |")
				print("| O X X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O O X |")
					print("| O X X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 3,1
		if cell == "31":
			print("New O on 3,1:")
			print("- - - - -")
			print("|     O |")
			print("|     X |")
			print("| O X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     O |")
			print("| X   X |")
			print("| O X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   O |")
				print("| X   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O   O |")
				print("| X X X |")
				print("| O X O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O O |")
				print("| X   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O O |")
				print("| X   X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X O O |")
					print("| X O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|     O |")
				print("| X O X |")
				print("| O X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|       |")
			print("| O   X |")
			print("| O X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|   X   |")
			print("| O   X |")
			print("| O X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O X   |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("|   X O |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X O |")
				print("| O   X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X X O |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("|   X   |")
				print("| O O X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X X |")
				print("| O O X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|       |")
			print("|   O X |")
			print("| O X O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X     |")
			print("|   O X |")
			print("| O X O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O   |")
				print("|   O X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O   |")
				print("| X O X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 3,1
				if cell == "31":
					print("New O on 3,1:")
					print("- - - - -")
					print("| X O O |")
					print("| X O X |")
					print("| O X O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 3,1
			if cell == "31":
				print("New O on 3,1:")
				print("- - - - -")
				print("| X   O |")
				print("|   O X |")
				print("| O X O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X     |")
				print("| O O X |")
				print("| O X O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X   X |")
				print("| O O X |")
				print("| O X O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,1
				if cell == "21":
					print("New O on 2,1:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("Enemy turn:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| O X O |")
					print("- - - - -")
					
					print("It's a tie!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		
		print("wrong cell!")
		quit()
	#what happens if player goes 2,3
	if cell == "23":
		print("New O on 2,3:")
		print("- - - - -")
		print("|       |")
		print("|     X |")
		print("|   O O |")
		print("- - - - -")
		
		print("Enemy turn:")
		print("- - - - -")
		print("|     X |")
		print("|     X |")
		print("|   O O |")
		print("- - - - -")
		
		cell = input("Your turn:")
		#what happens if player goes 1,1
		if cell == "11":
			print("New O on 1,1:")
			print("- - - - -")
			print("| O   X |")
			print("|     X |")
			print("|   O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| O X X |")
			print("|     X |")
			print("|   O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| O X X |")
				print("| O   X |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| O X X |")
				print("| O X X |")
				print("|   O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| O X X |")
					print("| O X X |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| O X X |")
				print("|   O X |")
				print("|   O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| O X X |")
				print("|     X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,1
		if cell == "21":
			print("New O on 2,1:")
			print("- - - - -")
			print("|   O X |")
			print("|     X |")
			print("|   O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X O X |")
			print("|     X |")
			print("|   O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("| X O X |")
				print("| O   X |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O X X |")
				print("|   O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,3
				if cell == "13":
					print("New O on 1,3:")
					print("- - - - -")
					print("| X O X |")
					print("| O X X |")
					print("| O O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| X O X |")
				print("|   O X |")
				print("|   O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X O X |")
				print("|     X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,2
		if cell == "12":
			print("New O on 1,2:")
			print("- - - - -")
			print("|     X |")
			print("| O   X |")
			print("|   O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("| X   X |")
			print("| O   X |")
			print("|   O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("| X O X |")
				print("| O   X |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X O X |")
				print("| O   X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 2,2
				if cell == "22":
					print("New O on 2,2:")
					print("- - - - -")
					print("| X O X |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			#what happens if player goes 2,2
			if cell == "22":
				print("New O on 2,2:")
				print("- - - - -")
				print("| X   X |")
				print("| O O X |")
				print("|   O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("| X X X |")
				print("| O O X |")
				print("|   O O |")
				print("- - - - -")
				#Lose condition!
				
				print("oh nooo! You lost!")
				quit()
			#what happens if player goes 1,3
			if cell == "13":
				print("New O on 1,3:")
				print("- - - - -")
				print("| X   X |")
				print("| O   X |")
				print("| O O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 2,2
		if cell == "22":
			print("New O on 2,2:")
			print("- - - - -")
			print("|     X |")
			print("|   O X |")
			print("|   O O |")
			print("- - - - -")
			
			print("Enemy turn:")
			print("- - - - -")
			print("|     X |")
			print("|   O X |")
			print("| X O O |")
			print("- - - - -")
			
			cell = input("Your turn:")
			#what happens if player goes 1,1
			if cell == "11":
				print("New O on 1,1:")
				print("- - - - -")
				print("| O   X |")
				print("|   O X |")
				print("| X O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 2,1
			if cell == "21":
				print("New O on 2,1:")
				print("- - - - -")
				print("|   O X |")
				print("|   O X |")
				print("| X O O |")
				print("- - - - -")
				#Win condition!
				print("congrats! You won!")
				quit()
			#what happens if player goes 1,2
			if cell == "12":
				print("New O on 1,2:")
				print("- - - - -")
				print("|     X |")
				print("| O O X |")
				print("| X O O |")
				print("- - - - -")
				
				print("Enemy turn:")
				print("- - - - -")
				print("|   X X |")
				print("| O O X |")
				print("| X O O |")
				print("- - - - -")
				
				cell = input("Your turn:")
				#what happens if player goes 1,1
				if cell == "11":
					print("New O on 1,1:")
					print("- - - - -")
					print("| O X X |")
					print("| O O X |")
					print("| X O O |")
					print("- - - - -")
					#Win condition!
					print("congrats! You won!")
					quit()
				
				print("wrong cell!")
				quit()
			
			print("wrong cell!")
			quit()
		#what happens if player goes 1,3
		if cell == "13":
			print("New O on 1,3:")
			print("- - - - -")
			print("|     X |")
			print("|     X |")
			print("| O O O |")
			print("- - - - -")
			#Win condition!
			print("congrats! You won!")
			quit()
		
		print("wrong cell!")
		quit()
	
	print("wrong cell!")
	quit()

print("wrong cell!")
quit()
