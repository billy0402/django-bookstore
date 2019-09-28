# django-bookstore

## environment
- [macOS 10.14.6](https://www.apple.com/tw/macos/mojave/)
- [PyCharm 2019.2.3](https://www.jetbrains.com/pycharm/)
- [Python 3.7.4](https://www.python.org/)
- [Django 2.2.5](https://github.com/django/django)
- [Django REST framework 3.10.3](https://github.com/encode/django-rest-framework)

## ORM query
```python
# import
from books.models import Book

Book
books.models.Book
```

### INSERT ONE
```python
# INSERT INTO books_book(name, price, introduction) VALUES ('Hello', 150, 'This is a book.');
Book.objects.create(name="Hello", price=150, introduction='This is a book.')
<Book: Book object (1)>

# INSERT INTO books_book(name, price, introduction) VALUES ('Hello2', 150, 'This is a book.');
Book.objects.create(name="Hello2", price=150, introduction='This is a book.')
<Book: Book object (2)>

# INSERT INTO books_book(name, price, introduction) VALUES ('Hello3', 150, 'This is a book.');
Book.objects.create(name="Hello3", price=150, introduction='This is a book.')
<Book: Book object (3)>
```

### SELECT ALL
```python
# SELECT * FROM books_book;
Book.objects.all()
<QuerySet [<Book: Book object (1)>, <Book: Book object (2)>, <Book: Book object (3)>]>

Book.objects.all().query
<django.db.models.sql.query.Query at 0x10ed36940>

print(Book.objects.all().query)
SELECT "books_book"."id", "books_book"."name", "books_book"."price", "books_book"."introduction" FROM "books_book"
```

### SELECT ONE
```python
# SELECT * FROM books_book WHERE id=1;
Book.objects.get(pk=1)
<Book: Book object (1)>

print(Book.objects.get(pk=1))
Book object (1)

# SELECT * FROM books_book WHERE price=150;
Book.objects.filter(price=150)
<QuerySet [<Book: Book object (1)>, <Book: Book object (2)>, <Book: Book object (3)>]>

# SELECT * FROM books_book WHERE price=150 LIMIT 2;
Book.objects.filter(id__lte=2)
<QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]>

# SELECT * FROM books_book ORDER BY id;
Book.objects.order_by('id')
<QuerySet [<Book: Book object (1)>, <Book: Book object (2)>, <Book: Book object (3)>]>

# SELECT * FROM books_book ORDER BY id DESC;
Book.objects.order_by('-id')
<QuerySet [<Book: Book object (3)>, <Book: Book object (2)>, <Book: Book object (1)>]>

# SELECT * FROM books_book ORDER BY RAND();
Book.objects.order_by('?')
<QuerySet [<Book: Book object (3)>, <Book: Book object (1)>, <Book: Book object (2)>]>
```

### UPDATE ONE
```python
# SELECT * FROM books_book WHERE id=1;
Book.objects.get(pk=1)

# SELECT id FROM books_book WHERE id=1;
book.id
1

# UPDATE books_book SET price=300 WHERE id=1;
book.price = 300

book.save()
```

### UPDATE MANY
```python
# INSERT INTO books_book(name, price, introduction) VALUES ('Hello2', 150, 'This is a book.');
Book.objects.create(name="Hello2", price=150, introduction='This is a book.')
<Book: Book object (4)>

# INSERT INTO books_book(name, price, introduction) VALUES ('Hello4', 200, 'This is a book.');
Book.objects.create(name="Hello4", price=200, introduction='This is a book.')
<Book: Book object (5)>

# INSERT INTO books_book(name, price, introduction) VALUES ('Hello5', 100, 'This is a book.');
Book.objects.create(name="Hello5", price=100, introduction='This is a book.')
<Book: Book object (6)>

# INSERT INTO books_book(name, price, introduction) VALUES ('Hello6', 500, 'This is a book.');
Book.objects.create(name="Hello6", price=500, introduction='This is a book.')
<Book: Book object (7)>

# INSERT INTO books_book(name, price, introduction) VALUES ('Hello7', 250, 'This is a book.');
Book.objects.create(name="Hello7", price=250, introduction='This is a book.')
<Book: Book object (8)>

# SELECT * FROM books_book WHERE price=200;
Book.objects.filter(price=200)
<QuerySet [<Book: Book object (5)>]>

# SELECT * FROM books_book WHERE price>=200;
Book.objects.filter(price__gte=200)
<QuerySet [<Book: Book object (1)>, <Book: Book object (5)>, <Book: Book object (7)>, <Book: Book object (8)>]>

# UPDATE books_book SET name='World' WHERE price>=200;
Book.objects.filter(price__gte=200).update(name='World')
4
```

### DELETE ONE
```python
# SELECT * FROM books_book WHERE id=2;
book = Book.objects.get(pk=2)

# SELECT id FROM books_book WHERE id=2;
book.id
2

# DELETE FROM books_book WHERE id=2;
book.delete()
(1, {'books.Book': 1})
```