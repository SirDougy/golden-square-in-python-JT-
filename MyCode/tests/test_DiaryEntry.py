import pytest 

from lib.DiaryEntry import DiaryEntry

"""
Given a title and contents
#format returns a formatted entry, eg:
"My Title : These are the contents" 
"""
def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.format()
    assert result == "My Title: Some contents"


'''
given title & contents
#count_words returns total number of words
'''
def test_count_words():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.count_words()
    assert result == 4


'''
given empty title
raises an error
'''
def test_error_if_empty():
    with pytest.raises(Exception) as err:
        DiaryEntry('', 'content')
    assert str(err.value) == 'ERROR: no title/contents entered'

'''
given empty contents
raises an error
'''
def test_error_if_empty_contents():
    with pytest.raises(Exception) as err:
        DiaryEntry('title', '')
    assert str(err.value) == 'ERROR: no title/contents entered'


'''
given wpm of 2 and text of 2 words
#reading_time returns 1 minute
'''
def test_reading_time_2wpm_2words():
    diary_entry = DiaryEntry('Title', 'one two')
    result = diary_entry.reading_time(2)
    assert result == 1

'''
given wpm of 2 and text of 4 words
#reading_time returns 2 minute
'''
def test_reading_time_2wpm_4words():
    diary_entry = DiaryEntry('Title', 'one two three four')
    result = diary_entry.reading_time(2)
    assert result == 2

'''
given wpm of 2 and text of 3 words
#reading_time returns 2 minute
'''
def test_reading_time_2wpm_3words():
    diary_entry = DiaryEntry('Title', 'one two three')
    result = diary_entry.reading_time(2)
    assert result == 2

'''
given wpm of 0
#reading_time raises an error
'''
def test_reading_time_0wpm():
    diary_entry = DiaryEntry('Title', 'one two three')
    with pytest.raises(Exception) as err:
        diary_entry.reading_time(0)
    assert str(err.value) ==  'ZERO is invalid wpm'

'''
given content of 6 words, wpm of 2 and time of 1 minute
#reading_chunk returns the first two words
'''
def test_reading_chunk_2wpm_and_1min():
    diary_entry = DiaryEntry('Title', 'one two three four five six')
    result = diary_entry.reading_chunk(2, 1)
    assert result == 'one two'

'''
given content of 6 words, wpm of 2 and time of 2 minute
#reading_chunk returns the first four words
'''
def test_reading_chunk_2wpm_and_2min():
    diary_entry = DiaryEntry('Title', 'one two three four five six')
    result = diary_entry.reading_chunk(2, 2)
    assert result == 'one two three four'

'''
given content of 6 words, wpm of 2 and time of 1 minute
first call #reading_chunk returns 'one two'
second call #reading_chunk returns 'three four'
'''
def test_2_calls_reading_chunk_2wpm_and_1min():
    diary_entry = DiaryEntry('Title', 'one two three four five six')
    assert diary_entry.reading_chunk(2, 1) == 'one two'
    assert diary_entry.reading_chunk(2, 1) == 'three four'

'''
given content of 6 words, wpm of 2 and time of 1 minute
first call #reading_chunk returns 'one two'
second call #reading_chunk returns 'three four'
third call #reading_chunk returns 'five six'
'''
def test_3_calls_reading_chunk_2wpm_and_1min():
    diary_entry = DiaryEntry('Title', 'one two three four five six')
    assert diary_entry.reading_chunk(2, 1) == 'one two'
    assert diary_entry.reading_chunk(2, 1) == 'three four'
    assert diary_entry.reading_chunk(2, 1) == 'five six'

'''
given content of 6 words
if #reading_chunk is called repeatedly
last chuck is remaining words in contents, even if less than user can read
next chunk loops back to start of text
'''
def test_reading_chunk_wraps_on_multiple_calls():
    diary_entry = DiaryEntry('Title', 'one two three four five six')
    assert diary_entry.reading_chunk(2, 2) == 'one two three four'
    assert diary_entry.reading_chunk(2, 2) == 'five six'
    assert diary_entry.reading_chunk(2, 2) == 'one two three four'

'''
given content of 6 words
if #reading_chunk is called repeatedly with an exact ending
last chuck is remaining words in contents
next chunk loops back to start of text
'''
def test_reading_chunk_wraps_on_multiple_calls_with_exact_ending():
    diary_entry = DiaryEntry('Title', 'one two three four five six')
    assert diary_entry.reading_chunk(2, 2) == 'one two three four'
    assert diary_entry.reading_chunk(2, 1) == 'five six'
    assert diary_entry.reading_chunk(2, 2) == 'one two three four'
