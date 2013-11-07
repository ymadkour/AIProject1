import copy
import Node


class Part:
    """docstring for part"""
    def __init__(self, index, parts):
        self.index = index
        self.parts = parts
        
    def checkParts(self,other_list,other):
        if len(other_list) != self(other):
            return False
        counter = 0
        for p in range(0,len(other_list)):
            if other_list[p].parts== other[p].parts:
                counter +=1
        if  counter == len(other_list):
            return True
        else:
            return False   
        
    def bfs(self, obstacles, parts, borders, gridSize,index):
        
        direction = ["North","South","East","West"]
        _temp_length = len(parts)

        done_flag = False
        check = 0
              
        for counter in range(index,_temp_length):
            
            if done_flag == True:
                break

            if len(parts[counter].parent.parts_list) != len(parts[counter].parts_list):
                flag = False
                
   
                
            if parts[counter].enterd == False:
                for j in parts[counter].parts_list:
                    for i in range(0,len(direction)):
                            parts[counter].enterd = True           
                            _temp_parts_list = copy.deepcopy( parts[counter])
                            move_flag = j.Move(direction[i],obstacles,_temp_parts_list,borders,gridSize)
                            node = [Node.Node(parts[counter],direction[i],_temp_parts_list.parts_list,0,_temp_parts_list.cost)]
                            node[0].enterd = move_flag
                            parts += node
                                
                            if(len(_temp_parts_list.parts_list) == 1):
                                return True
                            
                            check = 0
                            
                    if done_flag == True:
                        break      
                            
            else:
                check +=1                            
                        
                    
        if done_flag == False and check != _temp_length * 4:
            self.bfs(obstacles, parts, borders, gridSize,_temp_length)             
        
        if(len(_temp_parts_list.parts_list) == 1):
            return True
        return False 
        
        
        
        
    def dfs(self, obstacles, parts, borders, gridSize,index):
        
        direction = ["North","South","East","West"]
        _temp_length = len(parts)
        counter1=0
        done_flag = False
        if(len(parts[_temp_length-1].parts_list) == 1):

            return True
                                  
        for counter in range(index,_temp_length):

            if len(parts[counter].parent.parts_list) != len(parts[counter].parts_list):
                flag = False
                
            else:
                counter1 = 0    
                for p in range(0,len(parts[counter].parent.parts_list)):
                    if parts[counter].parent.parts_list[p]._eq_( parts[counter].parts_list[p]) == True:
                            counter1 +=1
                    if  counter1 == len(parts[counter].parent.parts_list):
                        flag = True
                    else:
                        flag =  False   
            if flag == False:
                for j in parts[counter].parts_list:
                    if done_flag == True:
                        break
                    for i in range(0,len(direction)):
                            parts[counter].enterd = True           
                            _temp_parts_list = copy.deepcopy( parts[counter])
                            move_flag = j.Move(direction[i],obstacles,_temp_parts_list,borders,gridSize)
                            
                            node = [Node.Node(parts[counter],direction[i],_temp_parts_list.parts_list,0,_temp_parts_list.cost)]
                            node[0].enterd = move_flag
                            parts += node
                            if move_flag == True:
                                self.dfs(obstacles, parts, borders, gridSize,len(parts)-1)    
                            if(len(parts[len(parts)-1].parts_list) == 1):
                                return True                           
                        
        if(len(parts[len(parts)-1].parts_list) == 1):
            return True
        return False              
                    
            
    def dfIDs(self, obstacles, parts, borders, gridSize,index,limit,goal_limit):
        
        direction = ["North","South","East","West"]
        _temp_length = len(parts)
        my_limit = copy.deepcopy(limit)
        counter1=0
        if len(parts[_temp_length-1].parts_list) == 1 :
            return True
        if limit == goal_limit:
            return False

        my_limit += 1

        if len(parts[index].parent.parts_list) != len(parts[index].parts_list):
                flag = False
                
        else:
                counter1 = 0    
                for p in range(0,len(parts[index].parent.parts_list)):
        
                            if parts[index].parent.parts_list[p]._eq_( parts[index].parts_list[p]) == True:
                                    counter1 +=1
                            if  counter1 == len(parts[index].parent.parts_list):
                                flag = True
                            else:
                                flag =  False   
        if flag == False:
                for j in parts[index].parts_list:
                    
                    for i in range(0,len(direction)):
                            parts[index].enterd = True           
                            _temp_parts_list = copy.deepcopy( parts[index])
                            move_flag = j.Move(direction[i],obstacles,_temp_parts_list,borders,gridSize)
                            parts +=[Node.Node(parts[index],direction[i],_temp_parts_list.parts_list,0,_temp_parts_list.cost)]
                            if move_flag == True:
                                self.dfIDs(obstacles, parts, borders, gridSize,len(parts)-1,my_limit,goal_limit)           
                            if(len(parts[len(parts)-1].parts_list) == 1):
                                return True

        if(len(parts[len(parts)-1].parts_list) == 1):
           return True
        return False     
     
     
    def ID (self, obstacles, parts, borders, gridSize):
               
        limit = 1;
        length = len(parts)
        dif = length
         
        while True :
            (parts[0].parts_list[0]).dfIDs(obstacles,parts,borders,gridSize,len(parts)-1,0,limit)
            parts.append(parts[0])
            limit +=1;
            
            if len(parts)- length == dif or parts[len(parts)-2].parts_list == 1:
                break
            
            else:
                dif = len(parts) - length
                length = len(parts)
                
                 
    
    
    def greedy(self,parts,borders,obstacles,gridSize,check_flag):
        direction = ["North","South","East","West"]
        _temp_length = len(parts)
        flag = False

        if flag == False:
            temp_min_node = parts[len(parts)-1]
            min_index = len(parts)-1
            
            
            for j in range(0 ,len(parts)):
                    if temp_min_node.heurisitc_value > parts[j].heurisitc_value and parts[j].enterd == False:
                        temp_min_node = parts[j]
                        min_index = j
                    elif   parts[j].enterd == True:
                        check_flag +=1
    
            parts[min_index].enterd = True
            if  len(parts[min_index].parts_list) == 1 and parts[min_index].enterd == True:
                return True
            if check_flag == len(parts) or temp_min_node.heurisitc_value >= 1000:
                return False
                           

            for node in parts[min_index].parts_list:
                for i in range(0,len(direction)):           
                        _temp_parts_list = copy.deepcopy( parts[min_index])
                        move_flag = node.Move(direction[i],obstacles,_temp_parts_list,borders,gridSize)
                        
                        
                        
                        if move_flag == True:
                            node_heuristic = getHeuristic(_temp_parts_list.parts_list,gridSize)
                        else:
                            node_heuristic = 10000            
                        parts +=[Node.Node(parts[min_index],direction[i],_temp_parts_list.parts_list,node_heuristic,_temp_parts_list.cost)]
   
                           

   
        self.greedy(parts,borders,obstacles,gridSize,check_flag)
        
        for p in parts:
            if  len(p.parts_list) == 1 and p.enterd == True:
                return True             
        return False 
        
        
    
    def astar(self,parts,borders,obstacles,gridSize,check_flag):
        direction = ["North","South","East","West"]
        _temp_length = len(parts)
        flag = False
        if flag == False:
            temp_min_node = parts[len(parts)-1]
            min_index = len(parts)-1
            
            
            for j in range(0 ,len(parts)):
                    if temp_min_node.heurisitc_value+temp_min_node.cost > parts[j].heurisitc_value+parts[j].cost and parts[j].enterd == False:
                        temp_min_node = parts[j]
                        min_index = j
                    elif   parts[j].enterd == True:
                        check_flag +=1
    

            
            parts[min_index].enterd = True
            if check_flag == len(parts) or temp_min_node.heurisitc_value >= 10000:
                return False
            if len(parts[min_index].parts_list) == 1 and parts[min_index].enterd == True:
                return True
                           

            for node in parts[min_index].parts_list:
                for i in range(0,len(direction)):           
                        _temp_parts_list = copy.deepcopy( parts[min_index])
                        move_flag = node.Move(direction[i],obstacles,_temp_parts_list,borders,gridSize)
                        
                        
                        if move_flag == True:
                        
                            node_heuristic = getHeuristic(_temp_parts_list.parts_list,gridSize)
                        else:
                            node_heuristic = 10000            
                        parts +=[Node.Node(parts[min_index],direction[i],_temp_parts_list.parts_list,node_heuristic,_temp_parts_list.cost+parts[min_index].cost -1)]
   
                           
                       

   
        self.astar(parts,borders,obstacles,gridSize,check_flag)             
        for p in parts:
            if  len(p.parts_list) == 1 and p.enterd == True:
                return True 
        return False 
               
               
    def Move(self, direction, obstacles, parts, borders, gridSize):
        
            temp_self = copy.deepcopy(self)
            temp_self_list = copy.deepcopy(self.parts)
            
         
            mt = 0
            while (True):

                mt += 1
                parts.cost = mt
                flag = 0
                counter_position = 0
                tempPosition = 0
                for position in temp_self.parts:
                    
                    if direction == "North":

                        tempPosition = position - gridSize
                        
                        """ check if the part hit the borders"""
                        if tempPosition <= 0:
                            flag -= 1                        

                    elif direction == "South":

                        tempPosition = position + gridSize
                        """ check if the part hit the borders"""
                        if tempPosition > (gridSize ** 2):
                            flag -= 1

                    elif direction == "East":
                        _tempPosition = position + 1
                        if position in borders and (_tempPosition in borders or _tempPosition > (gridSize ** 2)):
                            flag -=1
                        else:    
                            tempPosition = position + 1
                        

                    elif direction == "West":
                        _tempPosition = position - 1
                        if position in borders and (_tempPosition in borders or _tempPosition < 1):
                            flag -=1    
                        else:
                            tempPosition = position - 1              

                    """ check if the part hit an obstacle"""

                    if tempPosition in obstacles:
                            flag -= 1
                            flag1 = True
                            if direction == "North":
                                    new_part_position = [(tempPosition + gridSize)]
                                    
                            elif direction == "South":
                                new_part_position = [(tempPosition - gridSize)]
                                    
                            elif direction == "East":
                                new_part_position = [(tempPosition - 1)]
                            elif direction == "West":
                                new_part_position = [(tempPosition + 1)]

                            for old_position in temp_self_list:
                                
                                differenace = old_position - temp_self_list[counter_position]
                               

                                if differenace != 0:    
                                    new_part_position.append(new_part_position[0] + differenace)
                                if mt == 1:
                                    flag1 = False
                            for p in parts.parts_list:
                                if self._eq_(p) == True:            
                                    p.parts = new_part_position
                                    
                            
                            return flag1      




                    """ check if there is a hit between parts """        
                    for part in parts.parts_list:
                        for temp_p in part.parts:
                            if tempPosition == temp_p:
                                flag1 = True
                            else:
                                flag1 = False 
                        if flag1 == True and self._eq_(part) == False:
                            flag += gridSize
                        
                            for part_position in part.parts:
                                
                                if direction == "North":
                                    new_part_position = [(tempPosition + gridSize)]
                                    
                                elif direction == "South":
                                    new_part_position = [(tempPosition - gridSize)]
                                    
                                elif direction == "East":
                                    new_part_position = [(tempPosition - 1)]
                                elif direction == "West":
                                    new_part_position = [(tempPosition + 1)]

                                for old_position in temp_self_list:
                                
                                    differenace = old_position - temp_self_list[counter_position]
                                    
                                    if differenace != 0:    
                                        new_part_position.append(new_part_position[0] + differenace) 

                            new_part_position += part.parts
                            new_part_position.sort()
                            new_part = Part(self.index, new_part_position)
                            
                            for p in parts.parts_list:
                                if self._eq_(p) == True:
                                    parts.parts_list.remove(p)
                            parts.parts_list.remove(part)
                            new_part_position1 = []
                            
                            while True:
                                break_counter = 0
                                stop_flag = False
                                for pat in parts.parts_list:
                                    for tem_pat in pat.parts:
                                        for pa in new_part_position:
                                            
                                            if direction == "North" or direction == "South":
                                                if tem_pat == pa -1 or tem_pat == pa + 1:
                                                    new_part_position1 += pat.parts
                                                    try:
                                                        parts.parts_list.remove(pat)
                                                    except:
                                                        print "try and catch"
                                                    stop_flag = True
                                                    break
                                                else:
                                                    break_counter +=1   
                                                
                                            elif direction == "East" or direction == "West":
                                                if tem_pat == pa - gridSize or tem_pat == pa + gridSize:
                                                    new_part_position1 += pat.parts
                                                    try:
                                                        parts.parts_list.remove(pat)
                                                    except:
                                                        print "try and catch"
                                                    stop_flag = True
                                                    break
                                                else:
                                                    break_counter +=1  
                                              
                                                
                                    if stop_flag  == True:
                                     break
                                if break_counter >= len(parts.parts_list):
                                     break
                                
                                       
                            
                            new_part.parts += new_part_position1    
                            parts.parts_list.append(new_part)
                            parts.parts_list = list(set(parts.parts_list))
                            return True
                        
                    temp_length = len(self.parts) - 1                        
                    if flag < 0 and temp_length == counter_position :
                        
                        return  False

                    temp_self.parts [counter_position] = tempPosition
                    counter_position += 1
 
 
    def _eq_ (self, other):
        if self.index == other.index:                        
            if self.parts == other.parts:               
                return True
        else:          
            return False   
         
         
