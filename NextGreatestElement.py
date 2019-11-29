 #######################################
 ## Name: The Next Greatest Element   ##
 ## Owner: Darshit Pandya             ##
 ## Purpose: Data Structure Practice  ##
 #######################################

from StackUsingLinkedList import Stack

def main(stack_object, element_list):
 	"""
 	Arguments:
 		- stack_object: stack object
 		- element_list: List of all the elements

 	Return
 		- nge_list: List of the next greatest element for each of the element
 	"""
 	stack_object2 = Stack()
 	len_ = len(element_list)
 	nge_list = [-1]*len_
 	counter = len_ - 1

 	for element_ in element_list:
 		stack_object.push(element_)


 	while not stack_object.isEmpty():
 		while not stack_object2.isEmpty():
	 		if stack_object.root.data < stack_object2.root.data :
	 			nge_list[counter] = stack_object2.root.data
	 			break
	 		else:
 				stack_object2.pop()

 		stack_object2.push(stack_object.root.data)
 		stack_object.pop()
 		counter = counter - 1

 	return nge_list

if __name__ == '__main__':
 	stack_object = Stack()
 	elements_ = [3, 6, 5, 2, 11, 25, 25]
 	nge_list = main(stack_object, elements_)
 	print(nge_list)