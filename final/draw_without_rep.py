import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    bucket = ['r','r','r','r','g','g','g','g']
    success = 0

    for i in range(numTrials):
        sample = random.sample(bucket,3)

        if sample in [['r','r','r'], ['g','g','g']]:
            success += 1

    print('Fraction of successful trails is: {0:.2f}'.format(success/numTrials))

drawing_without_replacement_sim(1000)