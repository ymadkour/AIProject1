import robot
import Grid
'''
Created on Oct 30, 2013

@author: madkour
'''

gridSize = 4
part2 = robot.Part(1,[15])
part3 = robot.Part(2,[9])
part4 =robot.Part(3,[13])
part5 = robot.Part(4,[16])
myList = [part2,part3,part4,part5]

"""print part2.depthFirstSearch([1,7,15],myList,[1,4,5,8,9,12,13,16],4,0,[],["North","South","East","West"])"""

g =  Grid.Grid()
#part2 = g.parts_loctions[0]



print part2.depthFirstSearch([7],myList,[1,5,6,10,11,15,16,20,21,25],5,[],["North","South","East","West"],False)
print g.grid_size
#print g.obstacle_number
#print g.robot_parts
#print g.parts_loctions
#print g.obstacles_locations
print g.side_borders
#part5.Move('East', [7,1],myList , [1,4,5,8,9,12,13,16], 4)
#print "##########"
#print len(myList[0].parts)
