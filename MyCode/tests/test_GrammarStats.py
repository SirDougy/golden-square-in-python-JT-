import pytest
from lib.grammar_stats import GrammarStats


def test_non_empty_string_returns_correct_result():
    test1 = GrammarStats()
    result = test1.check("Text.")
    assert result == True


def test_ends_with_punctuation():
    test2 = GrammarStats()
    result = test2.check('Text.')
    assert result == True


def test_starts_with_lower_case():
    test3 = GrammarStats()
    result = test3.check('text.')
    assert result == False


def test_percentage_good_with_no_checked_texts():
    test4 = GrammarStats()
    result = test4.percentage_good()
    assert result == 0


def test_percentage_good_with_all_passed_texts():
    test5 = GrammarStats()
    test5.check('Text.')
    test5.check('Hello!')
    result = test5.percentage_good()
    assert result == 100


def test_percentage_good_with_some_passed_texts():
    test6 = GrammarStats()
    test6.check('Text.')
    test6.check('text.')
    test6.check('Hello!')
    result = test6.percentage_good()
    assert result == 66


def test_check_with_invalid_input():
    test7 = GrammarStats()
    result = test7.check('')
    assert result == False

def test_check_with_no_punctuation():
    test8 = GrammarStats()
    result = test8.check('Text')
    assert result == False


def test_check_with_all_upper_case():
    test9 = GrammarStats()
    result = test9.check('TEXT!')
    assert result == True


def test_check_with_multiple_sentences():
    test10 = GrammarStats()
    result = test10.check('Hello! This is a test.')
    assert result == True
