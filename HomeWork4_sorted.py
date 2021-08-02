l=[1, 212, 23, 2, 335, 202, 3, 250, 334, 4, 201, 24, 25, 7, 8, 200, 9, 210,  12, 30, 211, 15, 333, 101]
l=sorted(l)
#print(l)
def get_range(l):
    new = ''
    start = l[0]
    finish = l[0] 
    l.append('')
    for i in range(len(l)):
        if l[i] == finish + 1:
            finish = l[i]
            continue
        if start == finish:
            new += str(start)+" "
        else:
            new += str(start)+"-"+str(finish) +" "
        start = finish = l[i]
        str_final = ", ".join(new.split())
    return str_final

print(get_range(l))
