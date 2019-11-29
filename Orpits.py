#######################################
## Name: Orpits Problem ICPC test    ##
## Owner: Darshit Pandya             ##
## Purpose: Test                     ##
#######################################
from __future__ import print_function
all_lists =dict()

def print_(counter_, iterator_):
	all_lists[counter_] = "* "*iterator_

def main(initial_orpits):
	counter_ = -1
	current_orpits = initial_orpits
	
	while current_orpits>1 and counter_ < 13:
		if counter_ == -1:
			counter_ += 1
			print_(counter_, current_orpits)
		else:
			if current_orpits > 10:
				current_orpits = current_orpits//2
				counter_+=1
				print_(counter_, current_orpits)
			elif current_orpits >1 and current_orpits<=10:
				current_orpits = current_orpits + 3 - counter_
				counter_+=1
				print_(counter_, current_orpits)

	for key, val in all_lists.items():
		print(key,end="")
		print(val)

if __name__ == '__main__':
	initial_orpits = int(input().strip())
  	main(initial_orpits)     