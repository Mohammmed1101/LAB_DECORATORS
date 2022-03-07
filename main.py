


def my_decorator(*args):
    def checkArg(char1):
        if type(char1) == str and len(char1) > 5:
            return char1 , len(char1) , type(char1)
        raise ValueError("The argument should be string and it should have more than 5 characters.!")

    return checkArg
        

@my_decorator
def char(char11):
    return char11

print(char("kjkyyg"))



