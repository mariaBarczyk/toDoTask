# TODO List in OOP Way

## Description
In this exercise, you should write a simple application for short notes management.

## Structure
Each class should be stored in separated module, main module stores all logic regarding application (within main() function's body)

Create following classes:
- Todo
- TodoItem
- User

### TodoItem

Contains attributes about TODO item:
- name
- state
Constructor should has 1 parameters - name is assign from parameter. State has default value: "No done"

This class should contain following methods:
- toggle_done() - set state 'Done' value

### Todo

Contains attributes about TODO item:
- notes - list of notes (default value: empty list)
- assigned_user - initially set to None, stores user object for validation
Constructor without extra parameters

This class should contain and following methods:
- assign_user_to_todo(user) - assign user to notes. 'user' parameter is object of User class
- add_note(new_note) - add new note to list ('new_note' is object of TodoItem class)
- remove_note(id_note) - remove note from list by id
- display_notes() - list all notes with their state (done/undone) -> use magic method (__str__) from Todo class, to display information about notes

### User

Contains attributes about user:
- name
- password


## What the application should do?
1. App can create new user with name and password from terminal input
2. App creates new todo object
3. App assignes new user to todo object.
4. User can use todo object (add, delete and display notes)
5. User can add new note using TodoItem class
6. TodoItem class should has magic function (__str__) to display value of parameter


