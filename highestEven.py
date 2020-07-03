# Print the highest even number in a list
def highest_even(l):
    x=l[0]
    for i in l[1:]:
        if i%2==0 and i>=x:
            x=i
    return(x)

li = list(map(int,input('Enter numbers:').strip().split()))
print(highest_even(li))
