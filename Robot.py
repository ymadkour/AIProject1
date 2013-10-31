from Queue import *
import copy

class Part:
    """docstring for part"""
    def __init__(self, index, parts):
        self.index = index
        self.parts = parts


    def depthFirstSearch(self, obstacles, parts, borders, gridSize,result_list,directions,flag):


             _resutl_list = result_list[:]
             _resutl_length = len(result_list)
             _temp_parts = parts[:]
             _temp_length = len(parts)
             string_direction = ""
             if len(parts) == 1:
                 print "done"
                 return ["."]
             
             for counter in range(0,len(parts)):
                 if "North" in directions and (parts[counter].Move("North",obstacles,_temp_parts,borders,gridSize) == True) and flag == False:
                     print "north"
                     string_direction = "North"
                     
                     if _temp_length == len(_temp_parts):
                       _resutl_list+=parts[counter].depthFirstSearch(obstacles,_temp_parts,borders,gridSize,_resutl_list,["East","West"],flag)
                     else:
                       _resutl_list+=parts[counter].depthFirstSearch(obstacles,_temp_parts,borders,gridSize,_resutl_list,["North","South","East","West"],flag)  
                     if "." in _resutl_list:
                         break
                     _temp_parts = parts[:]   
                 if "South" in directions and (parts[counter].Move("South",obstacles,_temp_parts,borders,gridSize) == True) and flag == False :
    
                         print "south"
                         string_direction = "South"
                       
                         if _temp_length == len(_temp_parts):
                            _resutl_list+=parts[counter].depthFirstSearch(obstacles,_temp_parts,borders,gridSize,_resutl_list,["East","West"],flag)
                         else:
                            _resutl_list+=parts[counter].depthFirstSearch(obstacles,_temp_parts,borders,gridSize,_resutl_list,["North","South","East","West"],flag)
                         if "." in _resutl_list:
                             break
                         _temp_parts = parts[:]                
                 if "East"in directions and (parts[counter].Move("East",obstacles,_temp_parts,borders,gridSize) == True) and flag == False:
    
                         print "east"
                         string_direction = "East"
    
                         if _temp_length == len(_temp_parts):
                             _resutl_list+=parts[counter].depthFirstSearch(obstacles,_temp_parts,borders,gridSize,_resutl_list,["South","North"],flag)
                         else:
                             _resutl_list+=parts[counter].depthFirstSearch(obstacles,_temp_parts,borders,gridSize,_resutl_list,["North","South","East","West"],flag)
                         if "." in _resutl_list:
                             break
                         _temp_parts = parts[:]           
    
                 if "West" in directions and (parts[counter].Move("West",obstacles,_temp_parts,borders,gridSize)== True) and flag == False:
                         print "west"
                         string_direction = "West"
    
                         if _temp_length == len(_temp_parts):
                             _resutl_list+=parts[counter].depthFirstSearch(obstacles,_temp_parts,borders,gridSize,_resutl_list,["South","North"],flag)
                         else:
                             _resutl_list+=parts[counter].depthFirstSearch(obstacles,_temp_parts,borders,gridSize,_resutl_list,["North","South","East","West"],flag)
                         if "." in _resutl_list:
                             break
                         _temp_parts = parts[:]
                               
                                    
             _resutl_list.append(string_direction)
             print _resutl_list
             return _resutl_list
   

   

    def Move(self, direction, obstacles, parts, borders, gridSize):
        
            temp_self = copy.deepcopy(self)
            temp_self_list = self.parts[:]
            
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
                        if tempPosition > (gridSize ** gridSize):
                            flag -= 1

                    elif direction == "East":
                        _tempPosition = position + 1
                        if position in borders and _tempPosition in borders:
                            flag -=1
                        else:    
                            tempPosition = position + 1
                        

                    elif direction == "West":
                        _tempPosition = position - 1
                        if position in borders and _tempPosition in borders:
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
                                elif mt == 1:
                                    flag1 = False    
                            self.parts = new_part_position
                            return flag1      




                    """ check if there is a hit between parts """        
                    for part in parts:
                        if tempPosition in part.parts and self != part:
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
                            if self in parts:
                                parts.remove(self)
                            parts.remove(part)
                            return True
                        
                    temp_length = len(self.parts) - 1                        
                    if flag < 0 and temp_length == counter_position :
                        print "False"
                        return  False

                    temp_self.parts [counter_position] = tempPosition
                    counter_position += 1
 
gridSize = 4
part2 = Part(1,[9])
part3 = Part(2,[10])
part4 = Part(3,[8])
part5 = Part(4,[12])
myList = [part2,part3,part4,part5]

print part2.Move("East",[1,7,15],myList,[1,4,5,8,9,12,13,16],4)





