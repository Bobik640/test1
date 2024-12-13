class Book:
    def __init__(self, title, author, year, book_id):
        self.title = title
        self.author = author
        self.year = year
        self.book_id = book_id
        self.status = "доступна"  # Статус книги (доступна или выдана)

    def display_info(self):
        print(f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, ID: {self.book_id}, Статус: {self.status}")

    def change_status(self):
        if self.status == "доступна":
            self.status = "выдана"
        else:
            self.status = "доступна"


class User:
    def __init__(self, username, user_id):
        self.username = username
        self.user_id = user_id
        self.borrowed_books = []  # Список выданных книг

    def add_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)


class Library:
    def __init__(self):
        self.books = []  # Список книг
        self.users = []  # Список пользователей

    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        self.users.append(user)

    def issue_book(self, user_id, book_id):
        user = self.get_user(user_id)
        book = self.get_book(book_id)

        if book is None:
            print("Книга не найдена.")
            return

        if book.status == "выдана":
            print("Книга уже выдана.")
            return

        book.change_status()
        user.add_book(book)
        print(f"Книга '{book.title}' выдана пользователю '{user.username}'.")

    def return_book(self, user_id, book_id):
        user = self.get_user(user_id)
        book = self.get_book(book_id)

        if book is None:
            print("Книга не найдена.")
            return

        if book not in user.borrowed_books:
            print("Эта книга не была выдана пользователю.")
            return

        book.change_status()
        user.return_book(book)
        print(f"Книга '{book.title}' возвращена пользователем '{user.username}'.")

    def get_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def get_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None


def main():
    library = Library()

    while True:
        print("1. Добавить книгу")
        print("2. Зарегистрировать пользователя")
        print("3. Выдать книгу")
        print("4. Вернуть книгу")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            book_id = input("Введите ID книги: ")
            book = Book(title, author, year, book_id)
            library.add_book(book)
            print("Книга добавлена в библиотеку.")

        elif choice == '2':
            username = input("Введите имя пользователя: ")
            user_id = input("Введите ID пользователя: ")
            user = User(username, user_id)
            library.register_user(user)
            print("Пользователь зарегистрирован.")

        elif choice == '3':
            user_id = input("Введите ID пользователя: ")
            book_id = input("Введите ID книги: ")
            library.issue_book(user_id, book_id)

        elif choice == '4':
            user_id = input("Введите ID пользователя: ")
            book_id = input("Введите ID книги: ")
            library.return_book(user_id, book_id)

        elif choice == '5':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
