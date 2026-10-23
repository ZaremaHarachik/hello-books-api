
from flask import Blueprint, abort, make_response, request, Response
from flask_sqlalchemy import query
from app.models.book import Book
from ..db import db


# Blueprint for book routes
books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

# helper function to validate book id and return the book object or abort with 404 if not found
def validate_book(book_id):
    try:
        book_id = int(book_id)
    except ValueError:
        abort(404)

    book = db.session.get(Book, book_id)

    if book is None:
        abort(404)

    return book

def create_book_object(title, description):
    return Book(title=title, description=description)

# Create book route
@books_bp.post("")
def create_book():
    request_body = request.get_json()
    title = request_body["title"]
    description = request_body["description"]

    new_book = create_book_object(title, description)
    db.session.add(new_book)
    db.session.commit()

    response = {
        "id": new_book.id,
        "title": new_book.title,
        "description": new_book.description,
    }
    return response, 201


# Get all books route
@books_bp.get("")
def get_all_books():
    query = db.select(Book)

    title_param = request.args.get("title")

    if title_param:
        query = query.where(
            Book.title.ilike(f"%{title_param}%"))

    description_param = request.args.get("description")

    if description_param:
        query = query.where(
            Book.description.ilike(f"%{description_param}%")
        )

    query = query.order_by(Book.id)
    books = db.session.scalars(query).all()

    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description,
        })

    return books_response, 200    
    


# Get one book route
@books_bp.get("/<book_id>")
def get_one_book(book_id):
    book = validate_book(book_id)

    return {
        "id": book.id,
        "title": book.title,
        "description": book.description
    }, 200


# Update book route
@books_bp.delete("/<book_id>")
def delete_book(book_id):
    book = validate_book(book_id)
    db.session.delete(book)
    db.session.commit()

    return Response(status=204, mimetype="application/json")




