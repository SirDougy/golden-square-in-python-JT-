class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 1
        for char in self.text:
            if not char.isalpha():
                continue
            # counter[char] = counter.get(char, 1) + 1
            counter[char] = counter.get(char, 0) + 1 # AMENDED
            # By using 0 as the default value, we ensure that the first occurrence of a 
            # character is counted correctly as 1, and subsequent occurrences are incremented by 1.
            # using 1 will add the default value to the count instead
            if counter[char] > most_common_count:
                most_common = char
                # most_common_count += counter[char]
                most_common_count = counter[char] # AMENDED
                # the most_common_count variable is updated with the current count of 
                # counter[char], instead of adding it
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]
# un-corrected output: [3, "D"]
