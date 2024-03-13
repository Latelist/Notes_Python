def start_message():
    print("Добро пожаловать в приложение «Заметки».")
    
def choose_mode_message():
    print("Выберите, что хотите сделать: \n" + 
          "1 — записать заметку\n" + 
          "2 — прочитать заметки\n" + 
          "3 — отредактировать заметку\n" +
          "4 — удалить заметку\n" +
          "5 — завершить работу")
    
def goodbye_message():
    print("Спасибо за работу. До свидания.")

def add_note_message():
    print("Введите заметку:")

def will_continue_message():
    print("Продолжить? Y/N")

def choose_note_to_edit_message():
    print("Введите идентификатор заметки, которую хотите отредактировать. Идентификатор — это дата и время создания. Скопируйте нужный и вставьте.")

def edit_note_message():
    print("Введите отредактированную заметку.")

def edited_note_saved():
    print("Заметка отредактирована!")

def choose_note_to_delete_message():
    print("Введите идентификатор заметки, которую хотите удалить. Идентификатор — это дата и время создания. Скопируйте нужный и вставьте.")

def note_deleted_message():
    print("Заметка удалена!")

def no_such_note_message():
    print("Заметки с таким идентификатором нет.")

def no_such_command_message():
    print("Я не знаю такой команды.")

def notes_is_empty_message():
    print("Заметки пусты.")

def didnt_understand():
    print("Я не знаю такой команды, но все равно продолжу.")