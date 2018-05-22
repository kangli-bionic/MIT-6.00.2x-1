# 6.00.2x Problem Set 2: Simulating robots

import copy
import math
import random
import numpy as np
import ps2_visualize
import pylab

##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.5:
#from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5 

# For Python 3.6:
from ps2_verify_movement36 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6


# === Provided class Position
class Position(object):
   """
   A Position represents a location in a two-dimensional room.
   """
   def __init__(self, x, y):
       """
       Initializes a position with coordinates (x, y).
       """
       self.x = x
       self.y = y
        
   def getX(self):
       return self.x
    
   def getY(self):
       return self.y
    
   def getNewPosition(self, angle, speed):
       """
       Computes and returns the new Position after a single clock-tick has
       passed, with this object as the current position, and with the
       specified angle and speed.

       Does NOT test whether the returned position fits inside the room.

       angle: number representing angle in degrees, 0 <= angle < 360
       speed: positive float representing speed

       Returns: a Position object representing the new position.
       """
       old_x, old_y = self.getX(), self.getY()
       angle = float(angle)
       # Compute the change in position
       delta_y = speed * math.cos(math.radians(angle))
       delta_x = speed * math.sin(math.radians(angle))
       # Add that to the existing position
       new_x = old_x + delta_x
       new_y = old_y + delta_y
       return Position(new_x, new_y)

   def __str__(self):  
       return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
   """
   A RectangularRoom represents a rectangular region containing clean or dirty
   tiles.

   A room has a width and a height and contains (width * height) tiles. At any
   particular time, each of these tiles is either clean or dirty.
   """
   def __init__(self, width, height):
       """
       Initializes a rectangular room with the specified width and height.

       Initially, no tiles in the room have been cleaned.
       titles=[]
           for i in range(width):
               row=[]
               for j in range(height):
                   row[j] = False
               titles.append(row)
       width: an integer > 0
       height: an integer > 0
       """
       self.width = width
       self.height = height
       #self.tiles = np.full((width,height),False)
       titles=[]
       for i in range(width):
           row=[]
           for j in range(height):
               row.append(False)
           titles.append(row)   
       self.tiles = titles
        
   def showTiles(self):
       for w in self.tiles:
           print(w,'\n')   

   def cleanTileAtPosition(self, pos):
       """
       Mark the tile under the position POS as cleaned.

       Assumes that POS represents a valid position inside this room.

       pos: a Position
       """
       #self.tiles[int(pos.getX()),int(pos.getY())] = True
       self.tiles[int(pos.getX())][int(pos.getY())] = True

   def isTileCleaned(self, m, n):
       """
       Return True if the tile (m, n) has been cleaned.

       Assumes that (m, n) represents a valid tile inside the room.

       m: an integer
       n: an integer
       returns: True if (m, n) is cleaned, False otherwise
       """
       #return self.tiles[m,n]
       return self.tiles[m][n]
   def getNumTiles(self):
       """
       Return the total number of tiles in the room.

       returns: an integer
       """
       return self.width*self.height

   def getNumCleanedTiles(self):
       """
       Return the total number of clean tiles in the room.

       returns: an integer
       """
       #return np.count_nonzero(self.tiles==True)
       count = 0 
       for w in self.tiles:
           for h in w:
               if h == True:
                   count += 1
       return count

   def getRandomPosition(self):
       """
       Return a random position inside the room.

       returns: a Position object.
       """
       return Position(random.randint(0,self.width-1),random.randint(0,self.height-1))

   def isPositionInRoom(self, pos):
       """
       Return True if pos is inside the room.

       pos: a Position object.
       returns: True if pos is in the room, False otherwise.
       """
       return((0 <= pos.getX() < self.width )and (0 <= pos.getY() < self.height) )


