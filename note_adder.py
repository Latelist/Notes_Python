import note_saver
import messages
from datetime import datetime

def add_note(notes):
    current_datetime = datetime.now()
    note_id = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    messages.add_note_message()
    note = input()
    id = str(note_id)
    notes[id] = note
    note_saver.save_note_to_file(notes)
    print("Заметка добавлена!")