"""
 Aim : Designing a  random web-network of 10 webpages and find its page-rank and order them 
"""

# import libraries 
import networkx as nx            # for making graphs 
import matplotlib.pyplot as plt  # plotting graphs
import random                    # randomly generate nodes of graphs
import numpy as np

G = nx.DiGraph()                   # create a empty Directed graph 

# generate random network of webpages 

G.add_node(random.randint(0,9))

for _ in range(10):
  node = random.randint(0,9)
  G.add_node(node)
  G.add_edge(node,random.choice(list(G.nodes)))

nx.draw(G,with_labels=True)

plt.show()

graph_nodes = list(G.nodes)
n = len(graph_nodes)

print(n)
print(graph_nodes)

# Make matrix A show connections from ith-page pi to j-th pj . A[i][j] = 1 if connection from page i to page j exist else 0 

A = np.array([ np.array([0 for _ in range(n)]) for __ in range(n)])
i=0
for page_i in graph_nodes : 
  j=0
  for page_j in graph_nodes:
    if page_i in G.neighbors(page_j) : 
      A[i][j] = 1  
    j+=1
  i+=1 

A = A/np.sum(A,axis=0)
A = np.nan_to_num(A)
# Matrix B with all entries equals 1/n where n is no of pages in network 
B = (1/n)*np.ones((n,n))

# Make Transition matrix (M) with damping factor p(usually taken 0.15)(i.e. probability that page will be selected randomly from all 
# available web-pages.   as you might have guessed with (1-p) probability we will select page from all pages connected to given page

p = 0.15 
M = (1-p)*A + p*B        # as originally designed by Larry page and Sergey Brin . 
                         # Present implementation of  this algorithm is much more complicated.


# Power Iteration Method 
iterations=0

x = (1/n)*np.ones((n,1))  #initial guess of page-rank

while True :
  iteration+=1
  prev = x.copy()
  x = M.dot(x)
  error = abs(x - prev) 
  sos = sum(error)   # sum of square error
  if  sos <10**(-7): # exit condition
    break 

print("PageRank : " ,x.T)

rank_nodes = [[graph_nodes[i],x[i]] for i in range(len(x))]
rank_nodes = sorted(rank_nodes,key = lambda rank : rank[1])

print("Ranking of Pages ")
pages = [page[0] for page in rank_nodes]
print(*pages, sep=" < ")

