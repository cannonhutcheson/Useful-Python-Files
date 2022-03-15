
# list_of_args is a list that may be filled with booleans or expressions that evaluate to booleans.

def exclusive_or(list_of_args):
    if list_of_args[0] == list_of_args[1]:
        # print("False. Not an exclusive or.")
        return False
    else:
        # print("True. This is an exclusive or.")
        return True        
