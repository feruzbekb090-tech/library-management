"""Library Management System - dastur kirish nuqtasi (menyu va dastur oqimi)."""

import books

MENU = {
    "1": "Barcha kitoblarni ko'rish",
    "2": "Kitob qo'shish",
    "3": "Kitob ma'lumotlarini tahrirlash",
    "4": "Kitobni o'chirish",
    "5": "Kitob qidirish",
    "6": "Kitobni foydalanuvchiga berish",
    "7": "Kitobni qaytarish",
    "8": "Mavjud kitoblarni ko'rish",
    "9": "Berilgan kitoblarni ko'rish",
    "0": "Chiqish",
}

ACTIONS = {
    "1": books.show_all_books,
    "2": books.add_book,
    "3": books.edit_book,
    "4": books.delete_book,
    "5": books.search_books,
    "6": books.borrow_book,
    "7": books.return_book,
    "8": books.show_available_books,
    "9": books.show_borrowed_books,
}


def print_menu():
    print("\n===== LIBRARY MANAGEMENT =====")
    for key, title in MENU.items():
        print(f"{key}. {title}")


def main():
    while True:
        print_menu()
        choice = input("Tanlang: ").strip()

        if choice == "0":
            print("Dastur yakunlandi. Xayr!")
            break

        action = ACTIONS.get(choice)
        if action is None:
            print("Xato: 0 dan 9 gacha bo'lgan raqamni kiriting.")
        else:
            action()


main()
