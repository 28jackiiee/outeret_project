import os
import random
import time
def build():
    
    colors = ["Green", "Red", "Blue", "Yellow"]
    onlynums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    amount =  ["Draw Two", "Reverse", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    deck = []
    deck1 = []
    for color in colors:
        for num in amount:
            cardVal = "{} {}".format(color, num)
            deck.append(cardVal)
            if num != 0:
                deck.append(cardVal)
    for color in colors:
        for num in onlynums:
            cardVal = "{} {}".format(color, num)
            deck1.append(cardVal)
            if num != 0:
                deck1.append(cardVal)
    list_without_wilds = deck.copy()
    return list_without_wilds, deck1

def shuffle(deck):
    random.shuffle(deck)
    return deck

def assign(deck):
    ai = []
    human = []
    for i in range(5):
        num = random.randint(0,len(deck))
        ai.append(deck[num-1])
        del deck[num-1]
    for i in range(5):
        num = random.randint(0,len(deck))
        human.append(deck[num-1])
        del deck[num-1]
    return deck,human,ai
        

    

            

        
list_without_wilds,deck1 = build()
deck = shuffle(list_without_wilds)
deck,human,ai = assign(deck)

def uno():
    os.system('clear')
    print("This is a Game of Uno")
    time.sleep(3)
    os.system('clear')
    print('The Rules are Simple: Match either the number or the color. First to run out wins.')
    time.sleep(3)
    os.system('clear')
    print('There are also special cards. +2 gives 2 cards to the next player, and reverse skips the next players turn.')
    time.sleep(3)
    os.system('clear')
    print("You are playing with one other player. You are both given five cards.")
    time.sleep(3)
    os.system('clear')
    starting_card = deck1[random.randint(0,len(deck1))]
    starting_card_Split = starting_card.split(' ')
    startingcardnum = starting_card_Split[1]
    startingcardcolor = starting_card_Split[0]
    turn = 0
    print("The starting card is "+ starting_card)
    while True:
        while turn == 0:
            time.sleep(3)
            startingcardnum = str(startingcardnum)
            startingcardcolor = str(startingcardcolor)
            print('What Action Do You Want to Perform?')
            print("[1] Look at Cards\n[2] Play a Card\n[3] Draw a Card\n[4] Uno!\n[5] Forfeit\n<1 Integer> {Range: 1-5})")
            a = int(input())
            if a == 1:
                print(human)
            if a == 2:
                print("Enter the index of the card you want to play")
                inp = int(input())
                totalation = human[inp].split(' ')
                print(totalation)
                if (totalation[0] == startingcardcolor) and totalation[1]!="Reverse":
                    del human[inp]
                    print("It is now the AI's turn")
                    turn +=1
                elif (totalation[1] == startingcardnum) and totalation[1]!="Reverse":
                    del human[inp]
                    print("It is now the AI's turn")
                    turn +=1
                elif (totalation[1] == 'Reverse'):
                    print("It is your turn again")
            if a == 3:
                rando = random.randint(0,len(deck))
                human.append(deck[rando])
                print(human)
                del deck[rando]
            if a == 4 and len(human) ==1:
                print("You have 1 card left!")
            if a == 5:
                print("The Bot Wins!")
                return False
        
        final_card = totalation

        while turn ==1:
            os.system('clear')
            for amazing,i in enumerate(ai):
                
                i1 = i.split(' ')
                if turn ==1:
                    for thing in ai:
                        if final_card[0] == i1[0]:
                            print("The AI has played "+ i)
                            turn-=1
                            startingcardnum = i1[1]
                            startingcardcolor = i1[0]
                            del ai[amazing]
                            break
                if turn == 1:
                    for thingy in ai:
                        if final_card[1] == i1[1]:
                            turn-=1
                            print("The AI has played"+ i)
                            startingcardnum = i1[1]
                            startingcardcolor = i1[0]
                            del ai[amazing]
                            break
                if turn == 1:
                        item_color = i1[0]
                        item_number = i1[1]
                        if (item_color not in final_card[0]) and (item_number not in final_card[1]):
                            rando = random.randint(0,len(deck))
                            ai.append(deck[rando-1])
                            del deck[rando-1]

uno()