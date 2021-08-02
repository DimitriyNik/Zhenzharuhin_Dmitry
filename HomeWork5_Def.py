l = [1, 2, [2, 4, [[7, 8], 4, 6]]]


def sum_list(l, sum = 0):
    for i in l:
        if type(i) == list:
            sum += sum_list(i)
        else:
            sum += i
    return sum

print("Total sheet list =", sum_list(l))
    