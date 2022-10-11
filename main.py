inputvalues = input()
numbers = inputvalues.split()
for i in range(len(numbers)):
	numbers[i] = int(numbers[i]) 
smallest = numbers[0]
for i in range(len(numbers)):
    smallest = numbers[i]
    for j in range((len(numbers)-i)):
        if smallest > numbers[j+i]:
            smallest = numbers[j+i]
            smallest_position = j+i
    loan = numbers[i]
    numbers.remove(smallest)
    numbers.insert(smallest_position, loan)
    numbers.remove(numbers[i])
    numbers.insert(i, smallest)
    print(numbers)