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
            smallest_position = j+i+1
    print(smallest)
    loan = numbers[i]
    numbers.remove(smallest)
    print("removing1:", numbers)
    numbers.insert(smallest_position, loan)
    print("inserting1:", numbers)
    numbers.remove(numbers[i])
    print("removing2:", numbers)
    numbers.insert(i, smallest)
    print("inserting2:", numbers)
    print(numbers)