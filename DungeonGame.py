import random 


CELLS = [(0,0),(0,1),(0,2),
		 (1,0),(1,1),(1,2),
		 (2,0),(2,1),(2,2)]



def draw_Map(player):
	print(' _ _ _ ')
	tile = '|{}'

	for idx, cell in enumerate(CELLS):
		if idx in [0,1,3,4,6,7]:
			if cell == player:
				print(tile.format('X'),end ='')
			else:
				print(tile.format('_'),end='')
		else:
			if cell == player:
				print(tile.format('x|'))
			else:
				print(tile.format('_|'))
def get_Location():
	#monster = random 
	#door = random 
	#start = random 
	monster = random.choice(CELLS)
	door = random.choice(CELLS)
	start = random.choice(CELLS)

	if monster == door or monster == start or door == start:
		return get_Location()

	return monster, door, start
	
	# if monster,door, or start are the same, do it again

	#return monster, door, start

def move_player(player, move):
	x,y = player

	#Get player's position
	#If move is LEFT, y - 1
	#If move is RIGHT, y + 1
	#If move is UP, x - 1
	#If move is DOWN, x + 1
	if move == 'LEFT':
		y-=1
	elif move == 'RIGHT':
		y+=1
	elif move == 'UP':
		x-=1
	elif move == 'DOWN':
		x+=1


	return x,y

def get_moves(player):
	#player = (x,y)
	moves = ['LEFT','RIGHT','UP','DOWN']

	if player[1] == 0:
		moves.remove('LEFT')
	if player[1] == 2:
		moves.remove('RIGHT')
	if player[0] == 0:
		moves.remove('UP')
	if player[0] == 2:
		moves.remove('DOWN')

	return moves


monster, door, player = get_Location()
print("Welcome to the dungeon!")

while True:
	moves = get_moves(player)
	print("You're currently in room {}".format(player)) #fill in with player move
	draw_Map(player)
	print("You can move {}".format(moves)) #fill in with available moves
	print("Enter QUIT to quit")

	move = input("> ")
	move = move.upper()

	if move == "QUIT":
		break

	if move in moves:
		player = move_player(player,move)
	else:
		print("** Walls are hard, stop walking into them! **")
		continue

	if player == door:
		print("You Escaped!")
		break
	elif player == monster:
		print("You've been eaten!")
		break

#Logic Statements for moves