# === Problem 2
class Robot(object):
   """
   Represents a robot cleaning a particular room.

   At all times the robot has a particular position and direction in the room.
   The robot also has a fixed speed.

   Subclasses of Robot should provide movement strategies by implementing
   updatePositionAndClean(), which simulates a single time-step.
   """
   def __init__(self, room, speed):
       """
       Initializes a Robot with the given speed in the specified room. The
       robot initially has a random direction and a random position in the
       room. The robot cleans the tile it is on.

       room:  a RectangularRoom object.
       speed: a float (speed > 0)
       """
       self.room = room
       self.speed = speed
       self.position = room.getRandomPosition()
       self.direction = random.randrange(360)
       self.room.cleanTileAtPosition(self.position)

   def getRobotPosition(self):
       """
       Return the position of the robot.

       returns: a Position object giving the robot's position.
       """
       return self.position
    
   def getRobotDirection(self):
       """
       Return the direction of the robot.

       returns: an integer d giving the direction of the robot as an angle in
       degrees, 0 <= d < 360.
       """
       return self.direction

   def setRobotPosition(self, position):
       """
       Set the position of the robot to POSITION.

       position: a Position object.
       """
       self.position = position
       #self.room.cleanTileAtPosition(position)

   def setRobotDirection(self, direction):
       """
       Set the direction of the robot to DIRECTION.

       direction: integer representing an angle in degrees
       """
       self.direction = direction

   def updatePositionAndClean(self):
       """
       Simulate the passage of a single time-step.

       Move the robot to a new position and mark the tile it is on as having
       been cleaned.
       """
       raise NotImplementedError # don't change this!


# === Problem 3
class StandardRobot(Robot):
   """
   A StandardRobot is a Robot with the standard movement strategy.

   At each time-step, a StandardRobot attempts to move in its current
   direction; when it would hit a wall, it *instead* chooses a new direction
   randomly.
   """
   def updatePositionAndClean(self):
       """
       Simulate the passage of a single time-step.

       Move the robot to a new position and mark the tile it is on as having
       been cleaned.
       """
       pos = self.getRobotPosition()
       pos2 = pos.getNewPosition(self.getRobotDirection(),self.speed)
       while self.room.isPositionInRoom(pos2) == False:
           self.setRobotDirection(random.randrange(360))
           pos = self.getRobotPosition()
           pos2 = pos.getNewPosition(self.getRobotDirection(),self.speed)

       self.room.cleanTileAtPosition(pos)
       self.setRobotPosition(pos2)


# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                 robot_type):
   """
   Runs NUM_TRIALS trials of the simulation and returns the mean number of
   time-steps needed to clean the fraction MIN_COVERAGE of the room.

   The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
   speed SPEED, in a room of dimensions WIDTH x HEIGHT.

   num_robots: an int (num_robots > 0)
   speed: a float (speed > 0)
   width: an int (width > 0)
   height: an int (height > 0)
   min_coverage: a float (0 <= min_coverage <= 1.0)
   num_trials: an int (num_trials > 0)
   robot_type: class of robot to be instantiated (e.g. StandardRobot or
               RandomWalkRobot)
   """
   time_steps = []

   for i in range(num_trials):

       #anim = ps2_visualize.RobotVisualization(num_robots, width, height, delay=1/120)

       room = RectangularRoom(width,height)
       coverage = room.getNumCleanedTiles()/room.getNumTiles()
       robots=[]
       steps = 0
   
       for x in range(num_robots):
           robots.append(robot_type(room,speed))
    
       while coverage < min_coverage:

           #anim.update(room, robots)

           for robot in robots:
               robot.updatePositionAndClean()
           steps += 1
           coverage = room.getNumCleanedTiles()/room.getNumTiles()
           #print('steps:',steps,'coverage:',coverage)

       #anim.done()

       time_steps.append(steps)      
    
   return  float("{0:.2f}".format(sum(time_steps) / (len(time_steps))))
# Uncomment this line to see how much your simulation takes on average
#print(runSimulation(10, 0.3, 20, 20, 0.75, 1, StandardRobot))
#print(runSimulation(10, 0.3, 20, 20, 0.75, 1, RandomWalkRobot))

# === Problem 5
class RandomWalkRobot(Robot):
   """
   A RandomWalkRobot is a robot with the "random walk" movement strategy: it
   chooses a new direction at random at the end of each time-step.
   """
   def updatePositionAndClean(self):
       """
       Simulate the passage of a single time-step.

       Move the robot to a new position and mark the tile it is on as having
       been cleaned.
       """
       pos = self.getRobotPosition()
       self.setRobotDirection(random.randrange(360))
       pos2 = pos.getNewPosition(self.getRobotDirection(),self.speed)
       while self.room.isPositionInRoom(pos2) == False:
           self.setRobotDirection(random.randrange(360))
           pos = self.getRobotPosition()
           pos2 = pos.getNewPosition(self.getRobotDirection(),self.speed)

       self.room.cleanTileAtPosition(pos)
       self.setRobotPosition(pos2)


