def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'No user with this name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'

    return wrapper

@input_error
def hello_command():
    return "How can I help you?"

@input_error
def add_command(contact_dict, *args):
    name, phone = args
    contact_dict[name.lower()] = phone
    return f"Contact {name.capitalize()} added with phone {phone}."

@input_error
def change_command(contact_dict, *args):
    name, new_phone = args
    if name in contact_dict.keys():
        contact_dict[name.lower()] = new_phone
        return f"Phone number for contact {name.capitalize()} changed to {new_phone}."
    else:
        return f"There is no contact {name} your list."

@input_error
def phone_command(contact_dict, *args):
    name = args[0]
    return f"Phone number for contact {name.capitalize()} is {contact_dict[name.lower()]}."

@input_error
def show_all_command(contact_dict):
    if not contact_dict:
        return "No contacts available."
    else:
        result = "\n".join([f"{name.capitalize()}: {phone}" for name, phone in contact_dict.items()])
        return result

def main():
    contact_dict = {}
    while True:
        command = input("Enter a command: ").lower()

        if command in ["good bye", "close", "exit"]:
            print("Good bye.")
            break
        elif command == "hello":
            print(hello_command())
        elif command.startswith("add"):
            print(add_command(contact_dict, *command.split()[1:]))
        elif command.startswith("change"):
            print(change_command(contact_dict, *command.split()[1:]))
        elif command.startswith("phone"):
            print(phone_command(contact_dict, *command.split()[1:]))
        elif command == "show all":
            print(show_all_command(contact_dict))
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()