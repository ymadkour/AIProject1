'''
Created on Nov 2, 2013

@author: Youssef
'''

class Node(object):
    '''
    classdocs
    '''


    def __init__(self,parent,direction,parts_list,heurisitc_value,cost):
        self.parent = parent
        self.direction =  direction
        self.parts_list = parts_list
        self.heurisitc_value = heurisitc_value
        self.cost = cost
        '''
        Constructor
        '''
        