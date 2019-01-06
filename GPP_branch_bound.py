# -*- coding: utf-8 -*-
"""
@author: Darshit Pandya
@Module: Graph Partitioning Problem using branch & bound;backtracking

"""

input_matrix, best_solution_partition = list() , 0        
lowerbound, upperbound = 0, 0
levels = 0
row_columns = 0
coverage_stack = []

def vertical_lower_calc(fixed_elements_list):
    '''
    Step 1: sum smallest n/2 elements of columns
    '''
    sums = []
    minimum_tofind = (row_columns//2 - len(fixed_elements_list))
    iteration_list = [i for i in range(1, row_columns + 1) if not i in fixed_elements_list]
    for column in iteration_list:
            temp_list = []
            temp_sum = 0
            for fixed_row in fixed_elements_list:
                    temp_sum += input_matrix[fixed_row-1][column-1]
                    
            for row in iteration_list:
                    temp_list.append(input_matrix[row-1][column-1])
            temp_list = sorted(temp_list)
            sums.append(sum(temp_list[1:minimum_tofind + 1]) + temp_sum)     
    lowerbound = second_level_vertical_lower_calc(sums)
    return lowerbound

def second_level_vertical_lower_calc(sums):
    
    '''Step 2: from the sum of each column, sum n/2 minimum
       After finding lower and upper bound, just call the build function
       to start building the partitioning problem
    '''
    global lowerbound
    sums = sorted(sums)
    lowerbound = sum(sums[:row_columns/2])
    return lowerbound
    
def upper_bound_compute():
    global upperbound
    for i in range(0, row_columns/2):
            for j in range(row_columns/2, row_columns):
                    upperbound += input_matrix[i][j]

def collect_estimation(list_of_choices):
    
    ''' For each and every combination of vertices passed
    in the list of choices at a particular moment, call the lowerbound
    for the same'''
    estimations = []
    for choice in list_of_choices:
        estimations.append(vertical_lower_calc(choice))    
    return estimations
    
def print_the_selections(estimations, current_choices):
    '''
    Print the selections
    '''
    for estimation, current_choice in zip(estimations, current_choices):
        print current_choice, "--->" , estimation

def build(k):
    '''
    build funnction takes integer k as an input and doesn't return anything. Hence it is a void type.
    k: works around the number of vertices
    Note: levels are always equal to n/2
    In the build, every possibilty at each iteration for all levels should be covered using recursion
    '''
    global coverage_stack
    estimations = []
    current_choices = []    
    if k == 1:
        current_choices =  [[i] for i in range(1, (row_columns - (levels - k) + 1))]
    else:
        selectedNext = coverage_stack[-1]
        coverage_stack.remove(selectedNext)
        for i in range(selectedNext[-1] + 1, row_columns -(levels - k) + 1):
            temp = selectedNext
            current_choices.append(temp + [i])
        
        #print current_choices
    estimations = collect_estimation(current_choices)
    estimations, current_choices = zip(*sorted(zip(estimations, current_choices)))
    current_choices = list(current_choices)
    print_the_selections(estimations, current_choices)
    coverage_stack.extend(current_choices[-i] for i in range(1, len(current_choices) + 1))
    
    while not coverage_stack == []:
        if k<row_columns//2:
            build(k+1)
  
def graph_partitioning_bb(input_matrix):
    global row_columns
    row_columns = len(input_matrix)
    upper_bound_compute()
    vertical_lower_calc([])
    global levels
    levels = len(input_matrix) // 2
    build(1)
    print "Partition with minimum length is: "
    print "Length of the best partition found is: ", best_solution_partition

if __name__ == '__main__':
                
        input_matrix.append([0, 3, 4, 10, 32, 5, 15, 20])
        input_matrix.append([3, 0, 25, 8, 7, 12, 6, 9])
        input_matrix.append([4, 25, 0, 19, 13, 8, 10, 11])
        input_matrix.append([10, 8, 19, 0, 42, 4, 28, 15])
        input_matrix.append([32, 7, 13, 42, 0, 16, 70, 8])
        input_matrix.append([5, 12, 8, 4, 16, 0, 10, 9])
        input_matrix.append([15, 6, 10, 28, 70, 10, 0, 14])
        input_matrix.append([20, 9, 11, 15, 8, 9, 14, 0])  
        
        graph_partitioning_bb(input_matrix)
