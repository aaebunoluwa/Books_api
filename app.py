from flask import Flask, request, jsonify

app = Flask(__name__)

books = [{'id': 1,
        'name': 'Tales by moonlight',
        'author': 'Lanre Akinkunmi'},
        {'id': 2,
        'name': 'Percy Jackson',
        'author': 'Bolanle Sadiku'},
        {'id': 3,
        'name': 'The wives revolt',
        'author': 'Chioma Akpotha'}]

@app.route('/books', methods = ['GET', 'POST'])
def get_books():
    if request.method == 'GET':
        return jsonify(books)
    elif request.method == 'POST':
        new_book = request.get_json()
        books.append(new_book)
        return jsonify(books)
@app.route('/books/<int:book_id>')   
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
        
@app.route('/get_book')   
def get_a_book():
    book_id = request.args.get('book_id')
    print(book_id)
    for book in books:
        if book['id'] == int(book_id):
            return jsonify(book)

if __name__ == '__main__':
    app.run(debug = True)

