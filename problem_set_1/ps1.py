###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):   
    trips = []
    cowscopy=[]
    #sorted cows
    for cow in sorted(cows, key=cows.get, reverse=True):
        cowscopy.append([cow, cows[cow]])
    #start from ith cow
#    print('\n',cowscopy,'\n')
    while len(cowscopy) > 0:
        trip = []
        available=limit
        i=0
        while available > 0 and i < len(cowscopy):
            if cowscopy[i][1] <= available:
                trip.append(cowscopy[i][0])
                available -= cowscopy[i][1]
                del cowscopy[i]
                i-=1
            i+=1
        trips.append(trip)
    return trips
# Problem 2
def brute_force_cow_transport(cows,limit=10):
  
    for items in get_partitions(list(cows)):
        key = True  
#        print(items)
        for part in items:
#            print( part)       
            sum = 0
            for cow in part:       
                sum += cows[cow]
#            print('sum:', sum) 
            if sum > limit:
                key=False
                break
        if key == False:
#            print('key is False')
            pass   
        else:
            return items
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows("ps1_cow_data.txt")
    limit=10
    print('Greedy Algorithm')
    start = time.time()
    print(len(greedy_cow_transport(cows, limit)))
    end = time.time()
    print('running time:',end - start)
    
    print('Brute Force Algorithm')
    start = time.time()
    print(len(brute_force_cow_transport(cows, limit)))
    end = time.time()
    print('running time:',end - start)

"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

#cows = load_cows("ps1_cow_data.txt")
#limit=10
#print('\n',cows,'\n')

#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))

compare_cow_transport_algorithms()
