from note_app import NotesApp

def main():
    app = NotesApp()
    while True:
        print("\n--- Note App ---")
        print("1. Add a note")
        print("2. View all notes")
        print("3. Delete a note")
        print("4. Exit")

        choice = input("Pick an option 1-4: ").strip()

        if choice == "1":
            title = input("Enter a title for your note:")
            content = input("Enter note content:")
            app.add_note(title, content)

        elif choice == "2":
            app.view_notes()

        elif choice == "3":
            title = input("Enter a title to delete note: ")
            if app.delete_note(title):
                print("Your note has been deleted")
            else:
                print("This note does not exist")
                
                
        
        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice try again")

if __name__ == "__main__":
    main()