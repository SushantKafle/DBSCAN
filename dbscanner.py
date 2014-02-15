'''
Created on Feb 13, 2014

@author: sushant
'''

from cluster import *
from pylab import *

class dbscanner:
    
    dataSet = []
    count = 0
    
    def dbscan(self,D,eps,MinPts):
        self.dataSet = D
        
        title(r'DBSCAN Algorithm', fontsize=18)
        xlabel(r'X Coordinates',fontsize=17)
        ylabel(r'Y Coordinates', fontsize=17)
        
        C = -1
        Noise = cluster('Noise')
        for point in D:
            if point['visited']:
                continue
            
            point['visited'] = True #point visited
            NeighbourPoints = self.regionQuery(point['coord'],eps)
            
            if len(NeighbourPoints) < MinPts:
                Noise.addPoint(point['coord'])
                point['member']=True
            else:
                name = 'Cluster'+str(self.count);
                C = cluster(name)
                self.count+=1;
                self.expandCluster(point,NeighbourPoints,C,eps,MinPts)
                X = C.getX()
                Y = C.getY()
                plot(X,Y,'o',label=name)
                #s=[15 for i in range(len(X))]
                #scatter(X,Y,label=name,s=s)
                hold(True)
                
                C.printPoints()
        X = Noise.getX()
        Y = Noise.getY()
        plot(X,Y,'x',label='Noise')
        hold(False)
        legend(loc='lower left')
        grid(True)
        show()
        Noise.printPoints()
        
    
    def expandCluster(self,point,NeighbourPoints,C,eps,MinPts):
        C.addPoint(point['coord'])
        point['member']=True
        
        for p in NeighbourPoints:
            if not p['visited']:
                p['visited'] = True
                np = self.regionQuery(p['coord'],eps)
                if len(np) >= MinPts:
                    NeighbourPoints = NeighbourPoints + np
            if not p['member']:
                C.addPoint(p['coord'])
                p['member'] = True
                     
    def regionQuery(self,P,eps):
        result = []
        for d in self.dataSet:
            if self.dist(P,d['coord']) < eps:
                result.append(d)
        return result
    
    def dist(self,P,d):
        squaredSum = 0
        for dim in range(len(P)):
            squaredSum += (P[dim]-d[dim])**2
        return squaredSum**0.5
            
            
            
        
                
                 
            
            
            
            
        