from lib.vowel_remover import *

def test_simple_dud():
    remover = VowelRemoverDud("ab")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "b"

def test_long_sentence_with_punctuation_dud():
    remover = VowelRemoverDud("We will remove the vowels from this sentence.")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "W wll rmv th vwls frm ths sntnc."

# def test_remove_every_vowel_at_once_dud():
#     remover = VowelRemoverDud("aeiou")
#     result_no_vowels = remover.remove_vowels()
#     assert result_no_vowels == ""

def test_remove_every_vowel_at_once_dud_forced():
    remover = VowelRemoverDud("aeiou")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "eo"
    # FORCED - test fails when using expected output (SEE ABOVE)
    # code does not account for consecutive vowels

# def test_remove_consecutive_vowels_dud():
#     remover = VowelRemoverDud("Our Glorious Leader Pol Pot is in the pool")
#     result_no_vowels = remover.remove_vowels()
#     assert result_no_vowels == "r Glrs Ldr Pl Pt s n th pl"

def test_remove_consecutive_vowels_dud_forced(): 
    remover = VowelRemoverDud("Our Glorious Leader Pol Pot is in the pool")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "ur Glros Ladr Pl Pt s n th pol"
    # FORCED - test fails when using expected output (SEE ABOVE)
    # code does not account for consecutive vowels

##########################################################################################    

def test_simple():
    remover = VowelRemover("ab")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "b"

def test_long_sentence_with_punctuation():
    remover = VowelRemover("We will remove the vowels from this sentence.")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "W wll rmv th vwls frm ths sntnc."

def test_remove_every_vowel_at_once():
    remover = VowelRemover("aeiou")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == ""

def test_remove_consecutive_vowels():
    remover = VowelRemover("Our Glorious Leader Pol Pot is in the pool")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "r Glrs Ldr Pl Pt s n th pl"