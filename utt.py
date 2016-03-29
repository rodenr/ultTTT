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


####################################################################
def minimax( node, depth, alpha, beta, max_player):
	# Check to see if the large grid has a winner
	# or if we have reached a terminal node regardless of winner
	if depth == 0 or terminal_node(win_track):
		# figure out how to return heuristic


	# maximizing play
	if max_player:
		v = -maxsize
		# establish list of nodes
		# for each child of node:
			v = max( minimax(child, depth-1, alpha, beta, FALSE), v)
			alpha = max(alpha, v)
			if beta <= alpha:
				break
		return v
		
	else:
		v = maxsize
		# estblish list of nodes
		# for each child of node:
			v = min( minimax(child, depth-1, alpha, beta, TRUE), v)
			beta = min(beta, v)
			if beta <= alpha:
				break
		return v
###################################################################
if __name__ == "__main__":
	main()
