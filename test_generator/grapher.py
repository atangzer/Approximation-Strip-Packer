import numpy as np
from matplotlib import pyplot as plt

'''
Define the data using the test generator:
    print("The possible generated test cases:")
    print("1) Random Case 500 Items (n=500)")
    print("2) Random Case 5k Items (n=5000)")
    print("3) Random Case 7k Items (n=7000)")
    print("4) Random Case 9k Items (n=9000)")
    print("5) Diagonal Case (n=3000)")
    print("6) Mismatched Diagonal Case (n=4000)")
    print("7) Best Case (n=10)")
    print("8) Worst Case (n=10000)")
    print("9) All Pairs Case (n=1000)")
    print("10) Filled (No Gaps) Case (n=60)")
    print("11) Filled (With Gaps) Case (n=20)")
    print("12) Trivial Case (n=100)")

-The smaller test cases are mostly used to test correctness, they are included here for brevity
    -Performance testing is mostly done with the huge random generated cases, those will be the significant points on the graph

These are sorted by n, then used below
'''

#All test cases must have different values of n (no looping graphs)
#The average time out of 3 runs is used, rounded to 4 decimal places
testcases = {  # {int n: float time_taken}
    10: 0.088, # best_case
    20: 0.125, # filled_withgaps_case
    60: 0.22, # filled_nogaps_case
    100: 0.3287, # trivial_case
    500: 1.4937, # random_case_500
    1000: 2.491, # allpairs_case
    3000: 9.7453, # diagonal_case
    4000: 13.167, # mismatched_diag_case
    5000: 16.6687, # random_case_5k
    7000: 23.08, # random_case_7k
    9000: 29.8653, # random_case_9k
    10000: 32.853, #worst_case
}
n = list(testcases.keys()) # x-axis
time_taken = list(testcases.values()) # y-axis

#Format the graph
plt.title("Big-O of Our NFDH Implementation")
plt.xlabel("Number of items to place")
plt.ylabel("Time taken to place items (in ms)")

#Plot the graph, graphics are drawn in order of declaration

#Line of best fit
coef = np.polyfit(n, time_taken, 1)
poly1d_fn = np.poly1d(coef) #lambda x: estimate for y
plt.plot(n, poly1d_fn(n), 'k')

plt.plot(n, time_taken, 'c--') #Dotted line plot (connect the dots only), color=blue
plt.plot(n, time_taken, 'or') #(x,y); color=red and marker=circle, marker only

plt.savefig("big-o_graph.png")
plt.show() #This pops the plot (clears it), must be done after everything
