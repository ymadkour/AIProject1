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
                            
                            parts +=[Node.Node(parts[counter],direction[i],_temp_parts_list)]
                                
                            if(len(_temp_parts_list) == 1):
                                done_flag = True
                                break
                            
                            check = 0
            else:
                check +=1                            
                        
                    
        if done_flag == False and check != _temp_length * 4:
            self.dfs(obstacles, parts, borders, gridSize,_temp_length)             
        else:
            return parts 
        
        
        
        
    def dfs(self, obstacles, parts, borders, gridSize,index):
        
        direction = ["North","South","East","West"]
        _temp_length = len(parts)
        counter1=0
        done_flag = False
        check = 0
        if(len(parts[_temp_length-1].parts_list) == 1):
            done_flag = True
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
                    for i in range(0,len(direction)):           
                            _temp_parts_list = copy.deepcopy( parts[counter].parts_list)
                            move_flag = j.Move(direction[i],obstacles,_temp_parts_list,borders,gridSize)
                            print "%%%%%%%%%%%"
                            print direction[i]
                            print j.parts
                            for px in _temp_parts_list:
                                print px.parts
                            print "%%%%%%%%%%%"
                            
                            parts +=[Node.Node(parts[counter],direction[i],_temp_parts_list)]
                            if move_flag == True:
                                self.dfs(obstacles, parts, borders, gridSize,_temp_length)    
                            if(len(_temp_parts_list) == 1):
                                done_flag = True
                                break
                            
                            check = 0
            else:
                check +=1                            
                        
        return parts              
                    
            
    def dfIDs(self, obstacles, parts, borders, gridSize,index,limit,goal_limit):
        
        direction = ["North","South","East","West"]
        _temp_length = len(parts)
        my_limit = copy.deepcopy(limit)
        counter1=0
        done_flag = False
        check = 0
        if(len(parts[_temp_length-1].parts_list) == 1 or limit == goal_limit):
            done_flag = True
            return parts
                                  

        my_limit += 1
        
        if index == 16:
           t = len(parts[index].parent.parts_list)
           n =len(parts[index].parts_list)      

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
                                done_flag = True
                                break
                            
                            check = 0
        else:
                check +=1                            
                        
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
            if len(parts) == 55:
                te = 0
            if len(parts)- length == dif or parts[len(parts)-2].parts_list == 1:
                break
            
            else:
                dif = len(parts) - length
                length = len(parts)
                
                
              


    def depthFirstSearch(self, obstacles, parts, borders, gridSize,result_list,directions):


             _resutl_list = result_list[:]
             _resutl_length = len(result_list)
             _temp_parts = copy.deepcopy(parts)
             _temp_length = len(parts)
             string_direction = ""
             t = [""]
             if len(parts) == 1:
                 print "done"
                 return ["."]
             
             for counter in range(0,len(parts)):
                 print "test"
                 if "North" in directions and (_temp_parts[counter].Move("North",obstacles,_temp_parts,borders,gridSize) == True):
                     print "north"
                    
                     
                     if _temp_length == len(_temp_parts):
                       string_direction = ["North"] + _temp_parts[counter].parts
                       t+=_temp_parts[counter].depthFirstSearch(obstacles,_temp_parts,borders,gridSize,_resutl_list,["East","West"])
                     else:
                       string_direction = ["North"] + _temp_parts[len(_temp_parts)-1].parts
                       t+=_temp_parts[0].depthFirstSearch(obstacles,_temp_parts,borders,gridSize,_resutl_list,["North","South","East","West"])  
                     if "." in t:
                         _resutl_list+= t
                         break
                     _temp_parts = copy.deepcopy(parts)   
                 if "South" in directions and (_temp_parts[counter].Move("South",obstacles,_temp_parts,borders,gridSize) == True):
                         
                         print "south"

                       
                         if _temp_length == len(_temp_parts):
                            string_direction = ["South"] + _temp_parts[counter].parts
                            t+=_temp_parts[counter].depthFirstSearch(obstacles,_temp_parts,borders,gridSize,_resutl_list,["East","West"])
                         else:
                            string_direction = ["South"] + _temp_parts[len(_temp_parts)-1].parts
                            t+=_temp_parts[0].depthFirstSearch(obstacles,_temp_parts,borders,gridSize,_resutl_list,["North","South","East","West"])
                         if "." in t:
                             _resutl_list+=t
                             break
                         _temp_parts = copy.deepcopy(parts)                
                 if "East"in directions and (_temp_parts[counter].Move("East",obstacles,_temp_parts,borders,gridSize) == True):
    
                         print "east"

    
                         if _temp_length == len(_temp_parts):
                             string_direction = ["East"] + _temp_parts[counter].parts
                             t+=_temp_parts[counter].depthFirstSearch(obstacles,_temp_parts,borders,gridSize,_resutl_list,["South","North"])
                         else:
                             string_direction = ["East"] + _temp_parts[len(_temp_parts)-1].parts
                             t+=_temp_parts[0].depthFirstSearch(obstacles,_temp_parts,borders,gridSize,_resutl_list,["North","South","East","West"])
                         if "." in t:
                             _resutl_list+=t
                             break
                         _temp_parts = copy.deepcopy(parts)           
    
                 if "West" in directions and (_temp_parts[counter].Move("West",obstacles,_temp_parts,borders,gridSize)== True):
                         print "west"

    
                         if _temp_length == len(_temp_parts):
                             string_direction = ["West"] + _temp_parts[counter].parts
                             t+=_temp_parts[counter].depthFirstSearch(obstacles,_temp_parts,borders,gridSize,_resutl_list,["South","North"])
                         else:
                             string_direction = ["West"] + _temp_parts[len(_temp_parts)-1].parts
                             t+=_temp_parts[0].depthFirstSearch(obstacles,_temp_parts,borders,gridSize,_resutl_list,["North","South","East","West"])
                         if "." in t:
                             _resutl_list+=t
                             break
                         _temp_parts = copy.deepcopy(parts)
                 directions = ["North","South","East","West"]        
                               
             if string_direction != "":                       
                 _resutl_list.append(string_direction)
             return _resutl_list
   

   

    def Move(self, direction, obstacles, parts, borders, gridSize):
        
            temp_self = copy.deepcopy(self)
            temp_self_list = copy.deepcopy(self.parts)
            
            print "~~~~~~~~~~~~~~~" 
            mt = 0
            while (True):

                mt += 1
                flag = 0
                counter_position = 0
                tempPosition = 0
                for position in temp_self.parts:
                    
                    if direction == "North":

                        tempPosition = position - gridSize
                        print tempPosition
                        print "---------"
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
                                t = abs(differenace)

                                if differenace != 0:    
                                    new_part_position.append(new_part_position[0] + differenace)
                                if mt == 1:
                                    flag1 = False
                            for p in parts:
                                if self._eq_(p) == True:            
                                    p.parts = new_part_position
                            return flag1      




                    """ check if there is a hit between parts """        
                    for part in parts:
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
                            
                            parts.append(Part(self.index, new_part_position))
                            for p in parts:
                                if self._eq_(p) == True:
                                    parts.remove(p)
                            parts.remove(part)
                            return True
                        
                    temp_length = len(self.parts) - 1                        
                    if flag < 0 and temp_length == counter_position :
                        print "False"
                        return  False

                    temp_self.parts [counter_position] = tempPosition
                    counter_position += 1
 
 
    def _eq_ (self, other):
         if self.index == other.index:
             if self.parts == other.parts:
                 return True
         else:
              return False   
         






test=[Node.Node(Node.Node([],"",[]),"",[Part(1,[4]),Part(2,[7]),Part(3,[1])])]

#print Part(1,[1]).bfs([12],test,[1,4,5,8,9,12,13,16],4,0)
Part(1,[1]).ID([12],test,[1,4,5,8,9,12,13,16],4)




