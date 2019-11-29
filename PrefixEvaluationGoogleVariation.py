## ( + 5 6 ( * 2 3 4( + 3 4...) 7 8) 123 456)
## The variation is that the number can be any length long unlike 1
## which is used conventionally in all the prefix evaluation

class Solution:

	def __init__(self, expression_):
		self.expression = expression_

	def evaluate_expression(self):
		'''
		Function: It evaluates the given expression in reverse 
		for prefix evaluation

		If operand, push. If operator. pop two elements from the stack, evaluate them and push it back

		We can use an auxiliary stack too to know about the whole number formed
		'''
		stack_1 = []
		stack_2 = []

		for i in range(-1, -len(self.expression) - 1, -1):
		 	if not self.expression[i] in ["*", "+", "/", "-"," "]:
		 		stack_2.append(self.expression[i])

		 	if self.expression[i] == " ":
		 		temp = ""
		 		while stack_2:
		 			temp += stack_2.pop()
		 		if temp:
		 			stack_1.append(temp)

		 	if self.expression[i] in ["*", "+", "/", "-"]:
		 		str_1 = stack_1.pop()
		 		str_2 = stack_1.pop()
		 		val = eval(str_1 + self.expression[i] + str_2)
		 		stack_1.append(str(val))

		final_val = stack_1.pop()
		return final_val

solution = Solution("+ - 2 7 * 8 / 12 4")
final_value = solution.evaluate_expression()
print(final_value)