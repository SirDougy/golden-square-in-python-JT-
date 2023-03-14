# import datetime

# strftime('hms')

def estimate_reading_time(filename : str, words_per_minute : int):
    with open(filename) as f:
        lines = f.read().splitlines()
        lines = [i.replace(' ','') for i in lines]
        chars = ''.join(lines)
        char_count = len(chars)
        reading_time_seconds =  (char_count / words_per_minute) / 60
        return reading_time_seconds


words_per_minute = 200
reading_time_seconds = estimate_reading_time('test.txt', words_per_minute)


estimate_reading_time(filename : str, words_per_minute : int)

