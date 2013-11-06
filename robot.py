from Queue import *
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
        counter1=0
        done_flag = False
        check = 0
              
        for counter in range(index,_temp_length):
            
            if done_flag == True:
                break

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
                    for i in range(0,len(direction)):           
                            _temp_parts_list = copy.deepcopy( parts[counter].parts_list)
                            j.Move(direction[i],obstacles,_temp_parts_list,borders,gridSize)
                            print "%%%%%%%%%%%"
                            print direction[i]
                            print j.parts
                            for px in _temp_parts_list:
                                print px.parts
                            print "%%%%%%%%%%%"
                            
                            parts +=[Node.Node(parts[counter],direction[i],_temp_parts_list,0,0)]
                                
                            if(len(_temp_parts_list) == 1):
                                done_flag = True
                                break
                            
                            check = 0
                            
                    if done_flag == True:
                        break      
                            
            else:
                check +=1                            
                        
                    
        if done_flag == False and check != _temp_length * 4:
            self.bfs(obstacles, parts, borders, gridSize,_temp_length)             
        else:
            return parts 
        
        
        
        
    def dfs(self, obstacles, parts, borders, gridSize,index):
        
        direction = ["North","South","East","West"]
        _temp_length = len(parts)
        counter1=0
        done_flag = False
        if(len(parts[_temp_length-1].parts_list) == 1):

            return parts
                                  
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
                            _temp_parts_list = copy.deepcopy( parts[counter].parts_list)
                            move_flag = j.Move(direction[i],obstacles,_temp_parts_list,borders,gridSize)
                            print "%%%%%%%%%%%"
                            print direction[i]
                            print j.parts
                            for px in _temp_parts_list:
                                print px.parts
                            print "%%%%%%%%%%%"
                            
                            parts +=[Node.Node(parts[counter],direction[i],_temp_parts_list,0,0)]
                            if move_flag == True:
                                self.dfs(obstacles, parts, borders, gridSize,len(parts)-1)    
                            if(len(parts[len(parts)-1].parts_list) == 1):
                                done_flag = True
                                break                           
                        
        return parts              
                    
            
    def dfIDs(self, obstacles, parts, borders, gridSize,index,limit,goal_limit):
        
        direction = ["North","South","East","West"]
        _temp_length = len(parts)
        my_limit = copy.deepcopy(limit)
        counter1=0
        if(len(parts[_temp_length-1].parts_list) == 1 or limit == goal_limit):
            return parts

        my_limit += 1

        if len(parts[index].parent.parts_list) != len(parts[index].parts_list):
                flag = False
                
        else:
                counter1 = 0    
                for p in range(0,len(parts[index].parent.parts_list)):
                            print len(parts)
                            print index
                            print p
        
                            if parts[index].parent.parts_list[p]._eq_( parts[index].parts_list[p]) == True:
                                    counter1 +=1
                            if  counter1 == len(parts[index].parent.parts_list):
                                flag = True
                            else:
                                flag =  False   
        if flag == False:
                for j in parts[index].parts_list:
                    
                    for i in range(0,len(direction)):
                                       
                            _temp_parts_list = copy.deepcopy( parts[index].parts_list)
                            move_flag = j.Move(direction[i],obstacles,_temp_parts_list,borders,gridSize)
                            print "%%%%%%%%%%%"
                            print direction[i]
                            print j.parts
                            for px in _temp_parts_list:
                                print px.parts
                            print "%%%%%%%%%%%"
                            parts +=[Node.Node(parts[index],direction[i],_temp_parts_list)]
                            if move_flag == True:
                                self.dfIDs(obstacles, parts, borders, gridSize,len(parts)-1,my_limit,goal_limit)           
                            if(len(parts[len(parts)-1].parts_list) == 1):
                                break

        return parts     
     
     
    def ID (self, obstacles, parts, borders, gridSize):
               
        limit = 1;
        length = len(parts)
        dif = length
         
        while True :
            (parts[0].parts_list[0]).dfIDs(obstacles,parts,borders,gridSize,len(parts)-1,0,limit)
            parts.append(parts[0])
            print dif
            print len(parts)
            limit +=1;
            
            if len(parts)- length == dif or parts[len(parts)-2].parts_list == 1:
                break
            
            else:
                dif = len(parts) - length
                length = len(parts)
                
                
    """self is a node """ 
              
    def expandNode(self,parts,borders,obstacles,gridSize):
        expanded_nodes = []
        direction = ["North","South","East","West"]
          
        
        for i in range(0,len(direction)):
            temp_parts = copy.deepcopy(parts) 
            temp_self = copy.deepcopy(self) 
            flag = temp_self.Move(direction[i], obstacles,temp_parts.parts_list, borders, gridSize)
            
            if flag == False:
                node = [Node.Node(parts.parts_list,direction[i],temp_parts.parts_list,100,100)]
            elif flag == True and len(parts.parts_list) == len(temp_parts.parts_list):                
                node = [Node.Node(parts.parts_list,direction[i],temp_parts.parts_list,temp_parts.heurisitc_value,1)]
            elif flag == True and len(parts.parts_list) != len(temp_parts.parts_list):               
                node = [Node.Node(parts.parts_list,direction[i],temp_parts.parts_list,temp_parts.heurisitc_value - 1,0)]         
            print direction[i]    
            print node[0].heurisitc_value
            expanded_nodes += [flag] + node   
        
        return expanded_nodes
    
    
    
    def checkGoal(self,parts_list):
        return 1
        
    
    
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
    
            print "%%%%%%%%%%%"
            print temp_min_node.direction
            for px in temp_min_node.parts_list:
                print px.parts
            print "%%%%%%%%%%%"
            parts[min_index].enterd = True
            if check_flag == len(parts) or (len(parts[min_index].parts_list) == 1 and parts[min_index].enterd == True):
                return parts
                           

            for node in parts[min_index].parts_list:
                for i in range(0,len(direction)):           
                        _temp_parts_list = copy.deepcopy( parts[min_index])
                        move_flag = node.Move(direction[i],obstacles,_temp_parts_list,borders,gridSize)
                        
                        
                        
                        if move_flag == True:
                           node_heuristic = node.checkGoal(_temp_parts_list.parts_list)
                        else:
                            node_heuristic = 10000            
                        parts +=[Node.Node(parts[min_index],direction[i],_temp_parts_list.parts_list,node_heuristic,_temp_parts_list.cost)]
   
                           

   
        self.greedy(parts,borders,obstacles,gridSize,check_flag)             
        return parts 
        
        
    
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
    
            print "%%%%%%%%%%%"
            print temp_min_node.direction
            print temp_min_node.heurisitc_value
            print temp_min_node.cost
            for px in temp_min_node.parts_list:
                print px.parts
            print "%%%%%%%%%%%"
            parts[min_index].enterd = True
            if check_flag == len(parts) or (len(parts[min_index].parts_list) == 1 and parts[min_index].enterd == True):
                return parts
                           

            for node in parts[min_index].parts_list:
                for i in range(0,len(direction)):           
                        _temp_parts_list = copy.deepcopy( parts[min_index])
                        move_flag = node.Move(direction[i],obstacles,_temp_parts_list,borders,gridSize)
                        
                        
                        if move_flag == True:
                           node_heuristic = node.checkGoal(_temp_parts_list.parts_list)
                        else:
                            node_heuristic = 10000            
                        parts +=[Node.Node(parts[min_index],direction[i],_temp_parts_list.parts_list,node_heuristic,_temp_parts_list.cost+parts[min_index].cost)]
   
                           
                       

   
        self.astar(parts,borders,obstacles,gridSize,check_flag)             
        return parts 
               

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
                            
                            parts.parts_list.append(Part(self.index, new_part_position))
                            for p in parts.parts_list:
                                if self._eq_(p) == True:
                                    parts.parts_list.remove(p)
                            parts.parts_list.remove(part)
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
         






test=[Node.Node(Node.Node([],"",[],0,0),"",[Part(1,[4]),Part(2,[7]),Part(3,[1])],2,0)]

print Part(1,[1]).astar(test,[1,4,5,8,9,12,13,16],[12],4,0)
#Part(1,[1]).ID([12],test,[1,4,5,8,9,12,13,16],4)
#(test[0].parts_list[0]).expandNode(test[0],[1,4,5,8,9,12,13,16],[12],4)



