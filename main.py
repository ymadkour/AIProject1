import robot
import Grid
'''
Created on Oct 30, 2013

@author: madkour
'''
def GenGrid():
    return Grid.Grid()

def Search(grid, strategy, visualize):
        
    if strategy == "BFS":
        grid.robot_parts[0].parts_list[0].bfs(grid.obstacles_locations, grid.robot_parts, grid.side_borders, grid.grid_size,0)
    elif strategy == "DFS":
        grid.robot_parts[0].parts_list[0].dfs(grid.obstacles_locations, grid.robot_parts, grid.side_borders, grid.grid_size,0)
    elif strategy == "IDFS": #Iterative Deepening
        grid.robot_parts[0].parts_list[0].ID(grid.obstacles_locations, grid.robot_parts, grid.side_borders, grid.grid_size)
    elif strategy == "A*":
        grid.robot_parts[0].parts_list[0].astar(grid.robot_parts, grid.side_borders, grid.obstacles_locations, grid.grid_size,0)
    elif strategy == "Greedy":
        grid.parts_locations[0].parts_list[0].greedy(grid.robot_parts, grid.side_borders, grid.obstacles_locations, grid.grid_size, 0)
    
    
grid = GenGrid()
print Search(grid,"Greedy",False)

# print part2.depthFirstSearch([7],myList,[1,5,6,10,11,15,16,20,21,25],5,[],["North","South","East","West"],False)
# print g.grid_size
# #print g.obstacle_number
# #print g.robot_parts
# #print g.parts_loctions
# #print g.obstacles_locations
# print g.side_borders
# #part5.Move('East', [7,1],myList , [1,4,5,8,9,12,13,16], 4)
# #print "##########"
# #print len(myList[0].parts)
