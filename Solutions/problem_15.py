def lattice(n):
    numbers = [1]
    if n == 1:
        return 2
    numbers.append(n)
    while len(numbers) < n-1:
        for i in range(2,n):
            numbers.append(sum(numbers))
            print(numbers)
    numbers.append(2*numbers[n-2])
    print(numbers)
    return 2*sum(numbers)

print(lattice(4))