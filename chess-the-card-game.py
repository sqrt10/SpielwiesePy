
"""
Chess - The Card Game.

Welcome to another random challenge inspired by @ChessSimp.
You play chess but have limited options like in a card game.
If you want to move a piece or pawn, you must play the card first.

This is the script that uses the command line to simulate which cards
you hold in your hand, updated by which are played and drawn.

License:
As long as you retain this notice you can do whatever you want with this.
It would be nice if you give a shout-out to @ChessSimp and @SimpleFlips.
This file is part of https://github.com/sqrt10/spielwiese-py.
"""

from random import randrange
from time import sleep

### Game settings

# number of cards in a hand
maxHandSize = 5 # If you are not a coward, choose 4

# max amount of moves you have to win the game
maxNumberOfMoves = 40

# Names of all cards in your hand.
# If you initialize this non-empty, e.g. `[ "pawn" ]`,
# you start with a pawn, and the others are random.
handCards = [ "pawn" ]

### Ui settings

# print to console which card you pick
echoPick = True
# print to console which card you draw
echoDraw = True

### Game Setup

# names of all different pieces (and pawns)
pieces = [ "king", "queen", "rook", "bishop", "horsey", "pawn" ]
# probability of each piece, sorted like pieces
probabilities = [ 1, 1, 2, 2, 2, 8 ]
# cumulated sum of probabilities, sorted like pieces
probCum = []
# total sum of probabilities
probSum = 0

for prob in probabilities:
	probSum += prob
	probCum.append( probSum )

### Utility Functions

def drawCard( suppressEcho = False ):
	"""Adds a random piece to the hand cards."""
	randNo = randrange( 0, probSum ) # random number to compare with probCum
	for iPiece in range( len( pieces ) ):
		if randNo < probCum[ iPiece ]:
			break # a card was chosen, leave loop

	drawnPiece = pieces[ iPiece ]
	if not( suppressEcho ) and echoDraw:
		print( "You draw a " + drawnPiece + ".", end="" )
	handCards.append( drawnPiece )

def showHand():
	"""Prints the hand to console."""
	print( "Your current hand is:\t", end="" )
	print( str( handCards ).replace( "[", "" ).replace( "]", "" ).replace( "'", "" ) )

def pickCard( printHelp = False ):
	"""Expects user input and removes the selected card from the hand."""
	iHandCard = -1 # index in handCards of user selected piece; -1 : no valid user input
	while True: # will only finish with when a valid hand card is picked
		print( "Choose a card to play", end="" )
		if printHelp:
			print( " (type b/h/k/p/q/r)", end="" )
		print( ": ", end="" )
		userInput = input()
		if userInput == "":
			print( " - Please type a letter, try again." )
			continue
		key = userInput[ 0 ].lower()
		# Check with of the pieces has a matching first character
		for iHandCardTest in range( len( handCards ) ):
			if key == handCards[ iHandCardTest ][ 0 ]:
				iHandCard = iHandCardTest
				break

		if iHandCard == -1:
			print( " - This is not a valid hand card, try again." )
			continue # repeat the loop
		else:
			break # leave the loop

	if echoPick:
		print( "You play a " + handCards[ iHandCard ] + ". ", end="" )
	handCards.pop( iHandCard )

def main():
	"""Provides the interface in the console window."""

	# Print the rules
	print( "\n\nChess - The Card Game." )
	print( "\nWelcome to another random challenge inspired by @ChessSimp." )
	print( "You play chess, but have limited options like in a card game." )
	print( "If you want to move a piece or pawn, you must play the card first.\n" )
	print( "You start with a pawn and another " + str( maxHandSize-1 ) + " random cards." )
	print( "After you play a card, you draw another random card." )
	print( "The probability of each card is proportional to its frequency in the" )
	print( "starting position, i.e. drawing a pawn is eight times more likely" )
	print( "than drawing a queen and four times more likely than drawing a rook." )
	print( "The maximum amount of moves you have to win the game is " + str( maxNumberOfMoves ) + "." )

	firstPick = True

	# Draw until your hand is full
	while len( handCards ) < maxHandSize:
		drawCard( True )

	# main loop
	for iMove in range( maxNumberOfMoves ):
		print( "" ) # blank for formatting

		handCards.sort()
		showHand()

		pickCard( firstPick )
		firstPick = False

		drawCard()

		if echoPick or echoDraw:
			print( "" )

		if iMove == ( maxNumberOfMoves - 1 - 10 ):
			print( "You have 10 moves left." )
		elif iMove == ( maxNumberOfMoves - 1 - 5 ):
			print( "You have 5 moves left." )
		elif iMove == ( maxNumberOfMoves - 1 - 1 ):
			print( "You have one move left." )

	print( "\nMaximum amount of moves reached." )
	print( "If you haven't won yet, you failed the challenge." )

if __name__ == "__main__":
	main()
