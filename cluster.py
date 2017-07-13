'''
Created on Feb 13, 2014

@author: sushant
'''

class Cluster:
    def __init__(self,  name, dim):
        self.name = name
        self.dim = dim
        self.pt_list = []
        self.X = []
        self.Y = []
        self.Z = []
    
    def add_point(self, point):
        self.pt_list.append(point)
        self.X.append(point[0])
        self.Y.append(point[1])

        ## if 3D
        if self.dim > 2:
            self.Z.append(point[2])

    def get_points(self):
        if self.dim > 2:
            return [self.X, self.Y, self.Z]
        
        return [self.X, self.Y]
    
    def erase(self):
        self.pList = []
    
    def get_X(self):
        return self.X
    
    def get_Y(self):
        return self.Y

    def get_Z(self):
        return self.Z
    
    def has(self,point):
        point in self.pt_list
            
    def __str__(self):
        print self.name + ' Points:'
        print '-----------------'
        print self.pt_list
        print len(self.pt_list)
        print '-----------------\n'
    
        
        
        