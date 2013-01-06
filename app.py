import os
import csv
import json
from random import shuffle
from flask import *

app = Flask(__name__)

@app.route('/')
def hello():
    url_for('static', filename='css/bootstrap.css')
    return render_template('br.html')

@app.route('/v1/get_books', methods=['GET'])
def get_books():
    n = int(request.args.get('n', 10)) # get n items, or 10 by default

    r = csv.reader(open('reduced_books.csv'))
    books = [row for row in r]
    shuffle(books)
    return json.dumps(books[0:n])

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True # DEBUG
    app.run(host='0.0.0.0', port=port)
