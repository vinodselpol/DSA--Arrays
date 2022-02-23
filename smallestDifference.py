def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	pointer1 = 0
	pointer2 = 0
	smallest = float("inf")
	difference = float("inf")
	smallestPair =[]
	while pointer1 < len(arrayOne) and pointer2 < len(arrayTwo):
		value1 = arrayOne[pointer1]
		value2 = arrayTwo[pointer2]
		difference = abs(value2 - value1)
		if difference == 0:
			return [value1, value2]
		elif value1 > value2:
			pointer2 +=1
		elif value1 < value2:
			pointer1 +=1
		if smallest > difference:
			smallest = difference
			smallestPair =[value1, value2]
	return smallestPair
