import random

def generate_number(start:int,end:int) -> int:
    '''
    Generate a random number between start and end.
    '''
    return random.randint(start, end)
