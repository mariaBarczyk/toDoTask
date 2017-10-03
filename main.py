from todo import Todo
from todo_item import TodoItem
from user import User

'''
user1 = User('Ala', 'admin')
user2 = User('Kotek', 'miaumiau123')

print(user1.user_name)
print(user2.user_name)

print(user1.password)
print(user2.password)

print(user1.display_info_about_user())
print(user2.display_info_about_user())

print(user1)  # jak damy print wtedy szuka __str__ w całej klasie i jak znajdzie to printuje
print(user2)
'''


def main():
    # 1
    usename_input = input('Podaj nazwę użytkownika: ')
    password_input = input('Podaj hasło użtkownika: ')
    user = User(usename_input, password_input)

    # 2
    tasks = Todo()  # tworzymy obiekt z klasy todo

    # 3
    tasks.assign_user_to_todo(user)
    print(tasks.assigned_user)

    # 5
    first_note = TodoItem('zrobić zakupy')
    second_note = TodoItem('ogarnąć się')
    third_note = TodoItem('nauczyć się programować')
    # 4
    tasks.add_note(first_note)
    tasks.add_note(second_note)
    tasks.add_note(third_note)

    tasks.display_notes  # przed zmianą wyświetlamy
    tasks.notes[0].toggle_done()  # zmieniamy na 'Done'
    tasks.display_notes()  # po zmianie wyśiwetlamy


if __name__ == '__main__':
    main()

'''
## What the application should do?
1. App can create new user with name and password from terminal input
2. App creates new todo object
3. App assignes new user to todo object.
4. User can use todo object (add, delete and display notes)
5. User can add new note using TodoItem class
6. TodoItem class should has magic function (__str__) to display value of parameter
'''
