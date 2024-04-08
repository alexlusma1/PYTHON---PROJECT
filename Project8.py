import os

def create_file(filename):
    with open(filename, 'w') as file:
        text = input("Enter the text you want to write to the file:\n")
        file.write(text)

def read_file(filename):
    with open(filename, 'r') as file:
        print("File contents:")
        print(file.read())

def delete_and_start_over(filename):
    os.remove(filename)
    print(f"{filename} has been deleted and a new empty file has been created.")

def append_file(filename):
    with open(filename, 'a') as file:
        text = input("Enter the text you want to append to the file:\n")
        file.write(text)

def note_taking_program():
    filename = input("Enter a filename: ")

    if os.path.exists(filename):
        choice = input(f"'{filename}' already exists. What would you like to do?\n"
                       "A) Read the file\n"
                       "B) Delete the file and start over\n"
                       "C) Append the file\n"
                       "Enter your choice (A/B/C): ").upper()
        if choice == 'A':
            read_file(filename)
        elif choice == 'B':
            delete_and_start_over(filename)
            create_file(filename)
        elif choice == 'C':
            append_file(filename)
        else:
            print("Invalid choice. Please enter A, B, or C.")
    else:
        create_file(filename)

if __name__ == "__main__":
    note_taking_program()