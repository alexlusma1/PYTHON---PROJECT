Create a note-taking program. When a user starts it up, it should prompt them for a filename.

If they enter a file name that doesn't exist, it should prompt them to enter the text they want to write to the file. After they enter the text, it should save the file and exit.

If they enter a file name that already exists, it should ask the user if they want:

A) Read the file

B) Delete the file and start over

C) Append the file

If the user wants to read the file it should simply show the contents of the file on the screen. If the user wants to start over then the file should be deleted and another empty one made in its place. If a user elects to append the file, then they should be able to enter more text, and that text should be added to the existing text in the file. 





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
