'''
Created on Oct 31, 2013

@author: Youssef
'''
import random
import robot

class Grid(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.grid_size = random.randint(2,10)
        self.robot_parts = random.randint(1,self.grid_size)
        self.obstacle_number = random.randint(0,(self.grid_size - 1))
        self.parts_loctions = self.assignPartsPosition(self.robot_parts,self.grid_size)
        self.obstacles_locations = self.assignObstaclesPosition(self.obstacle_number,self.grid_size,self.parts_loctions)
        self.side_borders =  self.setBorders(self.grid_size)
        
        
    def assignPartsPosition(self,number,size):
        
        total = number ** 2
        temp_list = []
        for i in range(0,number):
            temp_position = random.randint(1,total)
            if temp_position not in temp_list:
                temp_list.append(robot.Part(i,temp_position))
      
        return temp_list
    
    def assignObstaclesPosition(self,number,size, locations):
        
        total = number ** 2
        temp_list = []
        for i in range(0,number):
            temp_position = random.randint(1,total)
            if temp_position not in locations and temp_position not in temp_list:
                temp_list.append(temp_position)
      
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
            