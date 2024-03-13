import note_adder
import note_reader
import messages
import note_printer
import note_editor
import note_deleter


def work_cycle(state):
    notes = note_reader.read_notes()
    print(notes)
    messages.start_message()
    while state:
        messages.choose_mode_message()
        mode = input()
        match mode:
            case "1":
                notes_id = note_adder.add_note(notes)
            case "2":
                lines = note_reader.read_notes()
                note_printer.print_notes(lines)
            case "3":
                lines = note_reader.read_notes()
                note_printer.print_notes(lines)
                messages.choose_note_to_edit_message()
                note_id = input()
                notes = note_editor.edit_note(note_id, notes)
            case "4":
                lines = note_reader.read_notes()
                note_printer.print_notes(lines)
                messages.choose_note_to_delete_message()
                note_id = input()
                notes = note_deleter.delete_note(notes, note_id)
            case "5":
                state = False
                messages.goodbye_message()
            case _:
                messages.no_such_command_message()
        if state == True:
            messages.will_continue_message()
            line = input()
            match line:
                case "Y":
                    continue
                case "N":
                    state = False
                    messages.goodbye_message()
                case _:
                    messages.didnt_understand()

        