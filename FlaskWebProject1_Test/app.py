from flask import Flask, jsonify, request, Response
import htmlRepository
import booksRepository as b
import json

app = Flask(__name__)

__name__ == "__main__"

books = b.books


def validBookObj(bookObj):
    if ("name" in bookObj and "price" in bookObj and "isbn" in bookObj):
        return True
    else:
        return False




@app.route('/')
def navToBooks():
    return '<a href=\"/books\">Go to Books</a>'

@app.route('/bookPreview')
def bookPreview():
    return htmlRepository.loadTestFile()

@app.route('/books')
def hello():
    return jsonify({'books':books})

@app.route('/books', methods=['POST'])
def addBook():
    requestData = request.get_json()
    if (validBookObj(requestData)):
        newBook = {
            "name": requestData['name'],
            "price": requestData['price'],
            "isbn": requestData['isbn']
        }
        books.insert(0, newBook)
        response = Response("",201, mimetype='application/json')
        response.headers['Location'] = "/books/" + str(newBook['isbn'])
        return response
    else:
        invalidBookObjectErrorMsg = {
            "error":"Invalid book object was passed in the request.",
            "helpString":"Data passed to this endpoint needs to be formatted similar to this object {'name':'BooklyBook - The Sequeling','price':15.33,'isbn':88845334411}"
        }
        response = Response(json.dumps(invalidBookObjectErrorMsg, indent=4), status=400, mimetype='application/json')
        return response
    return 

#GET
@app.route('/books/<int:isbn>')
def getbookByISBN(isbn):
    return_value = {}
    for book in books:
        if book["isbn"] == isbn:
            return_value = {
                'name': book["name"],
                'price': book["price"]
            }
    return jsonify(return_value)

#PUT
@app.route('books/<int:isbn>')
def replaceBook(isbn):
    return jsonify(request.get_json())

app.run(port=5000)