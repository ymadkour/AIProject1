import random
import Grid
import copy

'''
Created on Oct 30, 2013

@author: madkour
'''
def GenGrid():
    return Grid.Grid()

def Search(grid, strategy, visualize):
    heuristic_function = random.randint(0,1)
    if strategy == "Greedy" or strategy == "A*":
        if heuristic_function == 0:
            print "manhatten1"
        else:
            print "manhatten2"
        
    flag = False;    
    if strategy == "BFS":
         flag = grid.parts_locations[0].parts_list[0].bfs(grid.obstacles_locations, grid.parts_locations, grid.side_borders, grid.grid_size,0,)
    elif strategy == "DFS":
         flag = grid.parts_locations[0].parts_list[0].dfs(grid.obstacles_locations, grid.parts_locations, grid.side_borders, grid.grid_size,0)
    elif strategy == "IDFS": #Iterative Deepening
         flag = grid.parts_locations[0].parts_list[0].ID(grid.obstacles_locations, grid.parts_locations, grid.side_borders, grid.grid_size)
    elif strategy == "A*":
         flag = grid.parts_locations[0].parts_list[0].astar(grid.parts_locations, grid.side_borders, grid.obstacles_locations, grid.grid_size,0,heuristic_function)
    elif strategy == "Greedy":
         flag = grid.parts_locations[0].parts_list[0].greedy(grid.parts_locations, grid.side_borders, grid.obstacles_locations, grid.grid_size, 0,heuristic_function)
    
    cost = 0;
    final_list_sequence = []
    
    for i in range(0,len(grid.parts_locations)):
                if len(grid.parts_locations[i].parts_list) == 1 and grid.parts_locations[i].enterd == True:
                    cost = grid.parts_locations[i].cost
                    temp_node = grid.parts_locations[i]
                    flag = True
                    #print cost
                    break
        
        
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

    
                
    no_nodes =0;    
    if strategy == "IDFS" or  strategy == "DFS"  or strategy == "BFS" :
        no_nodes = len(grid.parts_locations)     
    
    if strategy == "A*" or strategy == "Greedy":
        for i in range(0,len(grid.parts_locations)):
            if grid.parts_locations[i].enterd == True:
                no_nodes +=1
                
                
   
    
    i = len(final_list_sequence)-2
    final = copy.deepcopy(final_list_sequence)   
    if final_list_sequence != []:
        if visualize == True:
            while i >=0:   
                print "------------------------"
                temp = copy.deepcopy(grid.obstacles_locations)
                if visualize == True:
                    
                    print visualization(final_list_sequence[i],grid.grid_size,temp)
                i -= 1
                print "------------------------"
                
        print "Cost:"
        print cost
        print "number of nodes choosen for expansion during the search"
        print no_nodes        
    else:
        print "no sequence was found"
            
    
    return [final,[cost],[no_nodes]]    
    

def visualization(parts,gridsize,obstacles):
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


        
grid = GenGrid()
strategy=raw_input('Please enter the strategy you want to execute:("Greedy","A*","BFS","DFS","IDFS") \n')
visualize_flag=raw_input('Visual presentation of the board as it undergoes to discovered tsolution, if one was found:(F\T)"note any other input will be count as false" \n')
if visualize_flag == 'T':
    print Search(grid,strategy,True)
else:
   print Search(grid,strategy,False) 


