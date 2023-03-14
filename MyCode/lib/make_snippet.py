def make_snippet1(text):
    return text


def make_snippet2(text):    
    words = text.split()
    return words
print(make_snippet2("one two three four five six"))


def make_snippet3(text):
    words = text.split()
    if len(words) <= 5:
        return True
    

def make_snippet4(text):
    words = text.split()
    if len(words) <= 5:
        return True
    else:
        return False


def make_snippet5(text):
    words = text.split()
    if len(words) <= 5:
        return " ".join(words)
    else:
        return False
print(make_snippet5("one two three four"))


def make_snippet6(text):
    words = text.split()
    if len(words) <= 5:
        return " ".join(words)
    else:
        return " ".join(words[:5])
print(make_snippet6("one two three four five six"))


def make_snippet7(text):
    words = text.split()
    if len(words) <= 5:
        return " ".join(words)
    else:
        return " ".join(words[:5]) + " ..."
print(make_snippet7("one two three four five six"))


def make_snippet8(text):
    words = text.split()
    if text == "":
        return "No text entered"
    elif len(words) <= 5:
        return " ".join(words)
    else:
        return " ".join(words[:5]) + " ..."
print(make_snippet8(""))

