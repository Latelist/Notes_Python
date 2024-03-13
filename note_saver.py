

def save_note_to_file(notes):
    with open ("notes.txt", "w") as file:
        for key, value in notes.items():
            file.write(key + "\n" + value + "\n\n")