# library-management

# Library Management System

Terminal (buyruq oynasi) orqali ishlaydigan kutubxona boshqaruv dasturi. Dastur yordamida kitoblarni qo'shish, ko'rish, tahrirlash, o'chirish, qidirish hamda kitoblarni foydalanuvchiga berish va qaytarib olish mumkin.

## Dastur nimalarni qila oladi

- Barcha kitoblar ro'yxatini ko'rsatadi
- Yangi kitob qo'shadi (ID avtomatik beriladi)
- Kitob ma'lumotlarini (nom, muallif, yil) tahrirlaydi
- Kitobni o'chiradi (foydalanuvchida turgan kitobni o'chirib bo'lmaydi)
- Kitobni nom yoki muallif bo'yicha qidiradi (katta-kichik harf farq qilmaydi)
- Kitobni foydalanuvchiga beradi va qaytarib oladi
- Faqat mavjud yoki faqat berilgan kitoblarni alohida ko'rsatadi

## Talablar

- Python 3.8 yoki undan yangi versiya
- Qo'shimcha kutubxona o'rnatish shart emas

Python o'rnatilganini tekshirish uchun terminalda yozing:

    python --version

## Ishga tushirish

1.  Terminalni oching va loyiha papkasiga o'ting:

        cd library_management

2.  Dasturni ishga tushiring:

        python main.py

3.  Menyudan kerakli raqamni kiriting va Enter bosing. Dasturdan chiqish uchun `0` ni kiriting.

## Papkalar tuzilmasi

    library_management/
    ├── main.py        menyu va dastur oqimi
    ├── books.py       kitoblar bilan ishlash (asosiy amallar)
    ├── utils.py       yordamchi funksiyalar
    ├── database.py    ma'lumotlar saqlanadigan joy
    └── README.md      shu yo'riqnoma

## Modullar va funksiyalar

### main.py - dastur boshqaruvi

Menyuni ko'rsatadi, foydalanuvchi tanlovini oladi va mos funksiyani chaqiradi. Menyu `0` tanlanmaguncha takrorlanadi.

| Funksiya     | Vazifasi                                                    |
| ------------ | ----------------------------------------------------------- |
| `print_menu` | Menyuni ekranga chiqaradi                                   |
| `main`       | Asosiy sikl: tanlovni oladi, mos funksiyani ishga tushiradi |

### books.py - kitoblar bilan ishlash

Har bir menyu punkti uchun alohida funksiya bor.

| Funksiya               | Vazifasi                                      |
| ---------------------- | --------------------------------------------- |
| `show_all_books`       | Barcha kitoblarni ko'rsatadi                  |
| `add_book`             | Yangi kitob qo'shadi                          |
| `edit_book`            | Kitob nomi, muallifi yoki yilini o'zgartiradi |
| `delete_book`          | Kitobni o'chiradi                             |
| `search_books`         | Kitobni qidiradi                              |
| `borrow_book`          | Kitobni foydalanuvchiga beradi                |
| `return_book`          | Berilgan kitobni qaytarib oladi               |
| `show_available_books` | Faqat kutubxonadagi kitoblarni ko'rsatadi     |
| `show_borrowed_books`  | Faqat berilgan kitoblarni ko'rsatadi          |

### utils.py - yordamchi funksiyalar

Bir xil tekshiruv kodi bir necha joyda takrorlanmasligi uchun shu yerga yig'ilgan.

| Funksiya            | Vazifasi                                               |
| ------------------- | ------------------------------------------------------ |
| `get_int`           | Butun son kiritilguncha so'raydi                       |
| `get_non_empty`     | Bo'sh bo'lmagan matn kiritilguncha so'raydi            |
| `get_optional_text` | Matn so'raydi, bo'sh qoldirilsa `None` qaytaradi       |
| `get_optional_int`  | Son so'raydi, bo'sh qoldirilsa `None` qaytaradi        |
| `find_book_by_id`   | ID bo'yicha kitobni topadi, topilmasa `None` qaytaradi |
| `format_book`       | Bitta kitobni bitta satr qilib tayyorlaydi             |
| `print_books`       | Kitoblar ro'yxatini ekranga chiqaradi                  |

### database.py - ma'lumotlar

| Nom                | Vazifasi                                          |
| ------------------ | ------------------------------------------------- |
| `books`            | Kitoblar ro'yxati (boshida 3 ta namuna kitob bor) |
| `counters`         | Keyingi ID raqamini saqlaydi (`next_book_id`)     |
| `generate_book_id` | Yangi takrorlanmas ID beradi                      |

## Kitob qanday saqlanadi

Har bir kitob lug'at (`dict`) ko'rinishida saqlanadi:

    {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2008,
        "available": True
    }

| Maydon      | Ma'nosi                                                      |
| ----------- | ------------------------------------------------------------ |
| `id`        | Kitobning takrorlanmas raqami                                |
| `title`     | Kitob nomi                                                   |
| `author`    | Muallif                                                      |
| `year`      | Nashr yili                                                   |
| `available` | `True` - kutubxonada bor, `False` - foydalanuvchiga berilgan |

## Menyu

    ===== LIBRARY MANAGEMENT =====
    1. Barcha kitoblarni ko'rish
    2. Kitob qo'shish
    3. Kitob ma'lumotlarini tahrirlash
    4. Kitobni o'chirish
    5. Kitob qidirish
    6. Kitobni foydalanuvchiga berish
    7. Kitobni qaytarish
    8. Mavjud kitoblarni ko'rish
    9. Berilgan kitoblarni ko'rish
    0. Chiqish

## Dastur qanday ishlaydi

1. `main.py` menyuni chiqaradi va raqam so'raydi.
2. Raqam `ACTIONS` lug'atidan qidiriladi va mos funksiya `books.py` dan chaqiriladi.
3. `books.py` dagi funksiya kerak bo'lganda `utils.py` dan yordamchi funksiyalarni, `database.py` dan kitoblar ro'yxatini oladi.
4. Amal tugagach, menyu yana ko'rsatiladi.

## Noto'g'ri kiritilgan ma'lumotlar

Dastur quyidagi holatlarda to'xtab qolmaydi, tushunarli xabar chiqaradi:

- Menyuda noto'g'ri raqam yoki matn kiritilsa
- ID o'rniga matn kiritilsa
- Mavjud bo'lmagan ID kiritilsa
- Nom yoki muallif bo'sh qoldirilsa
- Yil butun son bo'lmasa
- Berilgan kitobni yana berishga urinilsa
- Kutubxonadagi kitobni qaytarishga urinilsa
- Foydalanuvchida turgan kitobni o'chirishga urinilsa
- Kitoblar ro'yxati bo'sh bo'lsa

## Cheklovlar

- Ma'lumotlar faqat xotirada saqlanadi, dastur yopilganda yo'qoladi va keyingi ishga tushganda yana 3 ta namuna kitob bilan boshlanadi.
- `class`, tashqi kutubxona va ma'lumotlar bazasi ishlatilmagan.
