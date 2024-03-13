import note_saver
import messages

def delete_note(notes, note_id):
    if note_id in notes: 
        del notes[note_id]
        note_saver.save_note_to_file(notes)
        messages.note_deleted_message()
    else:
        messages.no_such_note_message()
    return notes
    