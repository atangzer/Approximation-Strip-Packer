import numpy as np
from matplotlib import pyplot as plt

'''
Define the data using the test generator: 
    print("The possible generated test cases:")
    print("1) Random Case (n=100)")
    print("2) Diagonal Case (n=1000)")
    print("3) Mismatched Diagonal Case (n=1000)")
    print("4) Best Case (n=10)")
    print("5) Worst Case (n=10000)")
    print("6) All Pairs Case (n=1000)")
    print("7) Filled (No Gaps) Case (n=60)")
    print("8) Filled (With Gaps) Case (n=20)")
    print("9) Trivial Case (n=100)")

These are sorted by n, then used below:
cases = best, filled_withgaps, filled_nogaps, random, trivial, diagonal, mismatched_diag, allpairs, worst
times = [0.1003, 0.1113, 0.214, 0.3217, 0.3007, 3.016, 3.414, 2.782, 33.0037]

-Worst case isn't included below because it messes up the scale of the graph
'''

#For graph points (Use all test cases)
n_pts = [10, 20, 60, 100, 100, 1000, 1000, 1000]
#best, filled_withgaps, filled_nogaps, random, trivial, diagonal, mismatched_diag, allpairs
time_taken_pts = [0.1003, 0.1113, 0.214, 0.3217, 0.3007, 3.016, 3.414, 2.782] #Time taken in milliseconds to 4 decimal places; Time given is average of 3 executions

#For line graph (Only 1 test case for every n)
#Using random case for n=100, using mismatched diagonal case for n=1000
n_lines = [10, 20, 60, 100, 1000] #x-axis; Unsigned int; Strictly increasing only
time_taken_lines = [0.1003, 0.1113, 0.214, 0.3217, 3.414] #y-axis; Unsigned float; Dependent on amount of data (n)

#Scale the output graph properly
x_axis = np.arange(10, 1000, 50)
y_axis = np.arange(0.0, 3.5, 0.1)
plt.xticks(x_axis)
plt.yticks(y_axis)

#Format the graph
plt.title("Big-O of our NFDH implementation")
plt.xlabel("Number of items to place")
plt.ylabel("Time taken to place items (in ms)")

#Plot the graph, graphics are drawn in order of declaration
plt.plot(n_lines,time_taken_lines, 'b') #Line plot, color=blue
plt.plot(n_pts,time_taken_pts, 'or') #(x,y); color=red and marker=circle, marker only

plt.savefig("big-o_graph.png")
plt.show() #This pops the plot (clears it), must be done after everything
