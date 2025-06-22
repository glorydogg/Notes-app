from note import Note  # assuming your Note class is in note.py

class NotesApp:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        new_note = Note(title, content)
        self.notes.append(new_note)

    def delete_note(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                return True
        return False
    
    def view_notes(self):
        if not self.notes:
            print("No notes yet!")
            return
        for i, note in enumerate(self.notes, start=1):
            print(f"\nNote {i}: \n{note}")
