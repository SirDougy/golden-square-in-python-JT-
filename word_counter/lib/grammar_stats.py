class GrammarStats:
    def __init__(self):
        self.num_checked = 0
        self.num_passed = 0
    def check(self, text):
        self.num_checked += 1
        if text[-1] == ('.' or '!' or '?') and (text[0].isupper()):
            self.num_passed += 1
            return True
        else:
            return False
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
    def percentage_good(self):
        if self.num_checked == 0:
            return self.num_passed == 0
        percent_pass = int((self.num_passed / self.num_checked) * 100)
        return percent_pass
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%

