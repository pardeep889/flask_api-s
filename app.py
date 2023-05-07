from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)

# database configrations
def db_connections():
    conn = None
    try:
        conn = sqlite3.connect('books.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

@app.route('/')
def live():
    return "App is Live"

@app.route('/books', methods=['GET', 'POST'])
def get_books():
    conn = db_connections()
    if request.method == 'GET':
        query = "SELECT * FROM book"
        cursor = conn.execute(query)
        allBooks = cursor.fetchall()
        return jsonify(allBooks), 200
    if(request.method == "POST"):
        data = request.get_json()
        query = """ INSERT INTO book (author, language, title) VALUES(?,?,?)"""
        cursor = conn.execute(query, (data['author'], data['language'], data['title']))
        conn.commit()
        return f"Book with ID: {cursor.lastrowid} is created successfully"
        

@app.route('/book/<int:id>', methods= ['GET', 'PUT', 'DELETE'])
def single_book(id):
    conn = db_connections()
    if(request.method == 'GET'):
        query = "SELECT * FROM book WHERE id=?"
        cursor = conn.execute(query, (id,))
        book = cursor.fetchall()
        if(len(book) > 0):
            return book
        else:
            return "Sorry no book associated with given Id"
        
    if(request.method == "PUT"):
        data = request.get_json()
        query = "UPDATE book SET title=?, author=?, language=? WHERE id=?"
        conn.execute(query, (data['title'], data['author'], data['language'],id))
        conn.commit()
        return jsonify(data), 201
        
    if(request.method == "DELETE"):
        query = "DELETE FROM book WHERE id=?"
        conn.execute(query, (id,))
        conn.commit()
        return f"Book with id: {id} has been deleted successfully"
        
app.run(debug=True)