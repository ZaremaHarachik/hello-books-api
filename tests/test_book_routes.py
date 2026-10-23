from app.routes.book_routes import create_book_object


def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_create_book_object():
    # Arrange
    title = "My Book"
    description = "A story"

    # Act
    book = create_book_object(title, description)

    # Assert
    assert book.title == title
    assert book.description == description


def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }


def test_create_one_book(client):
    # Act
    response = client.post("/books", json={
        "title": "New Book",
        "description": "The Best!"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "title": "New Book",
        "description": "The Best!"
    }


def test_get_one_book_not_found(client):
    response = client.get("/books/1")

    assert response.status_code == 404


def test_get_all_books_with_saved_books(client, two_saved_books):
    response = client.get("/books")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "title": "Ocean Book",
            "description": "watr 4evr"
        },
        {
            "id": 2,
            "title": "Mountain Book",
            "description": "i luv 2 climb rocks"
        }
    ]    