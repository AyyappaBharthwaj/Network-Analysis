import pandas as pd
import numpy as np
import networkx as nx 
import matplotlib.pyplot as plt

# Degree Centrality
G = pd.read_csv("E:/Data Science 18012022/Network Analysis/connecting_routes.csv")
G = G.iloc[0:2000, 1:20] # as the data is huge taking only 2000  details #
G.info()

print(nx.info(G))

g = nx.Graph()
g = nx.from_pandas_edgelist(G, source = 'Main Airport', target = 'Destination Airport')

print(nx.info(g))
## Graph has 602 Nodes and 1028 Edges

# Degree Centrality
d = nx.degree_centrality(g) 
print(d) 

pos = nx.spring_layout(g)
nx.draw_networkx(g, pos, node_size = 30, node_color = 'blue')

# closeness centrality
closeness = nx.closeness_centrality(g)
print(closeness)

## Betweeness Centrality 
b = nx.betweenness_centrality(g) 
print(b)

## Eigen-Vector Centrality
evg = nx.eigenvector_centrality(g) 
print(evg)

# cluster coefficient
cluster_coeff = nx.clustering(g)
print(cluster_coeff)

# Average clustering
cc = nx.average_clustering(g) 
print(cc)

