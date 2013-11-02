from Queue import *
import copy

class Part:
    """docstring for part"""
    def __init__(self, index, parts):
        self.index = index
        self.parts = parts

    def _eq_ (self, other):
        if self.index == other.index:
            if self.parts == other.parts:
                return True
        else:
            return False
        

    def IDFS(self,obstacles, parts, borders, gridSize):
        depth = 0
        goal = len(parts)
        while True:
            for part in parts: #Flag that all parts has been visited/Also check depth/ When comes back from depth +1
                result = part.parts.DLS(parts, obstacles, borders, gridSize, goal, depth)
                if result == True:
                    return True
                try:
                    if result is None:
                        depth += 1
                    elif len(result) == goal:
                        return True
                    else:
                        depth+=1
                except Exception, e:
                    pass
            return False
            
    def DLS(self, parts, obstacles, borders, gridSize, goal, depth):
        if depth == 0 and len(self.parts) == goal:
            return self
        if len(self.parts) == goal:
            return True
        elif depth > 0:
            for child in self.expand(parts, obstacles, borders, gridSize): #All directions fail case
                #try:
                if(len(child) > 0):
                    child[0].DLS(child[1], obstacles, borders, gridSize, goal, depth-1)
#                 except Exception, e:
#                     print e
            return False
#         else:
#             return None    
    
    def expand(self, parts, obstacles, borders, gridSize):
        children = []
        originalList1 = copy.deepcopy(parts)
        originalList2 = copy.deepcopy(parts)
        originalList3 = copy.deepcopy(parts)
        originalList4 = copy.deepcopy(parts)
        tmp_node1 = copy.deepcopy(self)
        tmp_node2 = copy.deepcopy(self)
        tmp_node3 = copy.deepcopy(self)
        tmp_node4 = copy.deepcopy(self)
        
        if tmp_node1.Move("North",obstacles,originalList1,borders,gridSize) == True:
            tmpList = copy.deepcopy(originalList1)
            for p in parts: #Removing from the original List warning
                for item in tmpList:
                    if item._eq_(p) == True:
                        tmpList.remove(item)
            originalList1.reverse()
            child_and_parts = [tmpList[0], originalList1]
            children.append(child_and_parts)
            
        if tmp_node2.Move("South",obstacles,originalList2,borders,gridSize) == True:
            tmpList = copy.deepcopy(originalList2)
            for p in parts:
                for item in tmpList:
                    if item._eq_(p) == True:
                        tmpList.remove(item)
            originalList2.reverse()
            child_and_parts = [tmpList[0], originalList2]
            children.append(child_and_parts)
        
        if tmp_node3.Move("East",obstacles,originalList3,borders,gridSize) == True:
            tmpList = copy.deepcopy(originalList3)
            for p in parts:
                for item in tmpList:
                    if item._eq_(p) == True:
                        tmpList.remove(item)
            originalList3.reverse()
            child_and_parts = [tmpList[0], originalList3]
            children.append(child_and_parts)
            
        if tmp_node4.Move("West",obstacles,originalList4,borders,gridSize) == True:
            tmpList = copy.deepcopy(originalList4)
            for p in parts:
                for item in tmpList:
                    if item._eq_(p) == True:
                        tmpList.remove(item)
            originalList4.reverse()
            child_and_parts = [tmpList[0], originalList4]
            children.append(child_and_parts)
        
        return children

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
   

    def _eq_ (self, other):
         if self.index == other.index:
             if self.parts == other.parts:
                 return True
         else:
              return False   
         

    

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
 
gridSize = 4
part2 = Part(1,[9])
part3 = Part(2,[10])
part4 = Part(3,[8])
part5 = Part(4,[12])
myList = [part2,part3,part4,part5]

#print part2.Move("East",[1,7,15],myList,[1,4,5,8,9,12,13,16],4)
# print 'hello'

print part2.IDFS([1,7,15],myList,[1,4,5,8,9,12,13,16],4) , "Final Result"

#print part2.DLS(myList, [1,3,15], [1,4,5,8,9,12,13,16], 4, 4, 3)
#print Part(1,[9,10]).Move("East",[1,7,15],[Part(1,[9,10]),Part(2,[11,10,12])],[1,4,5,8,9,12,13,16],4)
#print part2.depthFirstSearch([1,7,15],myList,[1,4,5,8,9,12,13,16],4,0,[],["North","South","East","West"])
#print Part(1,[9,10]).Move("East",[1,7,15],[Part(1,[9,10]),Part(2,[8,12,11])],[1,4,5,8,9,12,13,16],4)