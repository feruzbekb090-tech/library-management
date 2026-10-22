def get_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdecimal():
            return int(value)
        print("Xato: iltimos, butun son kiriting.")


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("Xato: bu maydon bo'sh bo'lmasligi kerak.")


def get_optional_text(prompt):
    value = input(prompt).strip()
    if value == "":
        return None
    return value


def get_optional_int(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            return None
        if value.isdecimal():
            return int(value)
        print("Xato: iltimos, butun son kiriting yoki bo'sh qoldiring.")


def find_book_by_id(books, book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None


def format_book(book):
    if book["available"]:
        status = "Mavjud"
    else:
        status = "Berilgan"
    return f"ID: {book['id']} | {book['title']} | {book['author']} | {book['year']} | {status}"


def print_books(books, empty_message="Kitoblar topilmadi."):
    if len(books) == 0:
        print(empty_message)
        return
    print("-" * 60)
    for book in books:
        print(format_book(book))
    print("-" * 60)