def showPlot1(title, x_label, y_label):
   """
   What information does the plot produced by this function tell you?
   """
   num_robot_range = range(1, 11)
   times1 = []
   times2 = []
   for num_robots in num_robot_range:
       print("Plotting", num_robots, "robots...")
       times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
       times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
   pylab.plot(num_robot_range, times1)
   pylab.plot(num_robot_range, times2)
   pylab.title(title)
   pylab.legend(('StandardRobot', 'RandomWalkRobot'))
   pylab.xlabel(x_label)
   pylab.ylabel(y_label)
   pylab.show()

showPlot1('Time It Takes 1 - 10 Robots To Clean 80% Of A Room','number of robots','time-steps')
    
def showPlot2(title, x_label, y_label):
   """
   What information does the plot produced by this function tell you?
   """
   aspect_ratios = []
   times1 = []
   times2 = []
   for width in [10, 20, 25, 50]:
       height = 300//width
       print("Plotting cleaning time for a room of width:", width, "by height:", height)
       aspect_ratios.append(float(width) / height)
       times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
       times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
   pylab.plot(aspect_ratios, times1)
   pylab.plot(aspect_ratios, times2)
   pylab.title(title)
   pylab.legend(('StandardRobot', 'RandomWalkRobot'))
   pylab.xlabel(x_label)
   pylab.ylabel(y_label)
   pylab.show()

showPlot2('Time It Takes Two Robots To Clean 80% Of Variously Shaped Rooms ','Aspect Ratio','Time-Steps')
    




def song_playlist(songs, max_size):

   """
   songs: list of tuples, ('song_name', song_len, song_size)
   max_size: float, maximum size of total songs that you can fit

   Start with the song first in the 'songs' list, then pick the next 
   song to be the one with the lowest file size not already picked, repeat

   Returns: a list of a subset of songs fitting in 'max_size' in the order 
            in which they were chosen.
   """
   songs_remaining = copy.deepcopy(songs)
   remaining = max_size
   result=[]

   try:
       song = songs_remaining.pop(0)
   except:
       return []

   if song[2] <= max_size:
       result.append(song[0])
       remaining -= song[2]
   else:
       return result
 
   songs_remaining.sort(key=lambda tup: tup[2])
    
   while(True):
       try:
           song = songs_remaining.pop(0)
       except:
           break
       if remaining >= song[2]:
           result.append(song[0])
           remaining -= song[2]
       else:
           break

   return result

songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size = 12.2
song_playlist(songs, max_size)


def max_contig_sum(L):
   """ L, a list of integers, at least one positive
   Returns the maximum sum of a contiguous subsequence in L """
   max = L[0]
   for i in range(1,len(L)+1):#num of contigous elem
       for j in range(len(L)):#starting index
           try:
               l = L[j:j+i]
               if sum(l) > max:
                   max = sum(l)
                   print(l)
           except:
               break
   return max

l=[3, 4, -8, 15, -1, 2]
max_contig_sum(l)

def solveit(test):
   """ test, a function that takes an int parameter and returns a Boolean
       Assumes there exists an int, x, such that test(x) is True
       Returns an int, x, with the smallest absolute value such that test(x) is True 
       In case of ties, return any one of them. 
   """
   i=0
   while(True):
       if test(i)==True:
           return i
       elif test(-i)==True:
           return -i
       i+=1

#### This test case prints 49 ####
def f(x):
   return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
   return x == 0
print(solveit(f))

def stdDevOfLengths(L):
   if len(L) == 0:
       return float('NaN')
   L2 = [len(i) for i in L]
   mean = sum(L2)/len(L2)
   sd = (sum([(mean-i)**2 for i in L2])/len(L2))**0.5
   return sd

L = ['apples', 'oranges', 'kiwis', 'pineapples']
L = ['*'*10,'*'*4,'*'*12,'*'*15,'*'*20,'*'*5]
stdDevOfLengths(L2)
10, 4, 12, 15, 20, 5

import random
import matplotlib.pylab as plt
dist = []
for i in range(10000):
   dist.append(random.gauss(0,30))
a = plt.hist(dist,30)
plt.show(a)
