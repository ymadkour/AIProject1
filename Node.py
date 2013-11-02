'''
Created on Nov 2, 2013

@author: Youssef
'''

class Node(object):
    '''
    classdocs
    '''


    def __init__(self,parent,direction,parts_list):
        self.parent = parent
        self.direction =  direction
        self.parts_list = parts_list
        '''
        Constructor
        '''
        