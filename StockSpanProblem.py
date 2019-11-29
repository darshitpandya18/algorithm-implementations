 #######################################
 ## Name: The Stock Span Problem      ##
 ## Owner: Darshit Pandya             ##
 ## Purpose: Data Structure Practice  ##
 #######################################

 ## Here we will consider that our Array is our stack
 ## And we will perform the stack operation
 ## to avoid time usage to write the Stack Class, we will import it directly 
 ## from the previously created Classes

import StackUsingLinkedList

def main(stack_object, stocks_prices):
	"""

	Arguments: 
		- stack_object: Stack Object that refers the stack
		- stock_prices: Stock Prices list values

	Return: 
		- stocks_span: Stock Span List
	
	Logic:
		- geeksforgeeks.org/the-stock-span-problem/
		- using stack
	"""
	stocks_span = list()
	len_ = len(stocks_prices)

	stocks_span.append(1) ###..... For the first element of the list
	stack_object.push(0)

	## We will check till stack is empty and the values of previous<=current
	for i in range(1, len_):
		while not stack_object.isEmpty() and stocks_prices[stack_object.root.data] <= stocks_prices[i]:
			stack_object.pop()
		

		if stack_object.isEmpty():
			stocks_span.append(i + 1)
		else:
			stocks_span.append(i - stack_object.root.data)
		stack_object.push(i)
	return stocks_span


if __name__ == '__main__':
	stack_object = StackUsingLinkedList.Stack()
	stocks_prices_list = [100, 80, 60, 70, 60, 75, 85]
	stocks_span = main(stack_object, stocks_prices_list)
	print(stocks_span)