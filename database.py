"""Ma'lumotlarni saqlash: boshlang'ich kitoblar ro'yxati va ID hisoblagich.

Ma'lumotlar faqat xotirada saqlanadi, dastur yopilganda yo'qoladi.
"""

books = [
    {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2008,
        "available": True,
    },
    {
        "id": 2,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "year": 1999,
        "available": True,
    },
    {
        "id": 3,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "year": 2015,
        "available": False,
    },
]

# Keyingi beriladigan ID. Lug'at ichida saqlaymiz, shunda boshqa fayldan ham o'zgartirish mumkin.
counters = {"next_book_id": 4}


def generate_book_id():
    """Yangi takrorlanmas ID qaytaradi va hisoblagichni bittaga oshiradi."""
    new_id = counters["next_book_id"]
    counters["next_book_id"] += 1
    return new_id
