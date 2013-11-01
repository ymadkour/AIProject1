from Queue import *
import copy

class Part:
    """docstring for part"""
    def __init__(self, index, parts):
        self.index = index
        self.parts = parts


    def depthFirstSearch(self, obstacles, parts, borders, gridSize,result_list,directions):


             _resutl_list = result_list[:]
             _resutl_length = len(result_list)
             _temp_parts = copy.deepcopy(parts)
             _temp_length = len(parts)
             string_direction = ""
             t = [""]
             if len(parts) == 1:
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
                        if tempPosition in part.parts and self._eq_(part) == False:
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
         

#print Part(1,[9,10]).Move("East",[1,7,15],[Part(1,[9,10]),Part(2,[8]),Part(3,[12])],[1,4,5,8,9,12,13,16],4)
print Part(1,[9,10]).Move("East",[1,7,15],[Part(2,[9]),Part(1,[8,12,11])],[1,4,5,8,9,12,13,16],4)

