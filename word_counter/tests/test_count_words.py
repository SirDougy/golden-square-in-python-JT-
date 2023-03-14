from lib.count_words import *


# def test_count_words1(): # basic test
#     assert count_words1('one two three four five') == 'one two three four five'


# def test_count_words2(): # added .split() to return text as a list
#     assert count_words2('one two three four five') == ['one', 'two', 'three', 'four', 'five']


# def test_count_words3(): # added .len() to count words in list
#     assert count_words3('one two three four five') == 5

##  code was tested & written in 3 stages, final version of test is below



def test_count_words(): # final version of code
    assert count_words('one two three four five') == 5  