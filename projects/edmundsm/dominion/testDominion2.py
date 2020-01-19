# -*- coding: utf-8 -*-
"""
Modified on Wed Jan 15 12:51 2020

@author: Martin Edmunds
"""

# import Dominion
# import random
# from collections import defaultdict

from testUtility import *

# Get player names
player_names = ["*Annie","*Ben","*Carla"]

# calculate number of victory cards and curses
nV = GetVictoryCount(player_names)
nC = GetCurseCount(player_names)

# Select the possible cards to be included in the game
box = SetupBoxes(nV)

# Set up the supply
supply_order = SetSupplyOrder()
supply = PopulateSupply(box, nV, nC, len(player_names))

# testing overrides

# initialize the trash
trash = []

# initialize player objects
players = ConstructPlayers(player_names)

#Play the game
PlayGame(supply, supply_order, players, trash)

#Final score
GetScore(players)