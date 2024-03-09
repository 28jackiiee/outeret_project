import random
from flask import Flask, render_template, request

app = Flask(__name__)


emoji_database = [
    {"name": "smile", "emoji": "😊", "clue": "Happy face"},
    {"name": "heart", "emoji": "🧡", "clue": "Symbol of love"},
    {"name": "cat", "emoji": "🐱", "clue": "Meow!"},
    {"name": "screaming", "emoji": "😱", "clue": "Scary"},
    {"name": "salute", "emoji": "🫡", "clue": "Salute"},
    {"name": "skull", "emoji": "💀", "clue": "Dead"},
    {"name": "poop", "emoji": "💩", "clue": "Poop"},
    {"name": "nerd", "emoji": "🤓", "clue": "Ermmm"},
    {"name": "shush", "emoji": "🤫", "clue": "Quiet"},
]

def get_random_emoji():
    return random.choice(emoji_database)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_guess = request.form['user_guess']
        correct_emoji = request.form['correct_emoji']
        if user_guess.lower() == correct_emoji.lower():
            result = "Congratulations! That's the correct emoji!"
            emoji = get_random_emoji()
        else:
            result = "Oops! Try again. That's not the correct emoji."
            emoji = {
                "emoji": request.form['current_emoji'],
                "clue": request.form['current_clue'],
                "name": correct_emoji
            }
    else:
        result = None
        emoji = get_random_emoji()

    return render_template('index.html', current_emoji=emoji['emoji'], current_clue=emoji['clue'], result=result, correct_emoji=emoji['name'])

if __name__ == '__main__':
    app.run(debug=True)