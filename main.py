import robot
import Grid
'''
Created on Oct 30, 2013

@author: madkour
'''
def GenGrid():
    return Grid.Grid()

def Search(grid, strategy, visualize):
    cost = 0
    flag = False;    
    if strategy == "BFS":
         flag = grid.parts_locations[0].parts_list[0].bfs(grid.obstacles_locations, grid.parts_locations, grid.side_borders, grid.grid_size,0)
    elif strategy == "DFS":
         flag = grid.parts_locations[0].parts_list[0].dfs(grid.obstacles_locations, grid.parts_locations, grid.side_borders, grid.grid_size,0)
    elif strategy == "IDFS": #Iterative Deepening
         flag = grid.parts_locations[0].parts_list[0].ID(grid.obstacles_locations, grid.parts_locations, grid.side_borders, grid.grid_size)
    elif strategy == "A*":
         flag = grid.parts_locations[0].parts_list[0].astar(grid.parts_locations, grid.side_borders, grid.obstacles_locations, grid.grid_size,0)
    elif strategy == "Greedy":
         flag = grid.parts_locations[0].parts_list[0].greedy(grid.parts_locations, grid.side_borders, grid.obstacles_locations, grid.grid_size, 0)
    
    
    for i in range(0,len(grid.parts_locations)):
            if len(grid.parts_locations[i].parts_list) == 1 and grid.parts_locations[i].enterd == True:
                cost = grid.parts_locations[i].cost
                temp_node = grid.parts_locations[i]
                #print cost
                break
    
    final_list_sequence = []
    final_list_direction = []
    if flag == True:
         while temp_node != []:
             t=[]
             for p in temp_node.parts_list:
                 t.append(p.parts)
             s =[]
             for i in t:
                 s += i     
             final_list_sequence += [s]
             final_list_direction += [temp_node.direction]
             temp_node = temp_node.parent
    print "Diretion"
    for i in range(0, len(final_list_sequence)):

        
        if i < len(final_list_direction):
            print final_list_direction[i]
        print final_list_sequence[i]
        print "----------------"
        
                  
    no_nodes =0;    
    if strategy == "IDFS" or  strategy == "DFS"  or strategy == "BFS" :
        no_nodes = len(grid.parts_locations)     
    
    if strategy == "A*" or strategy == "Greedy":
        for i in range(0,len(grid.parts_locations)):
            if grid.parts_locations[i].enterd == True:
                no_nodes +=1
    
    return flag    
    

def visualize(parts,gridsize,obstacles):
    result = ""
    
    for i in range(1,gridsize*gridsize+1):
        if i in parts and i % gridsize == 0:
            result += " R  " +" \n"
            parts.remove(i)
        elif i in parts and not i%gridsize == 0:
            result += " R  "
            parts.remove(i)
        elif i in obstacles and i % gridsize == 0:
            result += " O  " +" \n"
            obstacles.remove(i)
        elif i in obstacles and not i%gridsize == 0:
            result += " O  "
            obstacles.remove(i)
            
        else:
            if i % gridsize == 0:
                if i < 10:
                    result += " 0"+ str(i)+" \n"
                else:
                    result += " "+ str(i)+" \n"
            elif i <10:
                result += " 0" + str(i) + " "
            else:
                result += " " + str(i) + " "
    return result


print visualize([1,2,3,4,5,6,7],6,[35,36])
        
# grid = GenGrid()
# print Search(grid,"Greedy",False)
#print Search(grid,"BFS",False)
#print Search(grid,"DFS",False)
#print Search(grid,"IDFS",False)
#print Search(grid,"A*",False)

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
