import messages
import note_saver

def edit_note(note_id, notes):
    if note_id in notes:
        messages.edit_note_message()
        notes[note_id] = input()
        note_saver.save_note_to_file(notes)
        messages.edited_note_saved()
    else:
        messages.no_such_note_message()
    return notes