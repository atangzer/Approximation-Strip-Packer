#'source venv/bin/activate' to activate venv
#'deactivate' to exit venv

#Sizes 10-10000
#We are using Next-Fit Decreasing Height (NFDH)

#normal var is the texture atlas width (inf. height, finite set width); All values given will be relative to this var

#All written test cases will have a newline after the last entry

def main():

    # Make sure only 1 of the funcs is ran at once, manually comment out the rest
    testcases = 8
    print("The possible generated test cases:")
    print("1) Diagonal Case")
    print("2) Best Case")
    print("3) Worst Case")
    print("4) All Pairs Case")
    print("5) Filled (No Gaps) Case")
    print("6) Filled (With Gaps) Case")
    print("7) Mismatched Diagonal Case")
    print("8) Random Case")

    test = int(input("Please choose a test case number: "))
    assert test > 0 and test <= testcases, "Please enter an existing test case" #Throws AssertionError if bad choice


    switcher = {  # Map of generating functions
        1: diagonal_case,
        2: best_case,
        3: worst_case,
        4: allpairs_case,
        5: filled_nogaps_case,
        6: filled_withgaps_case,
        7: mismatched_diag_case,
        8: random_case,
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
def diagonal_case(): #Largest item first, each item is smaller than the last (size=10000)
    res = []
    normal = 10000
    n = 10000
    res.append(f'{normal} {n}')

    for i in reversed(range(1,n+1)):
        res.append(f'{i} {i}')
    return res

def best_case(): #All items can fit in the same bin, use smallest size (10)
    res = []
    normal = 10
    n = 10
    res.append(f'{normal} {n}')
    for h in reversed(range(1,n+1)):
        res.append(f'{h} {1}') #all items have width 1
    return res

def worst_case(): #No 2 items can go in the same bin, use largest size (10000)
    res = []
    normal = 10000
    n = 10000
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
    n = 10000
    res.append(f'{normal} {n}')

    height = 10 #For this case, all items have set height of 10

    for i in range(3333): #1/3 of the items are width 4, 1/3 of the items are width 6
        res.append(f'{height} 4')
        res.append(f'{height} 6')
    for i in range(3334): #The other (1/3) + 1 items are width 5; There are a even amount of 5's
        res.append(f'{height} 5')

    #If completely optimal, would have no whitespace in bins;
    #Would have exactly 3333 + (3334/2) = 5000 completely filled bins

    return res

def filled_nogaps_case(): #Completely filled bins (sqaures) as optimal case
    res = []
    normal = 10
    n = 100 #TODO: Determine this after drawing out the 5 squares on paper
    res.append(f'{normal} {n}')


    #Optimal solution will be 5 bins used (no whitespace); Proof is on attached doc
    return res

def filled_withgaps_case(): #Not quite completely filled squares, but no squares large enough to fill in the gaps (as optimal case)
    res = []
    normal = 10
    n = 100  # TODO: Determine this after drawing out the 5 squares on paper
    res.append(f'{normal} {n}')


    #Optimal Solution will be 5 bins used (with a little whitespace); Proof is on attached doc
    return res

def mismatched_diag_case(): #Mismatched diagonals, including really long but short items, really tall but thin items, and everything in between
    res = []
    normal = 10000
    n = 10000
    res.append(f'{normal} {n}')

    for i in range(1,n+1):
        res.append(f'{i} {(n+1) - i}')

    return res

def random_case(): #really big, completely random case
    from random import randrange
    res = []
    normal = 10000
    n = 10000
    res.append(f'{normal} {n}')

    for i in range(10000):
        height = randrange(1,10001)
        width = randrange(1,10001)
        res.append(f'{height} {width}')

    return res

if (__name__ == '__main__'):
    main()