import messages

def read_notes():
    with open ("notes.txt", "r") as file:
        lines = file.readlines()
        notes = {}
        if len(lines) > 2:
            for i in range(len(lines)):
                if lines[i] == "\n":
                    notes[lines[i-2].replace("\n", "")] = lines[i-1].replace("\n", "")
        else:
            messages.notes_is_empty_message()
        return notes