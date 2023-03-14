# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

> As a user
> So that I can manage my time
> I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def estimate_reading_time(text)
    # Parameters: 
    #     text: a string of text
    # Returns:
    #     a float to represent the reading time

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

"""
Given text of 200 words
returns reading time of 1.0
"""
estimate_reading_time('...200...') 
# => 1.0

"""
Given text of 400 words
returns reading time of 2.0
"""
estimate_reading_time('...400...') 
# => 2.0

"""
Given text of 300 words
returns reading time of 1.5
"""
estimate_reading_time('...300...') 
# => 1.5

"""
Given text of 400 words
returns reading time of 2.0
"""
estimate_reading_time('...400...') 
# => 2.0

"""
Given empty string
raises an error
"""
estimate_reading_time('') 
# Raises error: 'ERROR  - no text entered'

200 word SAMPLE TEXT:

one two three four five six seven eight nine ten
one two three four five six seven eight nine ten
one two three four five six seven eight nine ten
one two three four five six seven eight nine ten
one two three four five six seven eight nine ten
one two three four five six seven eight nine ten
one two three four five six seven eight nine ten
one two three four five six seven eight nine ten
one two three four five six seven eight nine ten
one two three four five six seven eight nine ten
ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN
ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN
ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN
ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN
ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN
ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN
ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN
ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN
ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN
ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!





<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
