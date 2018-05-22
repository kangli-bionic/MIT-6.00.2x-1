# You have a bucket with 3 red balls and 3 green balls. Assume that once you draw a ball out of the bucket, 
# you don't replace it. What is the probability of drawing 3 balls of the same color?

import random

def noReplacementSimulation(numTrials=100):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    numOfSuccess = 0
    bucket = ['r','r','r','g','g','g']

    for i in range(numTrials):
        ithchoice = random.sample(bucket,3)
        if ithchoice in [['r','r','r'],['g','g','g']]:
            numOfSuccess += 1
    return(numOfSuccess/numTrials)    

def main():
    numSim = 1000
    simresult = []

    for i in range(numSim):
        simresult.append(noReplacementSimulation(1000))

    # print(simresult)
    print(sum(simresult)/numSim) 
   
if __name__ == '__main__':
    main()

