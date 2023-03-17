class VowelRemoverDud:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
            i += 1
        return self.text

# this does not account for consecutive vowels in the string   
# When the method encounters a vowel in the text, it removes that vowel from the string 
# by slicing the string and re-assigning it to the original text variable. 
#
# However, it only removes the current vowel and moves to the next character, 
# not considering if the next character is also a vowel.

class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
            else:
                i += 1
        return self.text
    
# In the updated implementation, the else block is executed when the character at the 
# current index is not a vowel. In this block, [i] is incremented by 1, 
# so the loop moves on to the next character regardless of whether it is a vowel or not. 
# 
# This means that if two or more vowels are consecutive in the input string, 
# the loop will continue removing vowels until a consonant is encountered, 
# since [i] is incremented only when the current character is not a vowel.
