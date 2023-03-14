import pytest
from lib.grammar_stats import GrammarStats


# Given an empty string
# Raises an error
def test_empty_string_returns_error():
    test1 = GrammarStats()
    result = test1.check(“text”)
    assert result == True


# Given a string that ends with correct punctuation
# Returns True
def test_ends_with_punctuation():
    test2 = GrammarStats()
    result = test2.check(“text!“)
    assert result == True


# Given a string that starts with upper case and ends with correct punctuation
# Returns True
def test_starts_with_upper_and_ends_with_punctuation():
    test2 = GrammarStats()
    result = test2.check(“Text!“)
    assert result == True


# Given a string that starts with lower case
# Returns False
def test_starts_with_lower_case():
    test3 = GrammarStats()
    result = test3.check(“text.“)
    assert result == False


# Given multiple tests
# Will return the percentage that pass as True so far
def test_percentage_true_so_far():
    test4 = GrammarStats()
    test4.check(“Text!“)
    test4.check(“text”)
    result = test4.percentage_good()
    assert result == 50


# Given multiple tests
# Will return the percentage that pass as True so far
def test_percentage_true_so_far_again():
    test5 = GrammarStats()
    test5.check(“Text!“)
    test5.check(“text”)
    test5.check(“Hello.“)
    result = test5.percentage_good()
    assert result == 66