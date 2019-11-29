## Backtracking solution to find the maximum of non-adjacent neighbors
import copy
class Solution:
    
    def __init__ (self, input_array):
        self.array = input_array
        #self.tracker = dict()
        self.max_sum = 0
        self.max_tuple = []

    
    def backtrack(self, n, start = 0, temp_array = []):
        """
        Functionality: Backtracks to find each of the possible solution
        
        Arguments:
        - start: start index from where to traverse the array
        
        Returns when the start_index goes beyond the length of the array
        """
        if start >= n:
            if self.max_sum < sum(temp_array):
                self.max_tuple = copy.copy(temp_array)
                self.max_sum = sum(temp_array)
            return
                
        temp_ = temp_array
        for iterator_ in range(start, n):
            temp_.append(self.array[iterator_])
            self.backtrack(n, iterator_ + 2, temp_)
            temp_.pop()
        return
    def find_solution(self):
        n = len(self.array)
        _ = self.backtrack(n)
        print(self.max_sum)
        print(self.max_tuple)
    
    
solution = Solution([10, 55, 6, 20, 25, 56, 15])
solution.find_solution()