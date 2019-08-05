import numpy as np
import random
import networkx as nx # networkx 是一个用于复杂网络的结构、动态和功能的创建、操作和研究的 Python 软件包
from IPython.display import Image
import matplotlib.pyplot as plt

# Load the graph
G_karate = nx.karate_club_graph() # 空手道俱乐部的社交网络
# Find key-values for the graph
pos = nx.spring_layout(G_karate)
# Plot the graph
nx.draw(G_karate, cmap = plt.get_cmap('rainbow'), with_labels=True, pos=pos)