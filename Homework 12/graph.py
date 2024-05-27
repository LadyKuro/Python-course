import networkx as nx
import matplotlib.pyplot as plt

# Create a random undirected graph with more than 5 nodes
G = nx.gnm_random_graph(10, 20)

# Plot the graph
nx.draw(G, with_labels=True)
plt.savefig("graph.pdf")
plt.show()
