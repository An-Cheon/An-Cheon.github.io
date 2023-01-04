import random
def happiness():
    return 1
def sadness():
    return -1
def depression():
    return -16
def birth():
    fate = random.random()
    if fate > 0.9:
        return 'happy life'
    if fate > 0.2:
        return 'average life'
    return 'sad life'
def life():
    fate = birth()
    for day in range(365 * 78):
        1

print(fate)
