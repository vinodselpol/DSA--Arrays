def sumOfLinkedLists(linkedListOne, linkedListTwo):
    newHeadPointer=LinkedList(0)
	currentNode=newHeadPointer
	carry=0
	
	nodeOne=linkedListOne
	nodeTwo=linkedListTwo
	
	while nodeOne is not None or nodeTwo is not None or carry!=0:
		valueOne=nodeOne.value if nodeOne is not None else 0
		valueTwo=nodeTwo.value if nodeTwo is not None else 0
		sum =valueOne + valueTwo + carry
		
		newValue=sum%10
		newNode=LinkedList(newValue)
		currentNode.next=newNode
		currentNode=newNode
		
		carry=sum//10
		
		nodeOne=nodeOne.next if nodeOne is not None else None
		nodeTwo=nodeTwo.next if nodeTwo is not None else None
		
	return newHeadPointer.next
