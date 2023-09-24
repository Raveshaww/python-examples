# returns a tuple
def sum_all_nums(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(sum_all_nums(1,2,3,4,5,6,7,8,9,10))

def contains_purple(*args):
    if "purple" in args:
        return True
    return False