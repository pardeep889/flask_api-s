from flask import Flask, request, jsonify

app = Flask(__name__)

bookList = [
    {
        "id": 0,
        "author": "Pardeep",
        "language": "English",
        "title": "Book 1"
    },
     {
        "id": 1,
        "author": "Pardeep 1",
        "language": "Hindi",
        "title": "Book 2"
    }
     
]

@app.route('/')
def live():
    return "App is Live"

@app.route('/books', methods=['GET', 'POST'])
def get_books():
    if request.method == 'GET':
        if len(bookList) > 0:
            return jsonify(bookList)
        else:
            return "No Books Found"
    if(request.method == "POST"):
        data = request.get_json()
        bookList.append(data)
        return jsonify(bookList), 201

@app.route('/book/<int:id>', methods= ['GET', 'PUT', 'DELETE'])
def single_book(id):
    if(request.method == 'GET'):
        bookFound = []
        for book in bookList:
            if(book['id']) == id:
                bookFound.append(book)
            pass
        if(len(bookFound) > 0 ):
            return jsonify(bookFound)
        else:
            return "No book found!"
    if(request.method == "PUT"):
        data = request.get_json()
        id = data['id']
        for book in bookList:
            if(book['id'] == id):
                updatedBook = data
                return jsonify(updatedBook)
    if(request.method == "DELETE"):
        for book in bookList:
            if(book['id'] == id):
                bookList.pop(book['id'])
                return jsonify(bookList)
            pass
app.run(debug=True)