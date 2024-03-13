from flask import Flask, render_template, request
from spell_bee_solver import generate_words, find_perfect_pangram

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    word_list = None
    perfect_pangrams = None

    if request.method == 'POST':
        user_input = request.form['user_input'].lower()

        if len(user_input) == 7 and user_input.isalpha():
            word_list = generate_words(user_input)
            perfect_pangrams = find_perfect_pangram(user_input)

    return render_template('index.html', word_list=word_list, perfect_pangrams=perfect_pangrams)

if __name__ == '__main__':
    app.run(debug=True)
