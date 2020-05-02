#'source venv/bin/activate' to activate venv
#'deactivate' to exit venv

#Sizes 10-10000
#We are using Next-Fit Decreasing Height (NFDH)

#normal var is the texture atlas width (inf. height, finite set width); All values given will be relative to this var

#All written test cases will have a newline after the last entry

def main():

    # Make sure only 1 of the funcs is ran at once, manually comment out the rest
    testcases = 9
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

    test = int(input("Please choose a test case number: "))
    assert test > 0 and test <= testcases, "Please enter an existing test case" #Throws AssertionError if bad choice


    switcher = {  # Map of generating functions
        1: random_case,
        2: diagonal_case,
        3: mismatched_diag_case,
        4: best_case,
        5: worst_case,
        6: allpairs_case,
        7: filled_nogaps_case,
        8: filled_withgaps_case,
        9: trivial_case,
    }
    generator = switcher.get(test) #Get the proper test generating function
    name = generator.__name__ #Name the output the same as the function name + .txt; This will overwrite existing test cases


    with open(name+'.txt', 'w', encoding='utf-8') as outfile:

        #All functions should return a list of ints
        res = generator() #Execute the generating function

        randomizer(res) #Comment this out when need not random output
        res_str = linewriter(res)
        outfile.write(res_str)
    print('Done') #No error handling done

def linewriter(lst): #Since .writelines(lst) doesn't actually write '\n''s
    res = ''
    for line in lst:
        res += f'{line}\n' #Last newline should be fine
    return res

def randomizer(lst): #void
    from random import shuffle  # void shuffle(list)
    header = lst.pop(0)
    shuffle(lst)
    lst.insert(0, header)


#Cases; should be same with or without random order of input
#f'{width} {height}'
def diagonal_case(): #Largest item first, each item is smaller than the last (size=10000)
    res = []
    n = 1000
    normal = n
    res.append(f'{normal} {n}')

    for i in reversed(range(1,n+1)):
        res.append(f'{i} {i}')
    return res


def best_case(): #All items can fit in the same bin, use smallest size (10)
    res = []
    n = 10
    normal = n
    res.append(f'{normal} {n}')
    for h in reversed(range(1,n+1)):
        res.append(f'{1} {h}') #all items have width 1
    return res


def worst_case(): #No 2 items can go in the same bin, use largest size (10000)
    res = []
    n = 10000
    normal = n
    res.append(f'{normal} {n}')

    count = 5001 #As long as the width and height of all items are larger than half the bin width, no 2 items will ever fit together in the same bin
    for i in range(10000):
        res.append(f'{count} {count}')

        if(count >= 10000): #reset the count whenever it reaches the max size of the box
            count = 5001
        else:
            count+=1

    return res


#No need to reverse the range iterators, entries will all get shuffled anyway
def allpairs_case(): #All items are between 4 and 6 in width, no more than 2 items in one bin
    res = []
    normal = 10
    n = 1000
    res.append(f'{normal} {n}')

    height = 10 #For this case, all items have set height of 10

    for i in range(333): #1/3 of the items are width 4, 1/3 of the items are width 6
        res.append(f'4 {height}')
        res.append(f'6 {height}')
    for i in range(334): #The other (1/3) + 1 items are width 5; There are a even amount of 5's
        res.append(f'5 {height}')

    #If completely optimal, would have no whitespace in bins;
    #Would have exactly 3333 + (3334/2) = 5000 completely filled bins
    return res


def filled_nogaps_case(): #Completely filled bins (sqaures) as optimal case
    res = []
    normal = 10
    n = 60 #12 items every 4 bins, 4 * 5 loop iters = 20 bins total, therefore 12 * 5 = 60 items total
    res.append(f'{normal} {n}')

    #Make 4 * 5 = 20 completely filled bins in optimal case
    for i in range(5):
        #f'{width} {height}'
        #Each box is numbered according to attached diagram
        res.append('5 10') #1
        res.append('5 10') #2
        res.append('10 5') #3
        res.append('10 5') #4
        res.append('5 7') #5
        res.append('5 3') #6
        res.append('5 4') #7
        res.append('5 6') #8
        res.append('1 5') #9
        res.append('9 5') #10
        res.append('8 5') #11
        res.append('2 5') #12

    #Optimal solution will be 4 bins used per loop iter (no whitespace); Proof is on attached doc
    return res


def filled_withgaps_case(): #Not quite completely filled squares, but no squares large enough to fill in the gaps (as optimal case)
    res = []
    normal = 10
    n = 20 #4 items per bin, 5 bins total, therefore 4 * 5 = 20 items total
    res.append(f'{normal} {n}')

    #Makes 1 * 5 = 5 almost filled bins (with a small 1x1 square sized empty space in center of each bin) in optimal case
    for i in range(5):
        #f'{width} {height}'
        #Each box is numbered according to attached diagram
        res.append('3 10') #1
        res.append('7 4') #2
        res.append('6 1') #3
        res.append('7 5') #4

    #Optimal Solution will be 5 bins used (with a little whitespace); Proof is on attached doc
    return res


def mismatched_diag_case(): #Mismatched diagonals, including really long but short items, really tall but thin items, and everything in between
    res = []
    n = 1000
    normal = n
    res.append(f'{normal} {n}')

    for i in range(1,normal+1): #f'{width} {height}'
        res.append(f'{i} {(normal+1) - i}')

    return res


def random_case(): #really big, completely random case
    from random import randrange
    res = []
    n = 100
    normal = n
    res.append(f'{normal} {n}')

    for i in range(n):
        width = randrange(1,n+1)
        height = randrange(1,n+1)
        res.append(f'{width} {height}')

    return res


def trivial_case(): #Every item is exactly the width of 1 bin, no whitespace
    res = []
    n = 100
    normal = n
    res.append(f'{normal} {n}')

    for i in range(n):
        res.append(f'{n} {n}') #width==height

    return res


if (__name__ == '__main__'):
    main()