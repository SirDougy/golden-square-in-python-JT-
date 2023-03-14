# def todo_checker1(text):
#     return text


# def todo_checker2(text):
#     return True


def todo_checker(text):
    if not text:
        raise Exception('ERROR - no text entered')
    if "#TODO" in text:
        print(f'TASK FOUND '+ (text))
        return True
    else:
        print('NO TASK FOUND')
        return False
    
