from flask import Flask, request, render_template
import os
import random
import time

app = Flask(__name__)

def build():
    colors = ["Green", "Red", "Blue", "Yellow"]
    amount =  ["Draw Two", "Reverse", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    deck = []
    for color in colors:
        for num in amount:
            cardVal = "{} {}".format(color, num)
            deck.append(cardVal)
            if num != 0:
                deck.append(cardVal)

    return deck


def shuffle(deck):
    random.shuffle(deck)
    return deck

def assign(deck):
    ai = []
    human = []
    for i in range(5):
        num = random.randint(0, len(deck))
        ai.append(deck[num - 1])
        del deck[num - 1]
    for i in range(5):
        num = random.randint(0, len(deck))
        human.append(deck[num - 1])
        del deck[num - 1]
    return deck, human, ai

def can_play(card, top_card):
    print(card.split())
    if len(card.split()) == 3:
        card_color, card_number, _ = card.split()
    else:
        card_color, card_number = card.split()
    print(len(card.split()))

    if len(top_card.split()) == 3:
        top_color, top_number, _ = top_card.split()
    else:
        top_color, top_number = top_card.split()
    
    if card_color == top_color or card_number == top_number:
        return True
    else:
        return False

def get_color(card):
    if len(card.split()) == 3:
        color, _, _ = card.split()
    else:
        color, _ = card.split
    return color    

@app.route('/', methods=['GET', 'POST'])
def index():
    global human, ai, ai_played, starting_card, current_card, turn

    if request.method == 'POST':
        if request.form.get('input_p') == None:
            print("DONE")
            player_input = request.form.get('player_input').strip().lower()
            turn = 0
            if player_input.isdigit():
                inp = int(player_input) - 1
                if inp >= 0 and inp < len(human):
                    card_to_play = human[inp]
                    extra = card_to_play
                    extra = extra.split(' ')
                    if can_play(card_to_play, current_card):
                        current_card = card_to_play
                        turn+=1
                        del human[inp]
                        print(ai)
                    
                        while turn==1:
                            for i in ai:
                                splitted = i.split(' ')
                                if (can_play(i, current_card) == True) and (splitted[1]!='Reverse') and (splitted[1]!="Draw"):
                                    del ai[ai.index(i)]
                                    ai_played.append(i)
                                    current_card = i
                                    turn-=1
                                    break
                                else:
                                    rando = random.randint(1, len(deck))
                                    ai.append(deck[rando-1])
                                    del deck[rando-1]
                    else:
                        return render_template('index.html', output="Invalid move. Try again",
                                           starting_card=starting_card, current_card=current_card,
                                           player_hand=human, ai_played_cards=ai_played)
                    return render_template('index.html', output="You played a card.",
                                           starting_card=starting_card, current_card=current_card,
                                           player_hand=human, ai_played_cards=ai_played)
        input_p = request.form.get('input_p').strip().lower()

    

        if input_p == 'play':
            if len(human) == 1:
                return render_template('index.html', output="You can't play any cards! Draw a card.",
                                    starting_card=starting_card, current_card=current_card,
                                    player_hand=human, ai_played_cards=" ".join(ai_played))

            return render_template('index.html', output="Click a card to play",
                                starting_card=starting_card, current_card=current_card,
                                player_hand=human, ai_played_cards=ai_played)


        if input_p == 'draw':
            rando = random.randint(0, len(deck))
            human.append(deck[rando])
            del deck[rando]
            return render_template('index.html', output=f"You drew a card.", starting_card=starting_card,
                                current_card=current_card, player_hand=human, ai_played_cards=ai_played)

        if input_p == 'uno':
            if len(human) == 1:
                return render_template('index.html', output="UNO!", starting_card=starting_card,
                                    current_card=current_card, player_hand=human, ai_played_cards=ai_played)
            else:
                return render_template('index.html', output="You can only declare UNO when you have one card left!",
                                    starting_card=starting_card, current_card=current_card,
                                    player_hand=human, ai_played_cards=ai_played)


        else:
            return render_template('index.html', output="Invalid move! Try again.",
                                           starting_card=starting_card, current_card=current_card,
                                           player_hand=human, ai_played_cards=ai_played)

    return render_template('index.html', output="", starting_card=starting_card, current_card=current_card,
                           player_hand=human, ai_played_cards=ai_played)

if __name__ == '__main__':
    deck = build()
    deck = shuffle(deck)
    deck, human, ai = assign(deck)
    ai_played = []  # Store AI's played cards
    starting_card = deck[random.randint(0, len(deck))]
    current_card = starting_card
    turn = 0

    app.run(debug=True)