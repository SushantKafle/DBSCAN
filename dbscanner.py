'''
Created on Feb 13, 2014

@author: sushant
'''

from cluster import *
from pylab import *

class dbscanner:
    
    dataSet = []
    count = 0
    visited = []
    member = []
    Clusters = []
    
    def dbscan(self,D,eps,MinPts):
        self.dataSet = D
        
        title(r'DBSCAN Algorithm', fontsize=18)
        xlabel(r'Dim 1',fontsize=17)
        ylabel(r'Dim 2', fontsize=17)
        
        C = -1
        Noise = cluster('Noise')
        
        for point in D:
            if point not in self.visited:
                self.visited.append(point)
                NeighbourPoints = self.regionQuery(point,eps)
                
                if len(NeighbourPoints) < MinPts:
                    Noise.addPoint(point)
                else:
                    name = 'Cluster'+str(self.count);
                    C = cluster(name)
                    self.count+=1;
                    self.expandCluster(point,NeighbourPoints,C,eps,MinPts)
                    
                    plot(C.getX(),C.getY(),'o',label=name)
                    hold(True)
        
        if len(Noise.getPoints())!=0:
            plot(Noise.getX(),Noise.getY(),'x',label='Noise')
            
        hold(False)
        legend(loc='lower left')
        grid(True)
        show()
                    
                    
            
    
    def expandCluster(self,point,NeighbourPoints,C,eps,MinPts):
        
        C.addPoint(point)
        
        for p in NeighbourPoints:
            if p not in self.visited:
                self.visited.append(p)
                np = self.regionQuery(p,eps)
                if len(np) >= MinPts:
                    for n in np:
                        if n not in NeighbourPoints:
                            NeighbourPoints.append(n)
                    
            for c in self.Clusters:
                if not c.has(p):
                    if not C.has(p):
                        C.addPoint(p)
                        
            if len(self.Clusters) == 0:
                if not C.has(p):
                    C.addPoint(p)
                        
        self.Clusters.append(C)
        
        #C.printPoints()
        
                    
                
                     
    def regionQuery(self,P,eps):
        result = []
        for d in self.dataSet:
            if (((d[0]-P[0])**2 + (d[1] - P[1])**2)**0.5)<=eps:
                result.append(d)
        return result
    
            
            
            
        
                
                 
            
            
            
            
        
