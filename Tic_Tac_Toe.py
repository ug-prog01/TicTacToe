import itertools
from colorama import Fore, Back, Style, init
init()

board = []
player_current = 1
loss = False
win = True
game_state = loss
player = itertools.cycle([1,2])
next(player)
re = False


def reset_board():
	global board,game_state,player_current
	board = [[0 for i in range(game_size)] for i in range(game_size)]
	player_current = 1
	game_state = False


def player_move(board_map, player=0, row=0, col=0, just_display=False):
	try:
		if not just_display:
			if board_map[row][col] == 0:
				board_map[row][col] = player
				change_player()
			else:
				print('Cannot change position! Choose again!: ')
				return board_map

		s = "   " + "  ".join([str(i) for i in range(len(board_map))])
		print(s)
		for count, row in enumerate(board_map):
			colored_row = ""
			for item in row:
				if item == 0:
					colored_row += "   "
				elif item == 1:
					colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
				elif item == 2:
					colored_row += Fore.RED + ' O ' + Style.RESET_ALL
			print(count, colored_row)
			print()
		if not decide_win(board_map):
			return board_map
		else:
			global board
			return board

	except IndexError as e:
		print("Error: Incorrect position chosen", e)
		return board_map

	except Exception as e:
		print("Something went wrong", e)
		return board_map

def change_player():
	global player_current
	player_current = next(player)

def decide_win(board_map):
	#Horizontal
	for row in board_map:
		if check_span(row):
			return True

	#Vertical
	for col in range(len(board_map)):
		check = []

		for row in board_map:
			check.append(row[col])
		if check_span(check):
			return True

	#Diagonal
	diags = []

	for col, row in enumerate(reversed(range(len(board_map)))):
		diags.append(board_map[row][col])
	if check_span(diags):
		return True

	diags = []

	for col, row in enumerate(range(len(board_map))):
		diags.append(board_map[row][col])
	if check_span(diags):
		return True

	return False

def check_span(lst=[]):
	if lst.count(lst[0]) == len(lst) and lst[0] != 0:
		print(f"Winner -- Player {lst[0]}!!")
		global game_state,win,re
		game_state = win
		typ = input('Wanna play again?!(y/n): ')
		if typ.lower() == "y":
			re = True
			reset_board()
		else:
			re = False
			global playing
			playing = False
		return True
	else:
		return False


playing = True

while playing:
	game_size = int(input('Enter the grid size of the game: '))
	board = [[0 for i in range(game_size)] for i in range(game_size)]
	board = player_move(board, just_display=True)
	while game_state != win or re:
		print(f"-----Player {player_current}'s turn-----")
		row_choice = int(input('Enter the row number(0, 1, 2): '))
		col_choice = int(input('Enter the column number(0, 1, 2): '))
		board = player_move(board, player_current, row_choice, col_choice)
		draw_counter = 0
		for row in board:
			for col in row:
				if(col != 0):
					draw_counter += 1
		if(draw_counter == game_size * game_size):
			print("It's a draw!")
			typ = input('Wanna play again?!(y/n): ')
			if typ.lower() == "y":
				reset_board()
			else:
				game_state = win
				re = False
				playing = False