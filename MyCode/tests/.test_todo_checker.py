import pytest
from lib.todo_checker import *

# def test_todo_checker1():  # does it work at all?
#     assert todo_checker1('hello') == 'hello'

# def test_todo_checker2():  # check if it returns True
#     assert todo_checker2('hello') == True

def test_todo_checker1():  # check if it returns False
    assert todo_checker(' hello') == False

def test_todo_checker2():  # check if it returns True
    assert todo_checker('#TODO hello') == True

def test_todo_checker3():  # check if it returns True
    with pytest.raises(Exception) as e:
        todo_checker("")
    error_message = str(e.value)
    assert error_message == 'ERROR - no text entered'
    