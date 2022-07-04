import random

def return_short_url():
    sample = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    length = 7
    result = ''.join((random.choice(sample)) for i in range(length))
    return result
