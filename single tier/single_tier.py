import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("notes.db")
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL
    )
''')
conn.commit()

# Function to add a note
def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    print("\n✅ Note added successfully!\n")

# Function to view all notes
def view_notes():
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    
    if not notes:
        print("\n📭 No notes found!\n")
        return
    
    print("\n📋 Your Notes:\n")
    for note in notes:
        print(f"[{note[0]}] 📌 {note[1]}\n   {note[2]}\n")

# Function to delete a note
def delete_note():
    view_notes()
    note_id = input("Enter the Note ID to delete: ")
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    print("\n🗑️ Note deleted successfully!\n")

# Function to display menu
def menu():
    while True:
        print("\n=== 📝 Personal Note-Taking App ===")
        print("1️⃣ Add a Note")
        print("2️⃣ View Notes")
        print("3️⃣ Delete a Note")
        print("4️⃣ Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("\n👋 Exiting... Have a great day!\n")
            conn.close()
            break
        else:
            print("\n❌ Invalid choice. Please enter a valid option.\n")

# Run the menu
menu()
