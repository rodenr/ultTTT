# Ultimate Tic-Tac-Toe Project
# 
# A 3x3 grid of 3x3 TTT games is the playing field.
# Winning 3 TTT games in a row on the larger 3x3 grid
# is how to win the game.
#
# First player can pick any of 81 positions to play.
# All corresponding moves will on an individual TTT game
# will map to the new TTT board for the next players turn.

# If the designated TTT board the next move is mapped to
# is full, then any open space is now free to be chosen.
# -------------------------------------------------------
from sys import maxsize
###################################################################
def main():
	# initializes the game board and the array to track wins
	game_board = [[ '-' for x in range(9)] for x in range(9)]

	win_track = ['-' for x in range(9)]
	print(game_board)
	print()
	print(win_track)

	print("Hello, let's play ultimate tic tac toe")
	coin_flip()
	print("I go first, let's begin")
	
	game_board[4][4] = "X"
	move_count = 1
	previous_move = 4
	# while loop runs for duration of game
	while True:

		# Checks to see if either X or O has won the overall game
		if is_won(win_track, 'X'):
			print('X wins')
			break
		if is_won(win_track, 'O'):
			print('O wins')
			break	
		print("pending")
		
		if move_count % 2 == 0:
			previous_move = bot_move(game_board, win_track, previous_move)
			move_count += 1
			for game in game_board:
				print(game)
		else:
			previous_move = player_move(game_board, win_track, previous_move)
			move_count += 1
			print(previous_move)
			for game in game_board:
				print(game)

####################################################################
# Checks for a winning combination of tic tac toe solutions
#
# this function can be run on the big game board or
# on any of the little game boards
def is_won(board, player):
	if board[0] == player and board[1] == player and board[2] == player:
		return True

	if board[3] == player and board[4] == player and board[5] == player:
		return True

	if board[8] == player and board[7] == player and board[6] == player:
		return True

	if board[0] == player and board[3] == player and board[6] == player:
		return True

	if board[1] == player and board[4] == player and board[7] == player:
		return True

	if board[2] == player and board[5] == player and board[8] == player:
		return True

	if board[0] == player and board[4] == player and board[8] == player:
		return True

	if board[6] == player and board[4] == player and board[2] == player:
		return True

###################################################################
def coin_flip():
	while True:
		coin_toss = input("I'll flip a coin to go first, heads or tails? enter H/T: ")
		if coin_toss.upper() == "H":
			print("coin lands tails")
			break
		elif coin_toss.upper() == "T":
			print("coin lands heads")
			break
		else:
			print("cut that out you bozo, enter H/T")

####################################################################
# Function accepts user input, updates game_board, checks to see if
# the move wins a game on a miniboard
def player_move(game_board, win_track, previous_move):

	print("you have to play on mini-board", previous_move+1)

	# accept and validate user input for next move
	while True:
		mini_game_move = input("enter 1-9 to make your move: ")
		if mini_game_move.isnumeric() and int(mini_game_move)-1 in range(0,8):
			mini_game_move = int(mini_game_move)-1
			

			# Check to see if move is available
			if game_board[ previous_move ][ mini_game_move ] == "-":
				
				#move is good, break out of while loop
				break

		print("cut it out bozo, invalid move \n")


	# update game_board  and previous move with player input
	game_board[ previous_move ][ mini_game_move ] = "O"
	return mini_game_move

############################################################################

# Determine if it is opening, middle, or end game and make appropriate move
def bot_move(game_board, win_track, previous_move):
	# check if in opening
	initial_x_count = 0
	for game in game_board:
		if game[4] == "X":
			initial_x_count += 1
	if initial_x_count < 7:
		game_board[ previous_move ][4] = "X"
		return 4
	else:
		return 5
####################################################################


if __name__ == "__main__":
	main()
