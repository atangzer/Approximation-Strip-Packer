#'source venv/bin/activate' to activate venv
#'deactivate' to exit venv

#Sizes 10-10000
#We are using Next-Fit Decreasing Height (NFDH)

#We might need more width units (if no floats) to diff between 10000 rectangles
#normal var is the texture atlas width (inf. height, finite set width); All values given will be relative to this var

def main():

    name = input("Test case filename: ") #This will overwrite existing test cases

    with open(name+'.txt', 'w', encoding='utf-8') as outfile:
        #Make sure only 1 of the funcs is ran at once, manually comment out the rest
        res = [] #All functions should return a list of ints
        res = diagonal_case()



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

    for i in reversed(range(1,10001)):
        res.append(f'{i} {i}')
    return res

def best_case(): #No 2 items can go in the same bin, largest size (10000)
    normal = 10000
    pass

def worst_case(): #All items can fit in the same bin (width 4-6), smallest size (10)
    normal = 10
    pass

def allpairs_case(): #All items are between 4 and 6 in width, no more than 2 items in one bin
    normal = 10
    pass

def filled_nogaps_case(): #Completely filled bins (sqaures) as optimal case
    normal = 10
    pass

def filled_withgaps_case(): #Not quite completely filled squares, but no squares large enough to fill in the gaps (as optimal case)
    normal = 10
    pass



if (__name__ == '__main__'):
    main()