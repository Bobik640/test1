class Book:
    def __init__(self, title, author, year, book_id):
        self.title = title
        self.author = author
        self.year = year
        self.book_id = book_id
        self.is_available = True

    def display_info(self):
        status = 'доступна' if self.is_available else 'выдана'
        print(f"ID: {self.book_id}, Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {status}")

    def change_status(self, new_status):
        self.is_available = new_status


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.issued_books = []

    def issue_book(self, book):
        if book.is_available:
            self.issued_books.append(book)
            book.change_status(False)
            print(f"Книга '{book.title}' выдана пользователю {self.name}.")
        else:
            print(f"Книга '{book.title}' уже выдана другому пользователю.")

    def return_book(self, book):
        if book in self.issued_books:
            self.issued_books.remove(book)
            book.change_status(True)
            print(f"Книга '{book.title}' возвращена в библиотеку.")
        else:
            print(f"У пользователя {self.name} нет книги '{book.title}'.")


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в библиотеку.")

    def register_user(self, user):
        self.users.append(user)
        print(f"Пользователь {user.name} зарегистрирован в библиотеке.")

    def issue_book_to_user(self, book_id, user_id):
        book = self.find_book(book_id)
        user = self.find_user(user_id)
        if book and user:
            user.issue_book(book)

    def return_book_from_user(self, book_id, user_id):
        book = self.find_book(book_id)
        user = self.find_user(user_id)
        if book and user:
            user.return_book(book)

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        print(f"Книга с ID {book_id} не найдена.")
        return None

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        print(f"Пользователь с ID {user_id} не найден.")
        return None

    def display_books(self):
        print("\nСписок книг в библиотеке:")
        for book in self.books:
            book.display_info()

    def display_users(self):
        print("\nСписок пользователей библиотеки:")
        for user in self.users:
            print(f"ID: {user.user_id}, Имя: {user.name}, Количество книг на руках: {len(user.issued_books)}")


def main():
    library = Library()

    while True:
        print("\n1. Добавить книгу")
        print("2. Зарегистрировать пользователя")
        print("3. Выдать книгу пользователю")
        print("4. Вернуть книгу")
        print("5. Показать все книги")
        print("6. Показать всех пользователей")
        print("7. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            book_id = input("Введите ID книги: ")
            book = Book(title, author, year, book_id)
            library.add_book(book)

        elif choice == '2':
            name = input("Введите имя пользователя: ")
            user_id = input("Введите ID пользователя: ")
            user = User(name, user_id)
            library.register_user(user)

        elif choice == '3':
            user_id = input("Введите ID пользователя: ")
            book_id = input("Введите ID книги: ")
            library.issue_book_to_user(book_id, user_id)

        elif choice == '4':
            user_id = input("Введите ID пользователя: ")
            book_id = input("Введите ID книги: ")
            library.return_book_from_user(book_id, user_id)

        elif choice == '5':
            library.display_books()

        elif choice == '6':
            library.display_users()

        elif choice == '7':
            print("Завершение работы.")
            break

        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
