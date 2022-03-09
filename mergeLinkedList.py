# This is an input class. Do not edit.
##algorithm
# create three pointers, one pointer for each list and one pointer poiting to
# prev of first pointer. compare the values of p1 and p2. if p1 is less than p2
# then dont change anything, just update prev and p1 pointers by 1
# otherwise set the prev next pointer to p2, new p2 becomes p2.next

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
	recursiveMerge(headOne,headTwo, None)
	return headOne if headOne.value < headTwo.value else headTwo


def recursiveMerge(p1, p2, p1Prev):
	if p1 is None:
		p1Prev.next=p2
		return
	if p2 is None:
		return
	if p1.value < p2.value:
		recursiveMerge(p1.next, p2, p1)
	else :
		if p1Prev is not None:
			p1Prev.next=p2
		newP2=p2.next
		p2.next=p1
		recursiveMerge(p1, newP2, p2)
