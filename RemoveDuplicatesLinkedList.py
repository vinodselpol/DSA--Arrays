def removeDuplicatesFromLinkedList(linkedList):
    currentNode=linkedList
	while currentNode is not None:
		nextDistinctNode = currentNode.next
		while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
			nextDistinctNode = nextDistinctNode.next
		
		currentNode.next=nextDistinctNode
		currentNode = nextDistinctNode
	return linkedList
