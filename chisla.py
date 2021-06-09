x="five one eleven four fifteen sixteen nineteen twelve eight seventeen ten three four three eleven"
x=x.split()
print(x)
dict={'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7,
 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13,
  'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18,
  'nineteen':19, 'twenty':20}
x=[dict[i] for i in x]
print(x)
x=list(set(x))
print(x)

print([i for i in x if i%2 == 1])
print('sum',sum([i for i in x if i%2 == 1]))

n=len(x)
for i in range(0, (n-2), 2):
    print(x[i])
    print('work 1 i 2=',+x[i]*x[i+1])
    print('sum 2 i 3=',+x[i+1]+x[i+2])




