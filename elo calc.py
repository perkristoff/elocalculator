import math

# probability function
def probability(rating1, rating2):
    return 1.0 / (1 + math.pow(10, (rating1 - rating2) / 400.0))

# elo function
def elo_rating(Ra, Rb, K, outcome):
    # winning probabilities
    Pb = probability(Ra, Rb)
    Pa = probability(Rb, Ra)

    # update ELOs
    Ra = Ra + K * (outcome - Pa)
    Rb = Rb + K * ((1 - outcome) - Pb)

    # print updated ratings
    print("Updated Ratings:")
    print(f"Ra = {Ra} Rb = {Rb}")

# ELO ratings
Ra = 1200
Rb = 1000

# constant
K = 30

# Outcome: 1 for Player A win, 0 for Player B win, 0.5 for draw
outcome = 1

# Function call
elo_rating(Ra, Rb, K, outcome)
