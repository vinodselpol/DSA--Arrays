# This is the class of the input linked list.
# we need 4 elements to know OH,OT,NH,NT(o -original, N- new)
# traverse though the list and get the total length of list. and do k%list length
# if o then return the head
# then we need to identif the new tail position
# new tail position is length - k if k > 0 else k
#then traverse though the tailposition to find the new tail
# once found, new tail next = new head
#set tail next to none and list tail next to head and return new head
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    listLength=1
	listTail=head
	while listTail.next is not None:
		listTail=listTail.next
		listLength+=1
	offset = abs(k)% listLength
	if offset==0:
		return head
	newTailPos=listLength-offset if k > 0 else offset
	newTail = head
	for i in range(1,newTailPos):
		newTail=newTail.next
	newHead=newTail.next
	newTail.next=None
	listTail.next=head
	return newHead
