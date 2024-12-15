import todo
import os

def test_create_todo():
    todo.todos = []
    todo.create_todo(todo.todos,
                     title="Make some stuff",
                     description="Stuff needs to be programmed",
                     level="Important")
    
    assert len(todo.todos) == 1, "Todo was not created!"
    assert todo.todos[0]['title'] =="Make some stuff"
    assert (todo.todos[0]['description'] ==
            "Stuff needs to be programmed")
    assert (todo.todos[0]['level']) == "Important"

    print("ok - create_todo")

def test_get_function():
    assert todo.get_function('new') == todo.create_todo
    print("ok - get_function")

def test_get_fields():
    assert (todo.get_fields('new') ==
            ['title', 'description', 'level'])
    print("ok - test_get_fields")   

def test_run_command():
    result = todo.run_command(
        'test',
        {'abcd':'efgh', 'ijkl':'mnop'}
    )
    expected = """Command 'test' returned:
abcd: efgh
ijkl: mnop"""
    assert result == expected, \
                result + " != " + expected
    print ("ok - run_command")

def test_show_todos():
    todo.todos = [
        { 'title' : 'test todo',
          'description' : 'This is a test',
          'level' : 'IMPORTANT'
        }
    ]
    result = todo.show_todos(todo.todos)
    lines = result.split("\n")

    first_line = lines[0]
    assert "Item" in first_line
    assert "Title" in first_line
    assert "Description" in first_line
    assert "Level" in first_line
    second_line = lines[1]
    assert "1" in second_line
    assert "test todo" in second_line
    assert "This is a test" in second_line
    assert "IMPORTANT" in second_line

    print ("ok - show_todos")

def test_todo_sort_order():
    todo.todos = [
        { 'title' : 'test unimportant todo',
            'description' : 'An unimportant test',
            'level' : 'Unimportant'
        },
        { 'title' : 'test medium todo',
            'description' : 'A test',
            'level' : 'Medium'
        },
        { 'title' : 'test important todo',
            'description' : 'An important test',
            'level' : 'Important'
        },
    ]
    result = todo.show_todos(todo.todos)
    lines = result.split("\n")
    assert "IMPORTANT" in lines[1]
    assert "Medium," in lines[2]
    assert "Unimportant" in lines[3]

    print("OK - todo sort order")

def test_todo_wrap_long_lines():
    todo.todos = [
        { 'title' : 'test important todo',
         'description' : ('This is an important '
                          'test. We\'d really like '
                          'this line to wrap '
                          'several times, to '
                          'imitate what might '
                          'happen in a real '
                          'program.'),
                          'level' : 'IMPORTANT'
                          },
    ]
    result = todo.show_todos(todo.todos)
    lines = result.split("\n")

    assert "test important" in lines[1]
    assert "This is an important" in lines[1]

    assert "todo" in lines[2]
    assert "test. We'd really like" in lines[2]

    assert "this line to wrap" in lines[3]
    assert "several times, to" in lines[4]
    assert "imitate what might" in lines[5]
    assert "happen in a real" in lines[6]
    assert "program." in lines[7]

    print("ok - todo wrap long lines")

def test_save_todo_list():
            todos_original = [
                 { 'title' : 'test todo',
                  'description' : 'This is a test',
                  'level' : 'IMPORTANT'
                  }
            ]
            todo.todos = todos_original
            assert "todos.pickle" in os.listdir('.')

            todo.save_todo_list()
            assert "todos.pickle" in os.listdir('.')

            todo.load_todo_list()
            assert todo.todos == todos_original
            os.unlink("todos.pickle")
            print("ok - save todo list")

test_get_function()
test_create_todo()
test_run_command()
test_get_fields()
test_show_todos()
test_todo_wrap_long_lines()
test_save_todo_list()