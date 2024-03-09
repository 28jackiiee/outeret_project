from flask import Flask, render_template, request
import random
import time
app = Flask(__name__)

def get_random_direction():
    directions = ['Left', 'Right', 'Up', 'Down']
    return random.choice(directions)




    
@app.route('/', methods=['GET', 'POST'])
def index():
    global turn, ai_wins, wins
    if request.method == 'POST':
        aichoice = get_random_direction()
        data = request.form
        choice = data['direction']
        if turn == 0:
            while turn ==0:
                if choice == aichoice:
                    ai_wins += 1
                    return render_template('index.html',turn2="The AI guessed your move", decision = aichoice)
                if ai_wins>=2:
                    return render_template('index.html', win_decision="YOU LOSE TO A FREAKING BOT, ASSHOLE!")
                if choice != aichoice:
                    turn +=1
                    return render_template('index.html', turn1="It is now your turn", decision = aichoice)
                
            time.sleep(3)
        if turn ==1:
            while turn ==1:
                if choice == aichoice:
                    wins += 1
                    return render_template('index.html', turn2="You have guessed the AIs move", decision = aichoice)
                if wins >=2:
                    return render_template('index.html', win_decision="YOU WON, HUMAN!")
                if choice!= aichoice:
                    turn = 0
                    return render_template('index.html', turn1="It is now the AIs move", decision = aichoice) 
                
                    
                        
                


        
        
        
    return render_template('index.html', who_turn=0)

if __name__ == '__main__':
    turn = 0
    ai_wins = 0
    wins = 0
    app.run(debug=True)