def isSameRow (part1,part2,gridSize):
    for i in range (1, gridSize+1):
        start = i*gridSize - gridSize + 1
        end = i*gridSize
        if start<=part1 and part1<=end and start<=part2 and part2<=end:
            return True
    return False

def getHeuristicHelper(part1, part2, gridSize):
    if isSameRow(part1, part2, gridSize):
        return abs(part1-part2) - 1
    else:
        row1 = (part1//gridSize)+1
        row2 = (part2//gridSize)+1
        
        diff = abs(row1 - row2)
        if diff == 0:
            return 1;
        maximum = max (part1, part2)
        minimum = min (part1, part2)
        
        heuristic1 = diff
        
        newLoc = maximum - (gridSize*diff)
        
        heuristic2 = abs(newLoc-minimum) - 1
#         sameRow = maximum - diff #As if i raised the part to be in the same row with the other part
#         
#         heuristic2 = abs(minimum - sameRow)-1
        
        return heuristic1 + heuristic2

def getHeuristicHelper2(part,listOfParts ,gridSize):
    allHeuristics2 = []
    for part1 in listOfParts:
        allHeuristics3 = []
        for part2 in part.parts:
            #allHeuristics3 = []
            for part3 in part1.parts:
                heuristic3 = getHeuristicHelper(part3, part2, gridSize)
                allHeuristics3.append(heuristic3)
        allHeuristics2.append(min(allHeuristics3))
    allHeuristics2.remove(-1)
    return min(allHeuristics2)
        
def getHeuristic(listOfParts, gridSize):
    if len(listOfParts) == 1:
        return 0 
    allHeuristics = 0
    for part in listOfParts:
        allHeuristics += getHeuristicHelper2(part,listOfParts, gridSize)
    if allHeuristics > 1:
        allHeuristics = allHeuristics//2
    return allHeuristics