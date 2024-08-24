from flask import *
import py.utilities as ut

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def hello():
    card1 = render_template('modules/card_tc.html', title='Welcome', content='Hello World') # Reads the content of the card from the card_tc.html file, populates the template with title and content as specified.
    card2 = render_template('modules/card_tc.html', title='This is card 2', content='Hello World')
    return render_template('frames/index.html', tab_title = "Demo-Hello World", big_title = "Hello World", card1=card1, card2=card2)

@app.route('/multicard/<int:n>')
def multicard(n):
    cards = []
    for i in range(n):
        cards.append(render_template('modules/card_tc.html', title=f'This is card {i}', content='Hello World'))
        #The code above renders the card_tc.html template n times, each time with a different title. 
        #Then, it adds it to the list cards. In multicard.html, we use a for-loop to display all the cards in the list.
    return render_template('frames/multicard.html', tab_title = "Demo-Multicards",big_title = "Array of elements", cards=cards)

@app.route('/button')
def button():
    return render_template('pages/button_example.html')


@app.route('/sum/<int:a>/<int:b>')
def sum(a, b):
    return f'The sum of {a} and {b} is {ut.sum(a, b)}'


if __name__ == '__main__':
    app.run()