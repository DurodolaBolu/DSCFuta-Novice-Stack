import random
def dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return (dice1, dice2)

playy1 = []
playy2 = []
count = 1
while count <= 4:
    play1 = dice()
    play2 = dice()
    playy1.append(play1)
    playy2.append(play2)
    print(f"player 1 rolls {play1} and player 2 rolls {play2}")
    
    if sum(play1) == 2 or sum(play2) == 2:
        break
    count += 1
pla1 = []
for x in playy1:
    r = sum(x)
    pla1.append(r)
#print(pla1)
sol = sum(pla1)
print(f"Player 1 has a total of {sol} points")
pla2 = []
for x in playy2:
    r = sum(x)
    pla2.append(r)
#print(pla1)
son = sum(pla2)
print(f"Player 2 has a total of {son} points")
w1 = "Player 1 won the game"
w2 = "Player 2 won the game"
w3 = "It's a tie!!"
if sum(play1) == 2:
    print(f"{w1} because he got a (1, 1)")
    
elif sum(play2) == 2:
    print(f"{w2} because he got a (1, 1)")
    
elif sol > son:
    print(w1)

elif son > sol:
    print(w2)

elif son == sol:
    print(w3)


#print(playy1)
#print(playy2)