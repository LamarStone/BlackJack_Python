import random 

def generateCard():
    card = ["ace" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10" , "jack" , "queen" , "king"]
    number = random.randint(0 , 12)
    return card[number]

def calculatehand(hand , generatedcard):
    cards = {"ace" : 1 , "2" : 2 , "3" : 3 , "4" : 4 , "5" : 5 , "6" : 6 , "7" : 7 , "8" : 8 , "9" : 9 , "10" : 10 , "jack" : 10 , "queen" : 10 , "king" : 10}
    if hand < 10:
        cards["ace"] = 11
    hand += cards.get(generatedcard)
    return hand

def gameLoop():
    dealerHand = 0
    playerHand = 0
    newDealercard = generateCard()
    newPlayercard = generateCard()
    print(f"player :  {calculatehand(playerHand , newPlayercard)}")
    print(f"dealer :  {calculatehand(dealerHand , newDealercard)}")
    




if __name__=='__main__':
    gameLoop()