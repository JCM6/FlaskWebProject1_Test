from flask import Flask, jsonify, request, Response
import htmlRepository as html
import booksRepository as b
import json
from settings import *

books = b.books

def validBookObj(bookObj):
    if ("name" in bookObj and "price" in bookObj and "isbn" in bookObj):
        return True
    else:
        return False
        
@app.route('/')
def navToBooks():
    return '<a href=\"/books\">Go to Books</a>n<div>somethingfin</div>'

#GET
@app.route('/bookPreview', methods=['GET'])
def bookPreview():
    return html.loadTestFile()

#GET
@app.route('/books', methods=['GET'])
def hello():
    return jsonify({'books':books})

#POST
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

def validPutRequestData(requestData):
    if("name" in requestData and 'price' in requestData):
        return True
    else:
        return False

#PUT
@app.route('/books/<int:isbn>', methods=['PUT'])
def replaceBook(isbn):
    requestData = request.get_json()
    #Validate Book Object

    if(not validPutRequestData(requestData)):
        invalidBookObjectErrorMsg = {
            "error":"Valid book object must be passed in this request",
            "helpString":"Data passed should be similar to this: {'name':'bookname', 'price':1.00 }"
        }
        response = Response(json.dumps(invalidBookObjectErrorMsg), status=400, mimetype='application/json')
        return response

    newBook = {
        'name': requestData['name'],
        'price': requestData['price'],
        'isbn': isbn
    }
    i = 0
    for book in books:
        currentIsbn = book['isbn']
        if currentIsbn == isbn:
            books[i] = newBook
            i+=1

    response = Response('', status=204)
    return response

#PATCH
@app.route('/books/<int:isbn>', methods=['PATCH'])
def updateBook(isbn):
    requestData = request.get_json()
    updatedBook = {}
    if ("name" in requestData):
        updatedBook["name"] = requestData["name"]
    if ("price" in requestData):
        updatedBook["price"] = requestData["price"]
    
    for book in books:
        if book['isbn'] == isbn:
            book.update(updatedBook)
    
    response = Response("", status=204)
    response.headers['Location'] = "/books/" + str(isbn)
    return response


#DELETE
@app.route('/books/<int:isbn>', methods=["DELETE"])
def delete_book(isbn):
    i = 0
    searchSuccess = False
    for book in books:
        if book['isbn']==isbn:
            books.pop(i)
            response = Response("", status=204)
            searchSuccess = True
        if searchSuccess == False:    
            invalidBookObjectErrorMsg = {
                "error": "Book with the ISBN Number:" + str(isbn) + ' was not found. Unable to delete a resource that does not exist.'
            }
            response = Response(json.dumps(invalidBookObjectErrorMsg), status=404, mimetype='application/json')
        i+=1
    return response

app.run(port=5000)