class Todo():
    notes = []
    assigned_user = None

    def assign_user_to_todo(self, user):  # assign user to notes. 'user' parameter is object of User class
        self.assigned_user = user

    def add_note(self, new_note):
        self.notes.append(new_note)  # add new note to list ('new_note' is object of TodoItem class)

    def remove_note(self, id_note):
        self.notes.pop(id_note)  # remove note from list by id

    def display_notes(self):
        '''list all notes with their state (done/undone) -> 
        use magic method (__str__) from Todo class, to display 
        information about notes'''

        for task in self.notes:    # printujemy task w TodoItem i on idzie do TodoItem i szuka tam metody __str__
            print(task)  # <-- ten zapis wywoła nam __str__ z TodoItem