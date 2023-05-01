시작
import random


def getDigits(num):
    return list(int(i) for i in str(num))


def noDuplicates(num):
    num_list = getDigits(num)
    if len(num_list) == len(set(num_list)):
        return True
    return False


def generateDigits():
    while True:
        num = random.randint(1000, 9999)
        if noDuplicates(num):
            return num


