import os
import csv
import json
from random import shuffle, choice
from flask import *

app = Flask(__name__)

def get_books(n=10):
    possible_files = os.listdir('book_data')
    r = csv.reader(open('book_data/'+choice(possible_files)))
    books = [row for row in r]
    shuffle(books)
    return books[0:n]

@app.route('/')
def hello():
    initial_books = get_books(10)
    book_zero = initial_books.pop()
    return render_template('br.html', book_zero=book_zero, initial_books=initial_books)

@app.route('/v1/get_books', methods=['GET'])
def api_get_books():
    n = int(request.args.get('n', 10)) # get n items, or 10 by default
    books = get_books(n)
    return json.dumps(books)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True # DEBUG
    app.run(host='0.0.0.0', port=port)
