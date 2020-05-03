# #For graph points (Use all test cases)
# n_pts = [10, 20, 60, 100, 200, 300, 400, 1000]
# #best, filled_withgaps, filled_nogaps, trivial, random, diagonal, mismatched_diag, allpairs
# time_taken_pts = [0.1003, 0.1113, 0.214, 0.3007, 0.6943, 1.0137, 1.3083] #Time taken in milliseconds to 4 decimal places; Time given is average of 3 executions
#
# #For line graph (Only 1 test case for every n)
# n_lines = [10, 20, 60, 100, 200, 300, 400, 1000] #x-axis; Unsigned int; Strictly increasing only
# time_taken_lines = [0.1003, 0.1113, 0.214, 0.3007, 0.6943, 1.0137, 1.3083, 2.782] #y-axis; Unsigned float; Dependent on amount of data (n)
#
# #Scale the output graph properly
# x_axis = np.arange(10, 1000, 50)
# y_axis = np.arange(0.0, 3.5, 0.2)
# plt.xticks(x_axis)
# plt.yticks(y_axis)