import pytest 
from lib.task_tracker import TaskTracker

'''
initially there are no tasks
'''
def test_no_tasks_initially():
    tracker = TaskTracker()
    assert tracker.list_incomplete() == []

'''
when we add a task
it is reflected in the list of tasks
'''
def test_task_is_added():
    tracker = TaskTracker()
    tracker.add("walk dog")
    assert tracker.list_incomplete() == ["walk dog"]

'''
when we add multiple tasks
They are all reflected in the list of tasks
'''
def test_add_multiple_tasks():
    tracker = TaskTracker()
    tracker.add("walk dog")
    tracker.add("feed cat")
    tracker.add("wash laundry")
    assert tracker.list_incomplete() == [
        "walk dog", "feed cat", "wash laundry"]

'''
when we add multiple tasks & mark 1 completed
it is removed from the list of tasks
'''
def test_marks_tasks_complete():
    tracker = TaskTracker()
    tracker.add("walk dog")
    tracker.add("feed cat")
    tracker.add("wash laundry")
    tracker.mark_complete(1)
    assert tracker.list_incomplete() == ["walk dog", "wash laundry"]

'''
raises an error if 
try to mark non-existent task as completed (too low)
'''
def test_mark_complete_task_too_low():
    tracker = TaskTracker()
    tracker.add("walk dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(-1)
    assert str(err.value) == "no such task exists"
    assert tracker.list_incomplete() == ["walk dog"]

'''
raises an error if 
try to mark non-existent task as completed (too high)
'''
def test_mark_complete_task_too_high():
    tracker = TaskTracker()
    tracker.add("walk dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(1)
    assert str(err.value) == "no such task exists"
    assert tracker.list_incomplete() == ["walk dog"]