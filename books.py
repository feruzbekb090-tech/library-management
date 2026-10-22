"""Kitoblar bilan ishlovchi asosiy amallar (qo'shish, tahrirlash, o'chirish, qidirish, berish, qaytarish)."""

from database import books, generate_book_id
from utils import (
    get_int,
    get_non_empty,
    get_optional_text,
    get_optional_int,
    find_book_by_id,
    format_book,
    print_books,
)


def show_all_books():
    print("\n--- Barcha kitoblar ---")
    print_books(books, "Kutubxonada hozircha kitoblar yo'q.")


def add_book():
    print("\n--- Kitob qo'shish ---")
    title = get_non_empty("Kitob nomi: ")
    author = get_non_empty("Muallif: ")
    year = get_int("Nashr yili: ")

    book = {
        "id": generate_book_id(),
        "title": title,
        "author": author,
        "year": year,
        "available": True,
    }
    books.append(book)
    print(f"Kitob qo'shildi (ID: {book['id']}).")


def edit_book():
    print("\n--- Kitobni tahrirlash ---")
    book_id = get_int("Kitob ID: ")
    book = find_book_by_id(books, book_id)
    if book is None:
        print("Xato: bunday ID li kitob topilmadi.")
        return

    print("Hozirgi ma'lumot:")
    print(format_book(book))
    print("(Eski qiymatni saqlash uchun bo'sh qoldiring)")

    new_title = get_optional_text(f"Yangi nom [{book['title']}]: ")
    new_author = get_optional_text(f"Yangi muallif [{book['author']}]: ")
    new_year = get_optional_int(f"Yangi yil [{book['year']}]: ")

    if new_title is not None:
        book["title"] = new_title
    if new_author is not None:
        book["author"] = new_author
    if new_year is not None:
        book["year"] = new_year
    print("Ma'lumotlar yangilandi.")


def delete_book():
    print("\n--- Kitobni o'chirish ---")
    book_id = get_int("Kitob ID: ")
    book = find_book_by_id(books, book_id)
    if book is None:
        print("Xato: bunday ID li kitob topilmadi.")
        return
    if not book["available"]:
        print("Xato: kitob hozir foydalanuvchida, uni o'chirib bo'lmaydi.")
        return
    books.remove(book)
    print(f"'{book['title']}' o'chirildi.")


def search_books():
    print("\n--- Kitob qidirish ---")
    query = get_non_empty("Nom yoki muallif: ").lower()
    results = [
        book
        for book in books
        if query in book["title"].lower() or query in book["author"].lower()
    ]
    print_books(results, "Hech narsa topilmadi.")


def borrow_book():
    print("\n--- Kitob berish ---")
    book_id = get_int("Kitob ID: ")
    book = find_book_by_id(books, book_id)
    if book is None:
        print("Xato: bunday ID li kitob topilmadi.")
    elif not book["available"]:
        print("Bu kitob allaqachon berilgan.")
    else:
        book["available"] = False
        print(f"'{book['title']}' foydalanuvchiga berildi.")


def return_book():
    print("\n--- Kitobni qaytarish ---")
    book_id = get_int("Kitob ID: ")
    book = find_book_by_id(books, book_id)
    if book is None:
        print("Xato: bunday ID li kitob topilmadi.")
    elif book["available"]:
        print("Bu kitob allaqachon kutubxonada mavjud.")
    else:
        book["available"] = True
        print(f"'{book['title']}' qaytarildi.")


def show_available_books():
    print("\n--- Mavjud kitoblar ---")
    available = [book for book in books if book["available"]]
    print_books(available, "Mavjud kitoblar yo'q.")


def show_borrowed_books():
    print("\n--- Berilgan kitoblar ---")
    borrowed = [book for book in books if not book["available"]]
    print_books(borrowed, "Berilgan kitoblar yo'q.")
