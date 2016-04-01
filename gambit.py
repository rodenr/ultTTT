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

# Hold onto the last moves of both the bot and player

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
	

	# bot plays first before entering loop
	game_board[4][4] = "X"
	move_count = 1

	# make last_move dictionary with bot first move
	last_moves = {"bot":(4,4), "player":(10,10)}

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
			bot_move(game_board, win_track, last_moves)
			move_count += 1
			check_mini_boards( game_board, win_track, 'X')

			for game in game_board:
				print(game)
		else:
			player_move(game_board, win_track, last_moves)
			move_count += 1
			check_mini_boards( game_board, win_track, 'Y')

			for game in game_board:
				print(game)

####################################################################
# Checks the mini_boards to update win_track

def check_mini_boards( game_board, win_track, player):
	# If game is not already won, check if board is_won
	for i in range(0,9):
		game = game_board[i]
		if win_track[i] == "-" and is_won(game, player):
			# Since game was not previously won, update win_track
			win_track[i] = player

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
def player_move(game_board, win_track, last_moves):

	previous_move = last_moves["bot"][1]	

	print("you have to play on mini-board", previous_move+1)

	# accept and validate user input for next move
	while True:
		mini_game_move = input("enter 1-9 to make your move: ")
		if mini_game_move.isnumeric() and int(mini_game_move) in range(1,10):
			mini_game_move = int(mini_game_move)-1
			

			# Check to see if move is available
			if game_board[ previous_move ][ mini_game_move ] == "-":
				
				#move is good, break out of while loop
				break

		print("cut it out bozo, invalid move \n")


	# update game_board  and previous move with player input
	game_board[ previous_move ][ mini_game_move ] = "O"
	last_moves.update( {"player":(previous_move, mini_game_move)} )

############################################################################

# Determine if it is opening, middle, or end game and make appropriate move
def bot_move(game_board, win_track, last_moves):

	previous_move = last_moves["player"][1]

	open_move_map = {"0":8, "1":7, "2":6, "3":5, "5":3, "6":2, "7":1, "8":0}




	# Opening Game Strategy
	x_count = 0
	for game in game_board:
		for i in game:
			# Check for number of X's marked by bot
			if i == "X":
				x_count += 1
	if x_count < 8:
		# While in initial continue to select center of miniboards as X
		game_board[ previous_move ][4] = "X"
		last_moves.update( {"bot":( previous_move ,4 )} )


	



	#Middle Game Strategy

	# once X has selected the 8th center, select the mini_board square
	# that corresponds to the square that mini_board maps to on big_board
	elif x_count == 8:
		game_board[ previous_move ][ previous_move ] = "X"
		last_moves.update( {"bot":( previous_move, previous_move )} )


	# If player selects center piece on mini_board this maps to a full mini_board
	# this part of the gambit handles mapping it to the square opposite of the 
	# previous moves board on big_board
	elif previous_move == 4:
		previous_board_map = open_move_map[ str(last_moves["player"][0]) ]
		prev_bot_move  = last_moves["bot"][1]


		# if bot is sent to mini_board where it has already selected
		# the middle games move, finish off the MoFo, and win the mini board
		if game_board[ previous_board_map ][ prev_bot_move ] == "X":
			win_mini_board = open_move_map[ str(prev_bot_move) ]
			game_board[ previous_board_map ][ win_mini_board ] = "X"
			last_moves.update( {"bot":( previous_board_map, win_mini_board )} )

		else:
			game_board[ previous_board_map ][ prev_bot_move ] = "X"
			last_moves.update( {"bot":( previous_board_map, prev_bot_move )} )

	# keep using the square of the previous mini_board bot move
	else:
		print(last_moves)
		prev_bot_move = last_moves["bot"][1]
		if game_board[ previous_move ][ prev_bot_move ] == "X":
			win_mini_board = open_move_map[ str(prev_bot_move) ]
			game_board[ previous_move ][ win_mini_board ] = "X"
			last_moves.update( {"bot":( previous_move, win_mini_board )} )

		else:
			game_board[ previous_move ][ prev_bot_move ] = "X"
			last_moves.update( {"bot":( previous_move, prev_bot_move )} )


		
	

####################################################################


if __name__ == "__main__":
	main()
