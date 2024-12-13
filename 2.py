class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_student_id(self, student_id):
        self.student_id = student_id

    def get_student_id(self):
        return self.student_id

    def display_info(self):
        return f'{self.name}, {self.age} лет, ID: {self.student_id}'


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Студент добавлен.")

    def remove_student(self, student_id):
        for student in self.students:
            if student.get_student_id() == student_id:
                self.students.remove(student)
                print("Студент удалён.")
                return
        print("Студент не найден.")

    def find_student(self, student_id):
        for student in self.students:
            if student.get_student_id() == student_id:
                return student.display_info()
        return "Студент не найден."

    def display_all_students(self):
        if not self.students:
            print("Список студентов пуст.")
        else:
            print("Список студентов:")
            for idx, student in enumerate(self.students, 1):
                print(f"{idx}. {student.display_info()}")


def main():
    manager = StudentManager()
    
    while True:
        command = input("Введите команду (добавить, удалить, найти, показать, выход): ").strip().lower()

        if command == "добавить":
            name = input("Введите имя студента: ")
            age = input("Введите возраст студента: ")
            student_id = input("Введите номер студенческого билета: ")
            student = Student(name, age, student_id)
            manager.add_student(student)

        elif command == "удалить":
            student_id = input("Введите номер студенческого билета для удаления: ")
            manager.remove_student(student_id)

        elif command == "найти":
            student_id = input("Введите номер студенческого билета для поиска: ")
            result = manager.find_student(student_id)
            print(result)

        elif command == "показать":
            manager.display_all_students()

        elif command == "выход":
            print("Выход из программы.")
            break

        else:
            print("Неверная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()
