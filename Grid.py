'''
Created on Oct 31, 2013

@author: Youssef
'''
import random
import robot
import Node

class Grid(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.grid_size = random.randint(2,10)
        self.robot_parts = random.randint(1,self.grid_size-1)
        self.obstacle_number = random.randint(0,(self.grid_size - 2))
        self.parts_locations = self.assignPartsPosition(self.robot_parts,self.grid_size)
        self.obstacles_locations = self.assignObstaclesPosition(self.obstacle_number,self.grid_size,self.parts_locations[0].parts_list)
        self.side_borders =  self.setBorders(self.grid_size)
        
        
    def assignPartsPosition(self,number,size):
        
        total = size ** 2
        temp_list = []
        i = 0
        while i < number:
            flag1 = True
            temp_position = random.randint(1,total)
            for p in temp_list:
                if temp_position == p.parts:
                    flag1 = False
            if flag1 == True:
                temp_list.append(robot.Part(i,[temp_position]))
                i +=1
      
        return [Node.Node(Node.Node([],"",[],0,0),"",temp_list,robot.getHeuristic(temp_list, size),0)]
    
    def assignObstaclesPosition(self,number,size, locations):
        
        total = size ** 2
        temp_list = []
        i = 0
        while i < number:
            flag  = True
            temp_position = random.randint(1,total)
            for p in locations:
                if [temp_position] == p.parts:
                    flag = False
            if flag  ==  True and temp_position not in temp_list:
                temp_list.append(temp_position)
                i += 1
      
        return temp_list     
    
    
    def setBorders (self,grid_size):
        
        total = grid_size ** 2
        temp_list = []
        i = grid_size
        j = 1
        while i <= total:
            temp_list.append(j)
            temp_list.append(i)
            i += grid_size
            j += grid_size
            
        return temp_list  

            