
## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class TaskTracker():

    def add(self, task):
        # Parameters:
        #   task: string representing a task
        pass

    def list_incomplete(self):
        # Returns:
        #   a list of completed tasks
        pass

    def mark_complete(self, index):
        # Parameters:
        #   index: an integer representing the task to complete
        # side-effect:
        #   removes the task at index from the list of tasks
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

'''
initially there are no tasks
'''
tracker = TaskTracker()
tracker.list_incomplete() # +> []

'''
when we add a task
it is reflected in the list of tasks
'''
tracker = TaskTracker()
tracker.add("walk dog")
tracker.list_incomplete()
    # => ["walk dog"]

'''
when we add multiple tasks
They are all reflected in the list of tasks
'''
tracker = TaskTracker()
tracker.add("walk dog")
tracker.add("feed cat")
tracker.add("wash laundry")
tracker.list_incomplete()
    # => ["walk dog", "feed cat", "wash laundry"]

'''
when we add multiple tasks & mark 1 completed
it is removed from the list of tasks
'''
tracker = TaskTracker()
tracker.add("walk dog")
tracker.add("feed cat")
tracker.add("wash laundry")
tracker.mark_complete(1)
tracker.list_incomplete()
    # => ["walk dog", "wash laundry"]

'''
raises an error if 
try to mark non-existent task as completed (too low)
'''
tracker = TaskTracker()
tracker.add("walk dog")
tracker.mark_complete(-1) # raises error "no such task exists"
tracker.list_incomplete()    # => ["walk dog"]

'''
raises an error if 
try to mark non-existent task as completed (too high)
'''
tracker = TaskTracker()
tracker.add("walk dog")
tracker_mark_complete(2) # raises error "no such task exists"
tracker.list_incomplete()    # => ["walk dog"]


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

