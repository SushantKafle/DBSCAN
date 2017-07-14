'''
Created on Feb 13, 2014

@author: sushant
'''

from cluster import Cluster
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.spatial import distance

class DBScanner:
    
    def __init__(self, config):
        self.eps = config['eps']
        self.min_pts = config['min_pts']
        self.dim = config['dim']
        self.clusters = set()
        self.cluster_count = 0
        self.visited = []
        self.color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    
    def dbscan(self, data):
        self.init_params()
        self.data = data

        ## Setting up the plot
        fig = plt.figure()

        axis_proj = 'rectilinear'
        if self.dim > 2:
            axis_proj = '%dd' % self.dim

        ax = fig.add_subplot(111, projection = axis_proj)
        
        #default noise cluster
        noise = Cluster('Noise', self.dim)
        self.clusters.add(noise)

        for point in data:
            if point not in self.visited:
                self.visited.append(point)
                neighbour_pts = self.region_query(point)
                if len(neighbour_pts) < self.min_pts:
                    noise.add_point(point)
                else:
                    name = 'cluster-%d' % self.cluster_count
                    new_cluster = Cluster(name, self.dim)

                    self.cluster_count += 1
                    self.expand_cluster(new_cluster, point, neighbour_pts)
                    
                    if self.dim == 2:
                        ax.scatter(new_cluster.get_X(), new_cluster.get_Y(), c = self.color[self.cluster_count % len(self.color)],
                        marker = 'o', label = name)
                    elif self.dim == 3:
                        ax.scatter(new_cluster.get_X(), new_cluster.get_Y(), new_cluster.get_Z(), marker = 'o', 
                        c = self.color[self.cluster_count % len(self.color)], label = name)

                    ax.hold(True)
        
        if len(noise.get_points()) != 0:
            if self.dim > 2:
                ax.scatter(noise.get_X(), noise.get_Y(), noise.get_Z(), marker = 'x', label = noise.name)
            else:
                ax.scatter(noise.get_X(), noise.get_Y(), marker = 'x', label = noise.name)
        
        print ("Number of clusters found: %d" % self.cluster_count)
        
        ax.hold(False)
        ax.legend(loc='lower left')
        ax.grid(True)
        plt.title(r'DBSCAN Clustering', fontsize=18)
        plt.show()
                    

    def expand_cluster(self, cluster, point, neighbour_pts):
        cluster.add_point(point)
        for p in neighbour_pts:
            if p not in self.visited:
                self.visited.append(p)
                np = self.region_query(p)
                if len(np) >= self.min_pts:
                    for n in np:
                        if n not in neighbour_pts:
                            neighbour_pts.append(n)
                    
                for other_cluster in self.clusters:
                    if not other_cluster.has(p):
                        if not cluster.has(p):
                            cluster.add_point(p)

                if self.cluster_count == 0:
                    if not cluster.has(p):
                        cluster.add_point(p)
                        
        self.clusters.add(cluster)
                    
    
    def get_distance(self, from_point, to_point):
        p1 = [from_point[k] for k in range(self.dim)]
        p2 = [to_point[k] for k in range(self.dim)]
        return distance.euclidean(p1, p2)

                     
    def region_query(self, point):
        result = []
        for d_point in self.data:
            if d_point != point:
                if self.get_distance(d_point, point) <= self.eps:
                    result.append(d_point)
        return result

    def init_params(self):
        self.clusters = set()
        self.cluster_count = 0
        self.visited = []

    
            
            
            
        
                
                 
            
            
            
            
        
