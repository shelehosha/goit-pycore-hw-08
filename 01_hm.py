import pickle

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, contact_info):
        self.contacts[name] = contact_info

    def get_contact(self, name):
        return self.contacts.get(name, "Контакт не знайдено")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

def save_data(book, filename="addressbook.pkl"):
    """Функція для збереження даних адресної книги у файл"""
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    """Функція для завантаження даних з файлу"""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        # Повертаємо нову адресну книгу, якщо файл не знайдено
        return AddressBook()

def main():
    # Відновлюємо дані з файлу або створюємо нову AddressBook
    book = load_data()

    # Основний цикл програми
    while True:
        command = input("Введіть команду (add, get, delete, exit): ").strip().lower()
        
        if command == "add":
            name = input("Введіть ім'я: ")
            contact_info = input("Введіть контактну інформацію: ")
            book.add_contact(name, contact_info)
            print(f"Контакт {name} додано.")
        
        elif command == "get":
            name = input("Введіть ім'я: ")
            print(f"Контактна інформація: {book.get_contact(name)}")
        
        elif command == "delete":
            name = input("Введіть ім'я: ")
            book.delete_contact(name)
            print(f"Контакт {name} видалено.")
        
        elif command == "exit":
            # Зберігаємо дані у файл перед виходом
            save_data(book)
            print("Дані збережено. Вихід з програми.")
            break
        
        else:
            print("Невідома команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()