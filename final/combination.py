
import numpy as np

def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

def getTotal(choices, res):
    tot = 0
    for i in range(len(res)):
        # print('multipliers:', res[i], choices[i])
        tot += res[i]*choices[i]
    return tot

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    If choices = [1,2,2,3] and total = 4 you should return either [0 1 1 0] or [1 0 0 1]
    If choices = [1,1,3,5,3] and total = 5 you should return [0 0 0 1 0]
    If choices = [1,1,1,9] and total = 4 you should return [1 1 1 0]
    """
    length = len(choices)
    res = np.zeros(length, int)
    bestres = []
    
    for i in range( 2**length):
        binary = bin(i)[2:]
        res = np.array(list(binary), dtype = int)
        res = np.append(np.zeros(length-len(binary), dtype=int), res)
        # print(choices)
        # print(res)
        # print(getTotal(choices,res))
        if getTotal(choices, res) == total:
            bestres.append(res)
        # print('*'*20)
    
    while len(bestres) == 0:
        total -= 1
        res = np.zeros(length, int)
    
        for i in range(2**length):
            binary = bin(i)[2:]
            res = np.array(list(binary), dtype=int)
            res = np.append(np.zeros(length-len(binary), dtype=int), res)
            # print(choices)
            # print(res)
            # print(getTotal(choices,res))
            if getTotal(choices, res) == total:
                bestres.append(res)
            # print('*'*20)

    # print(bestres)

    best = bestres[0]
    for i in bestres:
        digitsum = np.sum(i)
        if digitsum < np.sum(best):
            best = i

    return best

    
        

        


    # return res
    

print("Best result:", find_combination([1, 1, 1, 9], 4))
