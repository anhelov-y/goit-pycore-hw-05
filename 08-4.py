
# Пустий словник для зберігання
contacts = {}


# декоратор для обробки
def input_error(func):
    # внутрішня функція для обгортки 
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        # обробка помилок
        except KeyError:
            return "Enter user name"

        except ValueError:
            return "Give me name and phone please"

        except IndexError:
            return "Not enough data"

        except Exception:
            return "Something went wrong :("

    return inner


# Додати контакт
@input_error
def add_contact(args, contacts_book):
    name, phone = args
    contacts_book[name] = phone
    return "Contact added."


# Зміна контакту
@input_error
def change_contact(args, contacts_book):
    name, phone = args
    # Видаємо помилку, якщо імені немає 
    if name not in contacts_book:
        raise KeyError
    contacts_book[name] = phone
    return "Contact updated."


# Вивести телефон за іменем
@input_error
def show_phone(args, contacts_book):
    name = args[0]
    if name not in contacts_book:
        raise KeyError
    return f"{name}: {contacts_book[name]}"


# Вивести всі контакти 
@input_error
def show_all(contacts_book):
    # На випадок пустого словнику
    if not contacts_book:
        return "No contacts yet."
    result = ""
    # Перебір варінтів та додавання в строку 
    for name, phone in contacts_book.items():
        result += f"{name}: {phone}\n"
    return result


def main():

    print("Simple contact bot. Type 'help' for commands.")

    while True:
        # Отримання команди від користувача
        command = input("Enter a command: ").strip()

        # Вихід з програми
        if command == "exit" or command == "close":
            print("Good bye!")
            break

        # команда add
        elif command.startswith("add"):
            parts = command.split()
            result = add_contact(parts[1:], contacts)
            print(result)

        # команда change
        elif command.startswith("change"):
            parts = command.split()
            result = change_contact(parts[1:], contacts)
            print(result)

        # команда phone
        elif command.startswith("phone"):
            parts = command.split()
            result = show_phone(parts[1:], contacts)
            print(result)

        #Вивести всі контакти 
        elif command == "all":
            print(show_all(contacts))

        # команда help
        elif command == "help":
            print("Commands:")
            print("add name phone")
            print("change name phone")
            print("phone name")
            print("all")
            print("exit / close")

        # На випадок невідомої команди
        else:
            print("Unknown command.")


# Точка входу
if __name__ == "__main__":
    main()