def mult_three(maximum):
    '''Returns multiples of three under maximum in a list.'''
    barf = []
    for number in range(1,maximum+1):
        if number % 3 == 0:
            barf.append(number)
    return barf

def mult_five(maximum):
    '''Returns multiples of three under maximum in a list.'''
    cloudy = []
    for i in range(1,maximum+1):
        if i % 5 == 0:
            cloudy.append(i)
    return cloudy
            

window = mult_three(999) + mult_five(999)
dups = set(window)
answer = sum(dups)
print(answer)