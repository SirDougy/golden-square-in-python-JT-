# {{PROBLEM}} Function Design Recipe

.

## 1. Describe the Problem

> As a user  
> So that I can keep track of my tasks  
> I want to check if a text includes the string `#TODO`.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def todo_checker(text)
    # Parameters: 
    #     text: a string of text
    # Returns:
    #     TRUE if string contains #TODO 

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```
Given text including '#TODO'
returns True
```
todo_checker('#TODO wash dishes')
# => True


```
Given text not including '#TODO'
returns False
```
todo_checker('wash dishes')
# => False

```
Given no text
raises an error
```
todo_checker('')
# => 'ERROR - no text entered'

```
_Encode each example as a test. You can add to the above list as you go._
```

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
