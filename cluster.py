'''
Created on Feb 13, 2014

@author: sushant
'''

class cluster:
    
    pList = []
    X = []
    Y = []
    name = ""
    
    def __init__(self,name):
        self.name = name
        self.pList = []
        self.X = []
        self.Y = []
    
    def addPoint(self,point):
        self.pList.append(point)
        self.X.append(point[0])
        self.Y.append(point[1])

    def getPoints(self):
        return self.pList
    
    def erase(self):
        self.pList = []
    
    def getX(self):
        return self.X
    
    def getY(self):
        return self.Y
    
    def has(self,point):
        
        if point in self.pList:
            return True
        
        return False
        
    def printPoints(self):
        print self.name+' Points:'
        print '-----------------'
        print self.pList
        print len(self.pList)
        print '-----------------'
    
        
        
        