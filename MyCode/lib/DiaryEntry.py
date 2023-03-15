import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == '' or contents == '':
            raise Exception('ERROR: no title/contents entered')
        self._title = title
        self._contents = contents
        self._read_so_far = 0


    def format(self):
        return f"{self._title}: {self._contents}"


    def count_words(self):
        words = self.format().split(' ')
        return len(words)


    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception('ZERO is invalid wpm')
        contents_word_count = len(self._contents.split())
        return math.ceil(contents_word_count / wpm)
    
        
    def reading_chunk(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        words = self._contents.split()
        if self._read_so_far >= len(words):
            self._read_so_far = 0
        chunk_start = self._read_so_far
        chunk_end = self._read_so_far + words_user_can_read
        chunk_words = words[chunk_start:chunk_end]
        self._read_so_far = chunk_end
        return " ".join(chunk_words)
    

